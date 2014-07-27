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

#main execution

args_len = len(sys.argv) - 1
args = sys.argv

flag = args[1]
number = args[2]

def checkArg(someString):
	if ('.' in someString):
		newList = someString.split('.', 1)
		stringToCheck = newList[0]
	 	return str.isdigit(stringToCheck)
	else:
		return str.isdigit(someString)

if (args_len != 2) or (checkArg(number) == False):
	print '''
	Usage: tempConv.py [switches] [temperature to convert in the form of 0.0]
			-c Celsius to Fahrenheit
			-f Fahrenheit to Celsius
	'''
	print checkArg(args[2])

else:
	temperature = float(args[2])
	flag = args[1]

	if flag == "-c":
		temp = tempConvert(temperature)
		print temp.calcFarenheit() + " F"
	else:
		temp = tempConvert(temperature)
		print temp.calcCelsius() + " C"


