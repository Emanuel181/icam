import json
from channels.generic.websocket import AsyncWebsocketConsumer

polls = {}

class PollConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.poll_id = self.scope['url_route']['kwargs']['poll_id']
        self.group_name = f"poll_{self.poll_id}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['action'] == 'vote':
            polls[self.poll_id]['votes'][data['option_index']] += 1
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'poll_update',
                    'poll': polls[self.poll_id],
                }
            )

    async def poll_update(self, event):
        await self.send(text_data=json.dumps(event['poll']))
