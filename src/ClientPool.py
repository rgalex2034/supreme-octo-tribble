import socket

class ClientPool:
	def __init__(self):
		self.clients = []
	def write(self, data):
		for cl in clients:
			cl.send(data)
