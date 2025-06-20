from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TelemetryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.drone_id = self.scope['url_route']['kwargs']['drone_id']
        self.group_name = f"telemetry_{self.drone_id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        # Echo or broadcast telemetry data
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'telemetry_message',
                'message': text_data,
            }
        )

    async def telemetry_message(self, event):
        await self.send(text_data=event['message'])