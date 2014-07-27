#!/usr/bin/python

import sys, os, os.path, urllib2, re, cookielib, time, datetime, locale


os.system('clear')

print '''
	Chose the Conversion:
	1. US Dollar -> Euro
	2. Euro -> US Dollar
	3. US Dollar -> British Pound
	4. British Pound -> US Dollar
	5. US Dollar -> Canadian Dollar
	6. Canadian Dollar -> US Dollar
	7. US Dollar -> Chines Yuan
	8. Chines Yuan -> US Dollar
	9. US Dollar -> Argentina Peso
	10. Argentina Peso -> US Dollar
	0. Exit
	'''
choice = raw_input("\t")

#Error checkig
def checkStringIsDigit(choice):
	if str.isdigit(choice):
		choice = int(choice) #turn the variable into an integer
		if choice == 0 or choice > 10: #chekc that selection is whithin allowed range
			return False
		else:
			return True
	else:
		return False


print checkStringIsDigit(choice)