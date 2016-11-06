import json

class Request():
	def __init__(self, method = "GET", path="/", params = [], data = ""):
		self.method = method
		self.path = path
		self.params = params
		self.data = data

	def encode(self):
		return json.dumps(self.__dict__)

	def decode(self, smsg):
		msg = json.loads(smsg)
		if "method" not in  msg or "path" not in msg:
			return False

		self.method = msg['method']
		self.path = msg['path']
		self.params = msg['params'] if "params" in msg else []
		self.data = msg['data'] if "data" in msg else ""
		return True

class Response():
	def __init__(self, code = "200", data = ""):
		self.code = code
		self.data = data

	def encode(self):
		return json.dumps(self.__dict__)

	def decode(self, smsg):
		msg = json.loads(smsg)
		if "code" not in msg:
			return False

		self.code = msg['code']
		self.data = msg['data'] if "data" in msg else ""
		return True
