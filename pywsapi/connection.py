import json
from utils import *
from vswebsoket.message import CLOSE_MESSAGE

from messages import Request, Response

class  Connection(VSThread):
	def __init__(self, server, connection):
		self.wsconnection = connection
		self.server = server
		self.isactive = True
		super(Connection, self).__init__()

	def is_active(self):
		return self.isactive

	def run (self):
		print("--> Client start")
		while not self.stopped():
			print("--> Client run")
			# Wait for message
			msg = self.wsconnection.receive_message()

			# Check if client cliosing connection
			if msg.type == CLOSE_MESSAGE:
				self.isactive = False
				self.wsconnection.close()
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
			print sresp
			self.wsconnection.send_message(sresp)
		print("--> Client end")
		del self

	def __del__(self):
		print "Conection distroied"
		self.wsconnection.close()
