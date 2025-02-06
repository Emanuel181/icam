import json
from channels.generic.websocket import AsyncWebsocketConsumer

polls = {}  # Store active polls (for simplicity)

class PollConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.poll_id = self.scope['url_route']['kwargs']['poll_id']
        self.group_name = f"poll_{self.poll_id}"

        # Join the poll group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        # Send initial poll data
        if self.poll_id in polls:
            await self.send(text_data=json.dumps(polls[self.poll_id]))

    async def disconnect(self, close_code):
        # Leave the poll group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        if data['action'] == 'vote':
            option_index = data['option_index']
            polls[self.poll_id]['votes'][option_index] += 1

            # Broadcast updated poll data
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'poll_update',
                    'poll': polls[self.poll_id],
                }
            )

    async def poll_update(self, event):
        await self.send(text_data=json.dumps(event['poll']))
