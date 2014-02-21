#!/usr/bin/python

class ReverseString:
	def setstring(self, string):
		self.data = string

	def displaystring(self):
		print('The original string is: ' "%s" % self.data)

	def reverse(self):
		self.data = self.data.lower() # Turn the string into all lowercase letters
		self.count = len(self.data) #count the charachter on the string
		self.reversed = ""

		# Reverse algorithm
		for w in xrange(self.count):
			self.reversed += self.data[self.count -1]
			self.count -=1

		# Print the reversed string on screen
		print('The reversed string is: ' "%s" % self.reversed)


w = raw_input("Type the word or string to be reversed: ")

newString = ReverseString()
newString.setstring(w)
newString.displaystring()
newString.reverse()