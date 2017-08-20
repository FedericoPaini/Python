#!/usr/bin/python

import sys, os, os.path, urllib2, re, cookielib, time, datetime, locale

file = 'conv_rates.txt' #file containing the exchange rates
user_agent="Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0)"
url="http://www.x-rates.com/table/?from=USD"

conversion_rates = open (file, 'w')
request = urllib2.Request(url, None, { 'User-Agent' : user_agent})
web = urllib2.urlopen(request)
html = web.read()
line = 1
titles = re.findall(r'<td class=\'rtRates\'><a href=\'/graph/\?from=(.*?)</td>', html)
for title in titles:
	title = title.replace("amp;to=", "")
	title = title.replace("&", "-")
	title = title.replace("'>", ",")
	title = title.replace("</a>", " ")
	title = title.replace("  ", "")
	title = title.rstrip()
	conversion_rates.write(title + ' \n')
	line += 1
	if line >= 100:
		break
conversion_rates.close()

#Remove Duplicate
lines = open(file, 'r').readlines()
lines_set = set(lines)
out  = open(file, 'w')

for line in lines_set:
    out.write(line)
