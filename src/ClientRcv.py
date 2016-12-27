import socket
import threading
import ClientPool

class ClientRcv(threading.Thread):
	def __init__(self, ip, port, pool):
		super(ClientRcv, self).__init__()
		self.ip = ip
		self.port = port
		self.pool = pool
		self.running = True
		self.srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.srv.bind((ip, port))
	def run(self):
		self.srv.listen(1)
		while self.running:
			client, addr = self.srv.accept()
			if not self.running:
				break
			print ("Cliente conectado")
			self.pool.clients.append(client)
