#!/usr/bin/python


def FizzBuzz(number):

	for x in xrange(1, number+1):
		if (x % 3) == 0 and (x % 5) == 0:
			print "FizzBuzz!"
		elif (x % 3) == 0:
			print "Fizz"
		elif (x % 5) == 0:
			print "Buzz"
		else:
			print x


number = int(raw_input("Number Range for FizzBuzz Challenge? "))
FizzBuzz(number)