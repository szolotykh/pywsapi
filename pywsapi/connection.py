import json
from utils import *
from vswebsoket.message import CLOSE_MESSAGE

from messages import Request, Response

class  Connection(VSThread):
	def __init__(self, server, connection):
		self.wsconnection = connection
		self.server = server
		self.lock = Lock()
		super(Connection, self).__init__()

	def run (self):
		while not self.stopped():
			# Wait for message
			msg = self.wsconnection.receive_message()

			# Check if client cliosing connection
			if msg.type == CLOSE_MESSAGE:
				self.stop()
				self.server.remove_client(self)
				return

			# Hendle message
			request = Request()
			resp = None
			if not request.decode(msg.data):
				resp = Response (400)
			else:
				if request.path in self.server.paths:
					data = self.server.paths[request.path](request.data)
					resp = Response (200, data)
				else:
					resp = Response (404)
			sresp = resp.encode()
			self.wsconnection.send_message(sresp)

	def __del__(self):
		self.wsconnection.close()
