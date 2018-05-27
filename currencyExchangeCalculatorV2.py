#!/usr/bin/python
#Version 2.0 
#By Federico Paini federico.paini@gmail.com

import sys, os, os.path, urllib2, re, cookielib, time, datetime, locale

#Variables
file = 'conv_rates.txt' #Text database file containing the exchange rates
e=u'\u20ac' #euro symbol
b = u'\xA3' #British Pound symbol
y=u'\u00a5' #yuan symbol
r=u'\u0052' #real symbol
p=u'\u20b1' #peso symbol

locale.setlocale( locale.LC_ALL, '' )

#Procedures
def checkFile(file): #create currency exchange text database file
	#check that the file exists and it's not empty
	if os.path.exists(file) == False or os.stat(file).st_size == 0:
		grabWebRates()

	#check that the file is no more than 24 hours old
	if  time.time() - os.path.getmtime(file) > 86400: #file older than 24 hours
		#grab the currency exchange data form the internet
		grabWebRates()
	else: #file is up to date
		return create_exchange_dict()

def stripComma(amount): #Strips commas and return a float
	if ',' in amount:
		amount = ''.join(e for e in amount if e.isdigit() or e == '.')
		amount = float(amount)
	else:
		amount = float(amount)
	return amount

def format_currency(value):
    return "{:,.2f}".format(value)

def create_exchange_dict(): #Create exchange dictionary
	exchange_rates_dict = {}
	with open(file, 'r') as fileobj:
	  for line in fileobj:
	      exchange_rates_dict[line.split(",")[0]] = line.split(",")[1].rstrip()
	return exchange_rates_dict

def grabWebRates():
	user_agent="Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0)"
	url="http://www.x-rates.com/table/?from=USD"
	conversion_rates = open (file, 'w+')
	request = urllib2.Request(url, None, { 'User-Agent' : user_agent})
	web = urllib2.urlopen(request)
	html = web.read()
	line = 1
	titles = re.findall(r'\?from=(.*?)</td>', html)
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

def errorTrap(errorCode): #Error handling
	if errorCode == 1:
		os.system('clear')
		print ("Select only numbers please! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit()
	
	elif errorCode == 2:
		os.system('clear')
		print ("Selection out of Bounds! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit()

	elif errorCode == 3:
		os.system('clear')
		print ("Exchange rate not found! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit()

	elif errorCode == 9:
		print ("Something went wrong! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit()

	elif errorCode == 10:
		os.system('clear')
		print ("Thanks for using Currency Calculator! (C) 2018 Federico Paini \n")
		exit()

	else: #exit gracefully
		os.system('clear')
		print ("Thanks for using Currency Calculator! (C) 2018 Federico Paini \n")
		exit()
	
	return 0

def checkChoice(choice, menuLimit):
	try: #check that the selection is a digit or exit with error
		int(choice)
	except Exception: #Error
		errorTrap(1)
	else:
		if int(choice) == 0: #Exit the program
			errorTrap(10)
		elif int(choice) <= int(menuLimit): #Error
			return int(choice)
		else:
			errorTrap(2)


def menu():
	print('''
	Chose the Conversion:

	1. US Dollar - Euro
	2. Euro - US Dollar
	------
	3. US Dollar - British Pound
	4. British Pound - US Dollar
	------
	5. US Dollar - Canadian Dollar
	6. Canadian Dollar - US Dollar
	------
	7. US Dollar - Chines Yuan
	8. Chines Yuan - US Dollar
	------
	9. US Dollar - Peso Argentino
	10. Peso Argentino - US Dollar
	------
	11. US Dollar - Brazilian Real 
	12. Brazilian Real - US Dollar
	------
	13. US Dollar - Mexican Peso
	14. Mexican Peso - US Dollar

	0. Exit
	''')

	conversionChoices= {
						1:'USD-EUR', 
						2:'EUR-USD', 
						3:'USD-GBP', 
						4:'GBP-USD', 
						5:'USD-CAD', 
						6:'CAD-USD', 
						7:'USD-CNY', 
						8:'CNY-USD',
						9:'USD-ARS',
						10:'ARS-USD',
						11:'USD-BRL',
						12:'BRL-USD',
						13:'USD-MXN',
						14:'MXN-USD'
						}

	menuLimit = len(conversionChoices)

	selected = "Null"
	
	choice = raw_input("\t")

	checkChoice(choice, menuLimit)

	for number, exchange in conversionChoices.items():
		if number == int(choice):
			selected = exchange
	
	return selected



def main():
	selected = menu()

	mainCurrency = selected.replace("-", " ")[:3:] #strinp the "-" form the stirng and take only the first 3 characterts
	secondaryCurrency = selected.replace("-", " ")[4:3:] #strinp the "-" form the stirng and take only the last 3 characterts
	
	amount = raw_input('Curency Amount '+ '(' + str(mainCurrency) + ')' +': ')

	try: #check that the selection is a float or exit with error
		float(amount)
	except Exception: #Error
		errorTrap(1)
	else:
		amount = float(amount)

	#checkFile(file)

	#dict = create_exchange_dict()
	
	#for exchange,rate in dict.items():
	#	if exchange == selected:
	#		result = amount * float(rate)

	print secondaryCurrency

#Execution
main()




