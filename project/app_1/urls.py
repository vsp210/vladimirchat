from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name = 'index'),
    path('register/', register, name='register'),
    path('messages', messages, name='messages'),
    path('messages/<int:message_id>/', delete_message, name='delete_message'),
]
