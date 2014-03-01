#!/usr/bin/python

import random

letters = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','z','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'@','!','$','%','&','(',')','^']

numbers = ['1','2','3','4','5','6','7','8','9','0']

letters_count = int(len(letters))
numbers_count = int(len(numbers))

pwd_length = int(raw_input("Password length:"))

if pwd_length < 6:
	print"Error! Password length must be at least 6 characters!"
	exit()

alpha_weight = float(raw_input("Password letters weight (0.0-1.0):"))

if (alpha_weight < 0) or (alpha_weight > 1):
	print"Error! Password weight must be between 0.0 and 1.0!"
	exit()

pwd_length_alpha = int(pwd_length * alpha_weight)
pwd_length_num = int(pwd_length - pwd_length_alpha)


#create random a string
def Pwd(counter, length, alphanum):

	string = ""

	while length !=0 :
		rdm = random.randrange(counter)
		digit = alphanum[rdm]
		string  += digit
		length -= 1

	return string

#scramble the strings
def Scramble(str1, str2):
	str = str1 + str2
	result = ''.join(random.sample(str, len(str)))
	return result

alpha = Pwd(letters_count, pwd_length_alpha, letters)
num = Pwd(numbers_count, pwd_length_num, numbers)

percent = str(int(alpha_weight * 100))

print "The password is: ",  Scramble(alpha, num)
print ("The password weight is {0}% letters".format(percent))

