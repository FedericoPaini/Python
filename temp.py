#!/usr/bin/python

import sys, os, os.path, urllib2, re, cookielib, time, datetime, locale

file = 'conv_rates.txt' #file containing the exchange rates
exchange_rates_dict = {}
conversion_rates = open (file, 'r') #open file read only

for line in conversion_rates:
	exchange_rates_dict[line.split(",")[0]] = line.split(",")[1].rstrip()
	#print line

conversion_rates.close()
print exchange_rates_dict
