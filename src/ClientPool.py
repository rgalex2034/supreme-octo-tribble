import socket

class ClientPool:
	def __init__(self):
		self.clients = []
	def write(self, data):
		for cl in self.clients:
			cl.send(data.encode())
			print("Mensaje enviado correctamente... o no")
