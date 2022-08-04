from django.urls import path
from chat import views

urlpatterns = [
    path("chat/", views.ChatListView.as_view()),
    path("chat/create/", views.CreateChatView.as_view()),
    path("message/create/", views.CreateMessageView.as_view()),
    path("message/delete/<int:id>/", views.DeleteMessageView.as_view())
]
