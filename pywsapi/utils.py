import threading

Lock = threading.Lock

# Thread class with stop method
class VSThread(threading.Thread):
	def __init__(self):
		super(VSThread, self).__init__()
		self._stop = threading.Event()

	def stop(self):
		self._stop.set()

	def stopped(self):
		return self._stop.isSet()
