#!/usr/bin/python

import sys, os, os.path, urllib2, re, cookielib, time, datetime

def menu():
	os.system('clear')
	print '''
	Chose the Conversion:
	1. USD -> EUR
	2. USD -> British Pound
	3. USD -> CAD
	4. USD -> Chines Yuan
	5. USD -> Australian Dollar
	7. USD -> Indian Rupee
	8. USD -> Swedish Krona
	9. USD -> Norwegian Krone
	10. USD -> Icelandic Krona
	11. USD -> Danish Krone
	12. USD -> Japanese Yen
	13. USD -> Swiss Franc
	14. USD -> Argentine Peso
	15. USD -> Brazilian Real
	00. Exit
	'''

	choice = int(raw_input("\t"))
	return choice


def get_web_data():
	timeStamp = datetime.datetime.now()
	conversion_rates = open ('conv_rates.txt', 'w')
	web = urllib2.urlopen('http://www.x-rates.com/table/?from=USD')
	html = web.read()

	try:
		line = 1
		titles = re.findall(r'<td class=\'rtRates\'><a href=\'/graph/\?from=(.*?)</td>', html)
		conversion_rates.write(str(timeStamp) + '\n')
		for title in titles:
			title = title.replace("amp;to=", "")
			title = title.replace("&", "-")
			title = title.replace("'>", ",")
			title = title.replace("</a>", " ")
			title = title.replace("  ", "")
			title = title.rstrip()
			conversion_rates.write(title + ' \n')
			line += 1
			if line >= 20:
				break
		conversion_rates.close()

	except Exception, e:
		print str(e)


# Execution
#choice = ''
#while choice != 00:
#	choice = menu()
#	if choice == 1:
#		print "You chose 1!"
#		break
#	elif choice == 2:
#		print "You chose 2!"
#		break
#	elif choice == 3:
#		print "You chose 3!"
#		break
get_web_data()