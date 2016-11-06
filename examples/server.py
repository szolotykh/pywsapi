from pywsapi import APIServer
from time import sleep

server = APIServer('127.0.0.1', 7777)

@server.route("string")
def get_string(data):
	return "My string."

server.start()
try:
	while True:
		print "working"
		sleep(1)
except:
	server.server.interrupt_accept()
	server.join()
