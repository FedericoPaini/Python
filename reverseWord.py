#!/usr/bin/python


word = raw_input("Word to be reversed: ")
count = len(word)
reverse = ""

for x in xrange(0,count):
	reverse += word[count-1]
	count -=1

print "The word reversed is:", reverse