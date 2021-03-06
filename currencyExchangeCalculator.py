#!/usr/bin/python3
#Version 2.2
#Use Python 3.x 
#Written by Federico Paini federico[DOT]paini[AT]gmail[DOT]com
#Usage permitten without consent from the author.  
#Use this program on a "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied  

import sys, os, os.path, urllib.request, re, time, datetime, locale

#Variables
file = 'conv_rates.txt' 												#Text database file containing the exchange rates

locale.setlocale( locale.LC_ALL, '' )

#Procedures
def check_File(file): 													#Create currency exchange text database file containing the exchange rates
	
	if os.path.exists(file) == False or os.stat(file).st_size == 0:		#Check that the file exists and is not empty
		grab_Web_Rates()														
	if  time.time() - os.path.getmtime(file) > 86400: 					#Check that the file is no more than 24 hours old
		grab_Web_Rates()												#Grab the currency exchange data form the internet
	else: 
		return create_Exchange_Dictionary()								#The file is up to date, all good

def strip_Comma(amount): 												#strip commas from the amount to be converted									
	if ',' in amount:
		amount = ''.join(e for e in amount if e.isdigit() or e == '.')
	return amount

def format_Currency(value):												#format currency US style 
    return "{:,.2f}".format(value)

def create_Exchange_Dictionary(): 										#Create dictionary from the text database
	exchange_Rates_Dictionary = {}
	with open(file, 'r') as fileobj:
	  for line in fileobj:
	      exchange_Rates_Dictionary[line.split(",")[0]] = line.split(",")[1].rstrip()
	return exchange_Rates_Dictionary

def grab_Web_Rates():													#Grab the exchange rates from the web and saves it into the text database
	user_agent="Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0)"
	url="http://www.x-rates.com/table/?from=USD"
	conversion_rates = open (file, 'w+')
	request = urllib.request.Request(url, None, { 'User-Agent' : user_agent})
	web = urllib.request.urlopen(request)
	html = web.read().decode('utf-8')
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

	#Remove Duplicates
	lines = open(file, 'r').readlines()
	lines_set = set(lines)
	out  = open(file, 'w')

	for line in lines_set:
	    out.write(line)

def error_Trap(error_Code): 										#Error handling function
	copyright = u'\u00a9'

	if error_Code == 1:
		os.system('clear')
		print ("Error! Only numbers are allowed ! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit(1)
	
	elif error_Code == 2:
		os.system('clear')
		print ("Error! Selection out of Bounds! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit(1)

	elif error_Code == 3:
		os.system('clear')
		print ("Error! Exchange rate not found! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit(1)

	elif error_Code == 9:
		print ("Error! Something went wrong! \n")
		print ("Thanks for using Currency Calculator! \n")
		exit(1)

	elif error_Code == 10:
		os.system('clear')
		print ("Thanks for using Currency Calculator! \n\n" + copyright + "2018 Federico Paini \n")
		exit(0)

	else: #exit gracefully
		os.system('clear')
		print ("Thanks for using Currency Calculator! \n\n" + copyright + "2018 Federico Paini \n")
		exit(0)
	
	return 0

def check_Choice(choice):
	try: 															#Check that the selection is a digit or exit with error
		int(choice)
	except Exception: 												#Print an error message and quit
		error_Trap(1)

def check_Float(amount):
	try: 															#check that the selection is a float or exit with error
		float(amount)
	except Exception: 												#Print an error message and quit
		error_Trap(1)
	else:
		amount = float(amount)										#Convert to float

	return amount

def split_Currencies(selected):
	primary_Currency = selected.replace("-", " ")[:3:] 				#Strinp the "-" form the stirng and take only the first 3 characterts
	secondary_Currency = selected.replace("-", " ")[4::] 			#Strinp the "-" form the stirng and take only the last 3 characterts

	return primary_Currency, secondary_Currency

def menu():															#Main menu function. User to select the desired exchange rates
	os.system('clear') 												#Clear the terminal

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

	conversion_Choices= {
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

	menu_Limit = len(conversion_Choices)
	selected = "Null"
	choice = strip_Comma(input("\t"))

	check_Choice(choice)

	if int(choice) == 0:											#Check that the selection is a number
		error_Trap(10)
	elif int(choice) > menu_Limit:									#Check that the selection is whithin the menu limits
		error_Trap(2)

	for number, exchange in conversion_Choices.items(): 			#Get the selected currency exchange 
		if number == int(choice):
			selected = exchange
	
	return selected

def main():
	selected = menu()

	primary_Currency = split_Currencies(selected)[0]
	secondary_Currency = split_Currencies(selected)[1]
	
	amount = input('Curency Amount '+ '(' + str(primary_Currency) + ')' +': ') 	#Get to amount to be converted 
	amount = strip_Comma(amount)
	amount = check_Float(amount)

	check_File(file)															#Check that the databse file exists and is current
	dict = create_Exchange_Dictionary()											#Create exchange dictionary from text database
	
	for exchange,rate in dict.items():											#Get the exchange rate aand compute the calculation
		if exchange == selected:
			exchangeRate = rate

    #Unicode currency symbols 
	e = u'\u20ac' 	#Euro 
	b = u'\xA3'   	#British Pound 
	y = u'\u00a5' 	#Chinese Yuan 
	r = u'\u0052' 	#Brazilian Real 
	p = u'\u20b1' 	#Mexican Peso 
	yn = u'\u00a5'	#Japanese Yen 
	d = u'\u0024'	#Dollar 


	amount = float(amount)
	exchangeRate = float(exchangeRate)
	result = amount * exchangeRate												#Execute the currency conversion

	#Print out final results to terminal 
	os.system('clear') 															#Clear the terminal

	if primary_Currency == "USD":												#Display the result 
		print ("Your amount (USD): "+"${:,.2f}".format(amount))
	elif primary_Currency == "EUR":
		print ("Your Amount (EUR): "+ e +"{:,.2f}".format(amount))
	elif primary_Currency == "GBP":
		print ("Your Amount (GBP): "+ b +"{:,.2f}".format(amount))
	elif primary_Currency == "CAD":
		print ("Your Amount (CAD): "+"${:,.2f}".format(amount))
	elif primary_Currency == "MXN":
		print ("Your Amount (MXN): "+ p +"{:,.2f}".format(amount))
	elif primary_Currency == "ARS":
		print ("Your Amount (ARS): "+ "${:,.2f}".format(amount))
	elif primary_Currency == "CNY":
		print ("Your Amount (CNY): "+ y +"{:,.2f}".format(amount))
	elif primary_Currency == "BRL":
		print ("Your Amount (BRL): "+ r +"{:,.2f}".format(amount))
	else:
		print ("Your Amount: "+ "{:,.2f}".format(amount))

	#result = format_Currency(result)

	if secondary_Currency== "USD":
		print ("Your amount (USD): "+"${:,.2f}".format(result))
	elif secondary_Currency == "EUR":
		print ("Your Amount (EUR): "+ e +"{:,.2f}".format(result))
	elif secondary_Currency == "GBP":
		print ("Your Amount (GBP): "+ b +"{:,.2f}".format(result))
	elif secondary_Currency == "CAD":
		print ("Your Amount (CAD): "+"${:,.2f}".format(result))
	elif secondary_Currency == "MXN":
		print ("Your Amount (MXN): "+ p +"{:,.2f}".format(result))
	elif secondary_Currency == "ARS":
		print ("Your Amount (ARS): "+ "${:,.2f}".format(result))
	elif secondary_Currency == "CNY":
		print ("Your Amount (CNY): "+ y +"{:,.2f}".format(result))
	elif secondary_Currency == "BRL":
		print ("Your Amount (BRL): "+ r +"{:,.2f}".format(result))
	else:
		print ("Converts To: "+ "{:,.2f}".format(result))

	print("The conversion rate for %r and %r is: %8.2f" %(primary_Currency, secondary_Currency, exchangeRate))

	return 0

#Execution
main()