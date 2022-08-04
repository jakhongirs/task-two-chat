import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer




class ChatConsumer(WebsocketConsumer):
    room_group_name = "clc"


    def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_group_name = f'chat_{self.room_name}'
        # self.room = Room.objects.get(name=self.room_name)

        # connection has to be accepted
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        print(text_data_json)

        # send chat message event to the room
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps(event['data']))

    def chat_message_without_data(self, event):
        self.send(text_data=json.dumps(event))