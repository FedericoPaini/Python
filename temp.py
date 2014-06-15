#!/usr/bin/python

import datetime

file = 'times.txt'

def recordTime(t):
	time_value = now.strftime("%m-%d-%Y %H:%M:%S")
	append_time = open (file, 'a')
	append_time.write(time_value + ' \n')


def count_lines(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

now = datetime.datetime.now()
recordTime(now)

print "Time recorded! Total line counts:", count_lines(file)
