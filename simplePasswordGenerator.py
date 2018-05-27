#!/usr/bin/python

import random

alphabet = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','z','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'@','!','$','%','&','1','2','3','4','5','6','7','8','9','0']

def RandomPwd(seed):
	counter = len(alphabet)
	pwd =""

	#create random pasword string
	while seed !=0 :
		select = random.randrange(counter)
		letter = alphabet[select]
		pwd  += letter
		seed -= 1
	return pwd

seed = int(raw_input("Password lenght: "))

print "The password is: ", RandomPwd(seed)
