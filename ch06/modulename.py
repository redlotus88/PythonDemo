class FirstClass():				#Define a class object
	def setdata(self, value):	#Define class methods
		self.data = value		#self is the instance
	def display(self):
		print(self.data)		#self.data: per instance


class SecondClass(FirstClass):		#Inherits setdata
	def display(self):				#Changes display
		print('Current value = "%s"' % self.data)


class ThirdClass(SecondClass):
	def __init__(self, value):
		self.data = value
	def __add__(self, other):
		return ThirdClass(self.data + other)
	def __str__(self):
		return '[ThirdClass: %s]' % self.data
	def mul(self, other):
		self.data *= other



