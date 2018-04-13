import random
class IP:

	def __init__(self):
		self.ip = ""

	def generateIP4(self,x,y,z,w):
		self.ip = x + "." + y + "." + z + "." + w
		return self.ip
	
	def generateRandomIP4(self):
		self.ip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
		return self.ip
