#!/usr/bin/python

import sys, os, os.path, urllib2, re, cookielib, time, datetime, locale, random


def censor(text, word):
    lst = text.split()
    lst_items = len(lst)
    word_lenght = len(word)

    for w in lst:
    	if w == word:
       		lst[lst.index(word)] = "*" * word_lenght
       		error = False
       	else:
       		error = True

    if error == False:
    	new_text = " ".join(lst)
    else:
    	new_text = "Error! Word not present"

    return new_text



text = raw_input("Sentence to censor: ")
word = raw_input("word to censor: ")

print censor(text,word)
