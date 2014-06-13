#!/usr/bin/python

import datetime, urllib2

file = 'http://www.paini.org/federico/times.txt'
timeDifference = datetime.timedelta(hours = 2)

def recordTime(t):
	time_value = now.strftime("%m-%d-%Y %H:%M:%S")
	append_time = open (file, 'a')
	append_time.write(time_value + ' \n')


def count_lines(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def getFile(file):
	data = urllib2.urlopen(file).read()
	data = data.split("\n")
	data = data + timeDifference
	count = 1
	for line in data:
		print line
		count = count + 1
	print "Total line counts:", count

now = datetime.datetime.now() + timeDifference

getFile(file)


