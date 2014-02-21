#!/usr/bin/python

class ReverseString:
	def SetSring(self, string):
		self.data = string

	def DisplayString(self):
		print('The original string is: ' "%s" % self.data)

	def Reverse(self):
		self.data = self.data.lower() # Turn the string into all lowercase letters
		self.count = len(self.data) #count the charachter on the string
		self.reversed = ""

		# Reverse algorithm
		for w in xrange(self.count):
			self.reversed += self.data[self.count -1]
			self.count -=1

		# Return the reversed string on screen
		return self.reversed


string = raw_input("Write String to reverse: ")
w = ReverseString()
w.SetSring(string)
print "The reversed string is: ", w.Reverse()
