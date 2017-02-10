
class Player():
	def __init__(self):
		self.name = input("Please enter your name:")

	def __str__(self):
		return '{}'.format(self.name)