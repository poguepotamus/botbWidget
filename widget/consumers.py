import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class BotbConsumer(WebsocketConsumer):
	def __init__(self):
		self.group_name = 'botb22'

	def connect(self):
		async_to_sync(self.channel_layer.group_add)(
			self.group_name, self.channel_name
		)

		self.accept()

	def disconnect(self, _):
		# Leave room group
		async_to_sync(self.channel_layer.group_discard)(
			self.group_name, self.channel_name
		)

	# Received a message from the websocket
	def receive(self, text_data):
		# Sending a message to the group
		print('received')
		async_to_sync(self.channel_layer.group_send)(
			self.group_name, {
				'type': 'botb_update',
				'update': json.loads(text_data)['update']
			}
		)


	def botb_update(self, event):
		update = event['update']
		print('update')

		# Sending a message to client websockets
		self.send(text_data=json.dumps({'update': update}))
