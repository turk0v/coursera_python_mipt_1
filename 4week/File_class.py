import os
import tempfile


class File:
	def __init__(self,route):
		self.route = route

	def write(self, string):
		with open(self.route,'w') as f:
			f.write(string)

	def __add__(self,obj):
		with open (self.route) as f1, open(obj.route) as f2:
			content = f1.read() + f2.read()
			new_file = File(os.path.join(tempfile.gettempdir(), 'new'))
			new_file.write(content)
			return new_file

	def __str__(self):
		return self.route

	def __getitem__(self,index):

		with open (self.route) as f:
			return f.readlines()[index]




# w