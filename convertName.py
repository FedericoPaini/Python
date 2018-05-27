#!/usr/bin/python

#dictionary
char = {'a': '@', 'i': '!', 'e': '&', 's': '$', 'o': '#'}

#using a function
def Convert(str):
	converted_name = ""

	for letter in name:
		if letter in char:
			converted_name += char[letter]
		else:
			converted_name += letter
	return converted_name

#using a class
class ConvertName():
	convName = ""

	def __init__(self, string):
		self.string = string

	def Convert(self):
		for self.letter in self.string:
			if self.letter in char:
				self.convName += char[self.letter]
			else:
				self.convName += self.letter
		return self.convName


name = raw_input("Name: ").lower()
newName = ConvertName(name)
print "Using OO class: ", newName.Convert()

print "Using a function: ", Convert(name)