from vswebsoket.client import  WSClient, CLOSE_MESSAGE
from connection import Connection
from messages import Request, Response
import socket

class APIClient(WSClient):
	def __init__(self):
		super(APIClient, self).__init__()
		self.connection = None
		self.onclose_callback = None

	def connect(self, url):
		self.connection = super(APIClient, self).connect(url)
		return self.connection

	def onclose(self, callback):
		self.onclose_callback = callback

	def api_request(self, method, path, params = [], data=""):
		try:
			self.connection.send_message(Request(method, path, params, data).encode())
			sresp = self.connection.receive_message()
			# Check if client cliosing connection
			if sresp.type == CLOSE_MESSAGE:
				if self.onclose_callback != None:
					self.onclose_callback()
				return None
			resp = Response()
			resp.decode(sresp.data)
			return resp
		except socket.error:
			if self.onclose_callback != None:
				self.onclose_callback()
			return None

	def get(self, path, params = [], data=""):
		return self.api_request("GET", path, params, data)

	def post(self, path, param = [], data=""):
		return self.api_request("POST", path, params, data)

	def close(self):
		self.connection.close()
