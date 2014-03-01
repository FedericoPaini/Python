#!/usr/bin/python

import sys, os, os.path, urllib2, re, cookielib, time, datetime, locale

file = 'conv_rates.txt' #file containing the exchange rates

locale.setlocale( locale.LC_ALL, '' )

def check_file(file):
	if os.path.exists(file) == False:
		grab_web_rates()

	#check that the file is no more than 24 hours long
	if  time.time() - os.path.getmtime(file) > 86400: #file older than 24 hours
		#grab the currency exchange data form the internet
		grab_web_rates()
	else: #file is up to date
		return create_exchange_dict()

def create_exchange_dict():
	exchange_rates_dict = {}
	conversion_rates = open (file, 'r') #open file read only

	for line in conversion_rates:
		exchange_rates_dict[line.split(",")[0]] = line.split(",")[1]

	conversion_rates.close()
	return exchange_rates_dict

def grab_web_rates():
	conversion_rates = open (file, 'w')
	web = urllib2.urlopen('http://www.x-rates.com/table/?from=USD')
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
		if line >= 20:
			break
	conversion_rates.close()

def get_result(choice, amount):
	dict = create_exchange_dict()
	for exchange,rate in dict.items():
		if exchange == choice:
			result = amount * float(rate)
			return rate, result
			break
		else:
			error = "Exchange not found! -get_result()- "

def format_currency(value):
    return "{:,.2f}".format(value)

def main():
	os.system('clear')
	print '''
	Chose the Conversion:
	1. US Dollar -> Euro
	2. US Dollar -> British Pound
	3. US Dollar -> Canadian Dollar
	4. US Dollar -> Chines Yuan
	0. Exit
	'''
	choice = int(raw_input("\t"))
	while choice != 0:
		check_file(file)
		amount = float(raw_input("Dollar Amount: $"))

		if choice == 1: #Euro
			os.system('clear')
			choice = "USD-EUR"
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			e=u'\u20ac' #euro symbol
			amount = locale.currency( amount, grouping=True )
			print "Your amount: ", amount
			print "Converts to: ", e, format_currency(result)
			print "The US Dollar -> Euro exchnage rate is: ", rate
			break

		elif choice == 2: #GB
			choice = "USD-GBP"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			e = u'\xA3' #British Pound symbol
			amount = locale.currency( amount, grouping=True )
			print "Your amount: ", amount
			print "Converts to: ", e, format_currency(result)
			print "The US Dollar -> GBP exchnage rate is: ", rate
			break

		elif choice == 3: #Canadian Dollar
			choice = "USD-CAD"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			amount = locale.currency( amount, grouping=True )
			result = locale.currency( result, grouping=True )
			print "Your amount: ", amount
			print "Converts to: ", result
			print "The US Dollar -> Canadian Dollar exchnage rate is: ", rate
			break

		elif choice == 4: #Chinese Yuan
			choice = "USD-CNY"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			amount = locale.currency( amount, grouping=True )
			print "Your amount: ", amount
			print "Converts to Yuan: ", format_currency(result)
			print "The US Dollar -> Chinese Yuan exchnage rate is: ", rate
			break

#execution
main()
