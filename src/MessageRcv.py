import socket
import threading
import ClientPool

class MessageRcv(threading.Thread):
	def __init__(self, ip, port, pool):
		super(MessageRcv, self).__init__()
		self.ip = ip
		self.port = port
		self.pool = pool
		self.running = True
		self.srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.srv.bind((ip, port))
	def run(self):
		while self.running:
			data, addr = self.srv.recvfrom(1024)
			if not self.running:
				break
			self.pool.write(data)
