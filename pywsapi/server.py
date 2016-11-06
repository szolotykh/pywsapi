from vswebsoket.server import WSServer
from connection import Connection
from messages import Request, Response
from utils import *

class AcceptProcessor(VSThread):
	def __init__(self, server):
		self.server = server

	def run(self):
		print "Waiting for connection"
		wsconnection = self.ws.accept ()
		if not wsconnection:
			print ("Stop waiting")
			break
		connection = Connection(self, wsconnection)
		self.server.add_client(connection)
		connection.start()
		print ("Client connected")



class APIServer(VSThread):
	def __init__(self, address, port):
		super(APIServer, self).__init__()
		self.ws = WSServer(address, port)
		self.paths = dict()
		self.clients = []


	def route(self, s):
		def wrapper(callback):
			self.paths[s] = callback
			return
		return wrapper

	def add_client(self, client):
		self.clients += [client]

	def remove_client(self, client):
		self.clients.remove(client)

	def run(self):
		while True:
			for client in list(self.clients):
				if not client.is_active()
					self.remove_client(client)

		print("Stopping.......")
		print self.client
		print("---------------")
		if self.client:
			self.client.wsconnection.close()
			self.client.stop()


	def __del__(self):
		print ("Server stop")
