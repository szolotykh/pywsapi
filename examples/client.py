from pywsapi import APIClient
from time import sleep
from  sys import exit

def onclose():
	print "Connection closed"
	exit()

if __name__ == "__main__":
	try:
		client = APIClient()
		client.onclose(onclose)
		client.connect("ws://127.0.0.1:7777")
		print "Connected to server"
		while True:
			response = client.get("string")
			print "Code:" + str(response.code)
			print "Data:" + response.data
			sleep(1)
	except KeyboardInterrupt:
		client.close()
		exit()
