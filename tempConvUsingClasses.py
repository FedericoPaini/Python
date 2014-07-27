#!/usr/bin/python

import sys

class tempConvert:
	def __init__(self, temperature):
		self.temperature = temperature

	def calcCelsius(self):
		self.temp = (self.temperature - 32) * ( float(5)/float(9) )
		self.temp = '{:.1f}'.format(self.temp)
		return self.temp

	def calcFarenheit(self):
		self.temp = ( self.temperature * ( float(9)/float(5) ) ) + 32
		self.temp = '{:.1f}'.format(self.temp)
		return self.temp

def checkArg(someString):
	if ('.' in someString):
		newList = someString.split('.', 1)
		left = newList[0]
		right = newList[1]
	 	if (str.isdigit(left) == True) and (str.isdigit(right) == True):
	 		return True
	 	else:
	 		return False
	else:
		return str.isdigit(someString)

#main execution

args_len = len(sys.argv) - 1
args = sys.argv

if (args_len != 2) or (checkArg(args[2]) == False):
	print '''
	Usage: [switches] [temperature to convert]
			-c Celsius to Fahrenheit
			-f Fahrenheit to Celsius
	'''
else:
	temperature = float(args[2])
	flag = args[1]

	if flag == "-c":
		temp = tempConvert(temperature)
		print temp.calcFarenheit() + " F"
	else:
		temp = tempConvert(temperature)
		print temp.calcCelsius() + " C"


