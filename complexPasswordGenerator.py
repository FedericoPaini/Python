#!/usr/bin/python

import random

# Password rules:
# Minimum 8 characters long
# At least 1 lower case + 1 upper case + 1 number + 1 special character
# Random selection

lowerCaseLetters = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','z','u','v','w','x','y','z']
upperCaseLetters = ['A','B','C','D','E','F','G','H','I','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
specialCharacters = ['@','!','$','%','&','(',')','^','?','*','#']
numbers = ['1','2','3','4','5','6','7','8','9','0']

passDict = {}

minPasswordLenght = 8


def main():
	pwd_length = int(raw_input("Password length (8 characters minimum):"))

	if pwd_length < minPasswordLenght:
		pwd_length = minPasswordLenght #enforces the minimum lenght requirement

	array = passAlg(pwd_length)
	passDict = {"lowerCaseLetters":  array[0], "upperCaseLetters": array[1], "numbers": array[2], "specialCharacters": array[3]}

	print passDict

	#iterationg through the dcitionary


def passAlg(pwd_length): #algorithm to select the password composition
	array = []
	while sum(array) != pwd_length:
		n1 = random.randrange(1, pwd_length) # Lower case letters
		n2 = random.randrange(1, pwd_length) # Uppoer case letters
		n3 = random.randrange(1, pwd_length) # Numbers
		n4 = random.randrange(1, pwd_length) # Special characters
		array =[n1, n2, n3, n4]
	return array


#execution
main()

