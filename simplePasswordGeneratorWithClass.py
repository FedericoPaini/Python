#!/usr/bin/python

import random

alphabet = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','z','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'@','!','$','%','&','1','2','3','4','5','6','7','8','9','0']

counter = len(alphabet)

class PasswordGenerator:
	def __init__(self, seed):
		self.seed = seed

	def GeneratePwd(self):
		self.pwd =""
		self.weight = random.randrange(self.seed)

		#create random pasword string
		while self.seed !=0 :
			self.select = random.randrange(counter)
			self.letter = alphabet[self.select]
			self.pwd  += self.letter
			self.seed -= 1
		return self.pwd

seed = int(raw_input("Password lenght: "))
newPass = PasswordGenerator(seed)
print newPass.GeneratePwd()
