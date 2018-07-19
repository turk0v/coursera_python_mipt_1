import socket
import time

class ClientError(Exception):
	pass



class Client:
	def __init__(self,host,port,timeout = None):
		self.socket = socket.create_connection((host,port), timeout)

	def send(self,msg):
		try:
			self.socket.sendall(msg.encode("utf8"))
		except socket.error as error:
			raise ClientError("Error sending data", error)

	def recieve(self):
		try:
			got_value = self.socket.recv(1024).decode("utf8")
		except socket.error as error:
			raise ClientError("Error recieving data", error)
		status,data = got_value.split("\n", 1)
		data = data.strip()

		if status == 'error':
			raise ClientError(data)
		return data


	def put(self,key,value,timestamp = None):
		if not timestamp:
			timestamp = int(time.time())
		msg = "put {0} {1} {2}\n".format(key,str(value),str(timestamp))
		self.send(msg)
		self.recieve()

	def get(self,key):
		data = {}
		msg = "get {}\n".format(key)
		self.send(msg)
		answer = self.recieve()
		items = [item.split() for item in answer.split('\n')]
		if items == [[]]:
			return data
		else:
			for i in range(0,len(items)):
				if items[i][0] not in data:
					data[items[i][0]] = []
				data[items[i][0]].append((int(items[i][2]), float(items[i][1])))
			if key == '*':
				return data
			else:
				data = {key: data.get(key)}
				return data







