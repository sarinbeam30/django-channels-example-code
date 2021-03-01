import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
        

class RealTimeConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.channel_group_name = 'core-realtime-data'
        # Join room group
        await self.channel_layer.group_add(
            self.channel_group_name,
            self.channel_name
        )
        await self.accept()
        print("----------connected--------")

    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.channel_group_name,
            self.channel_name
        )
        print("DISCONNECED CODE: ", close_code)
        print("----------disconnect--------")

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        print("RECEIVE : " + text_data)
        data = json.loads(text_data)
        message = data['message']
        await self.channel_layer.group_send(
            self.channel_group_name,{
                "type": 'log_message',
                "message": message
            }
        )
        print("----------receive--------")


    async def log_message(self, event):
        print('EVENT : ' + str(event))
        message = event["message"]
        await self.send(text_data=json.dumps({
            "message": message
        }))

        print("---------------LOG------------")

        
