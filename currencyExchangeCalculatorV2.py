#!/usr/bin/python
#Version 2.0
#Not yet compatible with Python 3.x 
#Written by Federico Paini federico.paini@gmail.com
#Usage permitten without consent from the author.  
#Use this program on a "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied  

import sys, os, os.path, urllib2, re, cookielib, time, datetime, locale

#Variables
file = 'conv_rates.txt' #Text database file containing the exchange rates

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
		return createExchangeDictionary()

def stripComma(amount): #Strips commas
	if ',' in amount:
		amount = ''.join(e for e in amount if e.isdigit() or e == '.')
	return amount

def formatCurrency(value):
    return "{:,.2f}".format(value)

def createExchangeDictionary(): #Create exchange dictionary
	exchangeRatesDictionary = {}
	with open(file, 'r') as fileobj:
	  for line in fileobj:
	      exchangeRatesDictionary[line.split(",")[0]] = line.split(",")[1].rstrip()
	return exchangeRatesDictionary

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
	copyright = u'\u00a9'

	if errorCode == 1:
		os.system('clear')
		print ("Error! Only numbers are allowed ! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit(1)
	
	elif errorCode == 2:
		os.system('clear')
		print ("Error! Selection out of Bounds! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit(1)

	elif errorCode == 3:
		os.system('clear')
		print ("Error! Exchange rate not found! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit(1)

	elif errorCode == 9:
		print ("Error! Something went wrong! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit(1)

	elif errorCode == 10:
		os.system('clear')
		print ("Thanks for using Currency Calculator! \n\n" + copyright + "2018 Federico Paini \n")
		exit(0)

	else: #exit gracefully
		os.system('clear')
		print ("Thanks for using Currency Calculator! \n\n" + copyright + "2018 Federico Paini \n")
		exit(0)
	
	return 0

def checkChoice(choice):
	try: #check that the selection is a digit or exit with error
		int(choice)
	except Exception: #Error
		errorTrap(1)

def checkFloat(amount):
	try: 							#check that the selection is a float or exit with error
		float(amount)
	except Exception: 				#Print an error message and quit
		errorTrap(1)
	else:
		amount = float(amount)		#convert to float

	return amount

def splitCurrencies(selected):
	primaryCurrency = selected.replace("-", " ")[:3:] 		#strinp the "-" form the stirng and take only the first 3 characterts
	secondaryCurrency = selected.replace("-", " ")[4::] 	#strinp the "-" form the stirng and take only the last 3 characterts

	return primaryCurrency, secondaryCurrency

def menu():
	os.system('clear') #Clear the terminal

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
	
	choice = stripComma(raw_input("\t"))

	checkChoice(choice)

	if int(choice) == 0:			#check that the selection is a number
		errorTrap(10)
	elif int(choice) > menuLimit:	#check that the selection is whithin the limits
		errorTrap(2)

	for number, exchange in conversionChoices.items(): #Get the selected currency exchange 
		if number == int(choice):
			selected = exchange
	
	return selected

def displayResults(primaryCurrency, secondaryCurrency, rate, amount):

	e = u'\u20ac' 	#Euro symbol
	b = u'\xA3'   	#British Pound symbol
	y = u'\u00a5' 	#Yuan symbol
	r = u'\u0052' 	#Real symbol
	p = u'\u20b1' 	#Peso symbol
	yn = u'\u00a5'	#Yen symbol
	d = u'\u0024'	#Dollar symbol

	result = float(amount) * float(rate) 

	os.system('clear') #Clear the terminal

	amount = formatCurrency(amount)

	if primaryCurrency == "USD":
		print ("Your amount (USD): "), d, amount
	elif primaryCurrency == "EUR":
		print ("Your amount (EUR): "), e, amount
	elif primaryCurrency == "GBP":
		print ("Your amount (GBP): "), b, amount
	elif primaryCurrency == "CAD":
		print ("Your amount (GBP): "), d, amount
	elif primaryCurrency == "MXN":
		print ("Your amount (MXN): "), p, amount
	elif primaryCurrency == "ARS":
		print ("Your amount (ARS): "), d, amount
	elif primaryCurrency == "CNY":
		print ("Your amount (CNY): "), y, amount
	elif primaryCurrency == "BRL":
		print ("Your amount (BRL): "), r, amount
	else:
		print ("Your amount: "), amount

	result = formatCurrency(result)

	if secondaryCurrency== "USD":
		print ("Coverts to (USD): "), d, result
	elif secondaryCurrency == "EUR":
		print ("Coverts to (EUR): "), e, result
	elif secondaryCurrency == "GBP":
		print ("Coverts to (GBP): "), b, result
	elif secondaryCurrency == "CAD":
		print ("Coverts to (GBP): "), d, result
	elif secondaryCurrency == "MXN":
		print ("Coverts to (MXN): "), p, result
	elif secondaryCurrency == "ARS":
		print ("Coverts to (ARS): "), d, result
	elif secondaryCurrency == "CNY":
		print ("Coverts to (CNY): "), y, result
	elif secondaryCurrency == "BRL":
		print ("Coverts to (BRL): "), r, result
	else:
		print ("Coverts to: "), result

	print("The conversion rate for " + primaryCurrency + "-" + secondaryCurrency + " is: "), rate

	return 0


def main():
	selected = menu()

	primaryCurrency = splitCurrencies(selected)[0]
	secondaryCurrency = splitCurrencies(selected)[1]
	
	amount = raw_input('Curency Amount '+ '(' + str(primaryCurrency) + ')' +': ') #Get to amount from the user terminal
	amount = stripComma(amount)
	amount = checkFloat(amount)

	checkFile(file)										#Check that the databse file exists and it's current
	dict = createExchangeDictionary()						#Create exchange dictionary from text database
	
	for exchange,rate in dict.items():					#Get the exchange rate aand compute the calculation
		if exchange == selected:
			exchangeRate = rate

	displayResults(primaryCurrency, secondaryCurrency, exchangeRate, amount)


#Execution
main()




