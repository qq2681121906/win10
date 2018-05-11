
class Dog(object):
	def __init__(self):
		self.__name = "xiaowang"
	
	def getName(self):
		return self.__name
	'''
	def __del__(self):
		pass
	
	def __new__(cls):
		super().__new__()

	def __str__(self):
		pass
	'''
dog = Dog()
print(dog.getName())