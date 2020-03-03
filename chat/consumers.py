from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from chat.models import ChatLog

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        #Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        #Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    #Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        handle = text_data_json['handle']
        message = text_data_json['message']
        date = text_data_json['date']
        await self._save_message(message, handle, date)

        #Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'handle': handle,
                'date':date
            }
        )
    #Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        handle = event['handle']
        date = event['date']
        # await self._save_message(message, handle, date)

        await self.send(text_data=json.dumps({ #この中身が「onmessage」に
            'message': message,
            'handle': handle,
            'date': date
        }))

    @database_sync_to_async
    def _save_message(self, message, handle, date):
        ChatLog.objects.create(
            room_name = self.room_name,
            message = message,
            handle = handle,
            date = date
        )
