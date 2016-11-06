from vswebsoket.client import  WSClient
from connection import Connection
from messages import Request, Response

class APIClient(WSClient):
	def __init__(self):
		super(WSClient, self).__init__()

	def api_request(self, method, path, params = [], data=""):
		self.client.send_message(Request(method, path, params, data).encode())
		sresp = self.client.receive_message()
		resp = Response()
		resp.decode(sresp)
		return resp

	def get(self, path, params = [], data=""):
		return self.api_request("GET", path, params, data)

	def post(self, path, param = [], data=""):
		return self.api_request("POST", path, params, data)

	def __del__(self):
		self.client.close()
