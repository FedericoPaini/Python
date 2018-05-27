#!/usr/bin/python

import sys, os, os.path, urllib2, re, cookielib, time, datetime, locale, random, math

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def censor(text, word):
    lst = text.split()
    lst_items = len(lst)
    word_lenght = len(word)

    for w in lst:
    	if w == word:
       		lst[lst.index(word)] = "*" * word_lenght

    new_text = " ".join(lst)
    return new_text

def count(sequence, argument):
	count = 0
	for item in sequence:
		if item == argument:
			count +=1
	return count

def purify(numbers):
	new_numbers = []
	for n in numbers:
		if n % 2 == 0:
			new_numbers.append(n)
	return new_numbers

def product(numbers):
	product = 1
	for n in numbers:
		product *= n
	return product

def remove_duplicates(text):
	new_list = []
	for l in text:
		if l not in new_list:
			new_list.append(l)
	return new_list

def median(text):
	text_lenght = len(text)
	text = sorted(text)

	if text_lenght % 2 == 0: #even list
		find_median = text_lenght / 2
		n1 = text[find_median - 1]
		n2 = text[find_median]
		result = float (  ( (float(n1) + float(n2)) / 2)  )
		return result

	else: #odd list
		find_median = text_lenght / 2
		return text[find_median]

def grades_sum(scores):
    tot = 0
    for s in scores:
         tot += s
    return tot

print grades_sum([47, 12, 94, 18, 70, 57, 25])


