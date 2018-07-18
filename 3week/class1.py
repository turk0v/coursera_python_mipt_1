class FileReader:
	
	def __init__(self,route):
		self.route = route

	def read(self):
		try:
			with open(self.route, 'r') as f:
				return(f.read())

		except IOError:
				return("")

def main():
	reader = FileReader("classfile.txt")
	print(reader.read())



if __name__  == '__main__':
	main()