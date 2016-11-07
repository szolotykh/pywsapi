from vswebsoket.server import WSServer
from connection import Connection
from messages import Request, Response
from time import sleep
from utils import *

class AcceptingProcessor(VSThread):
	def __init__(self, server):
		super(AcceptingProcessor, self).__init__()
		self.server = server

	def run(self):
		while True:
			wsconnection = self.server.ws.accept ()
			if not wsconnection:
				break
			connection = Connection(self.server, wsconnection)
			self.server.add_client(connection)
			connection.start()
			connection = None

	def stop(self):
		self.server.ws.interrupt_accept()
		self.join()



class APIServer():
	def __init__(self, address, port):
		self.ws = WSServer(address, port)
		self.paths = dict()
		self.clients = []
		self.lock = Lock()
		self.accepting_processor = AcceptingProcessor(self)

	def route(self, s):
		def wrapper(callback):
			self.paths[s] = callback
			return
		return wrapper

	def add_client(self, client):
		with self.lock:
			self.clients += [client]

	def remove_client(self, client):
		with self.lock:
			self.clients.remove(client)

	def start(self):
		self.accepting_processor.start()

	def stop(self):
		self.accepting_processor.stop()
		self.accepting_processor.join()
		for client in list(self.clients):
			self.remove_client(client)
			client.stop()
			client.join()
