from django.urls import path
from chat import views

urlpatterns = [
    path("list/", views.ChatListView.as_view()),
    path("create/", views.CreateChatView.as_view())
]
