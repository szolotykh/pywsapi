from pywsapi import APIServer
from time import sleep

if __name__ == "__main__":
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
		server.stop()
