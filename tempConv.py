#!/usr/bin/python

import sys

args_len = len(sys.argv) - 1
args = sys.argv

if args_len != 2 :
	print '''
	Usage: tempConv.py [switches] -v [value to convert]
			-c Celsius to Fahrenheit
			-f Fahrenheit to Celsius
	'''
elif args[1] == "-c":
	c = float(args[2])
	f = ( c * ( float(9)/float(5) ) ) + 32
	f = '{:.1f}'.format(f)

	print str(f) + " F"

elif args[1] == "-f":
	f = float(args[2])
	c = (f - 32) * ( float(5)/float(9) )
	c = '{:.1f}'.format(c)

	print str(c) + " C"

else:
	print '''
	Usage: tempConv.py [switches] -v [value to convert]
			-c Celsius to Fahrenheit
			-f Fahrenheit to Celsius
	'''