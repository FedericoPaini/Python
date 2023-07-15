#!/usr/bin/python
#Version 3.0
#Use Python 3.x 
#Written by Federico Paini 2015-2023 federico[DOT]paini[AT]gmail[DOT]com
#Usage permitten without consent from the author.  
#Use this program on a "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied 

import urllib.request, os, os.path, re, platform

file = 'conv_rates.txt'  # Text database file containing the exchange rates

# Unicode currency symbols
#e = u'\u20ac'   # Euro
#b = u'\xA3'     # British Pound
#y = u'\u00a5'   # Chinese Yuan
#br = u'\u0052'   # Brazilian Real
#mx = u'\u20b1'   # Mexican Peso
#yn = u'\u00a5'  # Japanese Yen
#d = u'\u0024'   # Dollar

def strip_comma(amount):
    if ',' in amount:
        amount = ''.join(e for e in amount if e.isdigit() or e == '.')
    return amount

def clear_screen():
    system = platform.system()
    if system == "Windows":
        return os.system('cls')
    elif system == "Linux":
        return os.system('clear')
    else:
        return os.system('clear')

def exchange_dictionary():
    exchange_dictionary = {}
    with open(file, 'r') as fileobj:
        for line in fileobj:
            exchange_dictionary[line.split(",")[0]] = line.split(",")[1].rstrip()
    return exchange_dictionary

def grab_rates():
    user_agent = "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0)"
    url = "http://www.x-rates.com/table/?from=USD"
    with urllib.request.urlopen(urllib.request.Request(url, None, {'User-Agent': user_agent})) as web:
        html = web.read().decode('utf-8')

    titles = re.findall(r'\?from=(.*?)</td>', html)[:100]

    with open(file, 'w+') as conversion_rates:
        for title in titles:
            title = title.replace("amp;to=", "").replace("&", "-").replace("'>", ",").replace("</a>", " ").replace("  ", "").rstrip()
            conversion_rates.write(f"{title}\n")

    # Remove duplicates
    with open(file, 'r') as f:
        lines = f.readlines()
        lines_set = set(lines)

    with open(file, 'w') as f:
        for line in lines_set:
            f.write(line)

def split_currencies(selected):
    primary = selected.replace("-", " ")[:3]
    secondary = selected.replace("-", " ")[4:]
    return primary, secondary

def check_float(amount):
    try:
        amount = float(amount)
    except ValueError:
        error_trap(1)
    return amount

def display_menu():
    print('''
    Choose the Conversion:

    1. US Dollar - Euro
    2. Euro - US Dollar
    ------
    3. US Dollar - British Pound
    4. British Pound - US Dollar
    ------
    5. US Dollar - Canadian Dollar
    6. Canadian Dollar - US Dollar
    ------
    7. US Dollar - Chinese Yuan
    8. Chinese Yuan - US Dollar
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

def get_user_choice():
    conversion_choices = {
        1: 'USD-EUR',
        2: 'EUR-USD',
        3: 'USD-GBP',
        4: 'GBP-USD',
        5: 'USD-CAD',
        6: 'CAD-USD',
        7: 'USD-CNY',
        8: 'CNY-USD',
        9: 'USD-ARS',
        10: 'ARS-USD',
        11: 'USD-BRL',
        12: 'BRL-USD',
        13: 'USD-MXN',
        14: 'MXN-USD'
    }

    while True:
        choice = input("Enter your choice (1-14): ")
        if choice.isdigit() and int(choice) in conversion_choices:
            selected = conversion_choices[int(choice)].split("-")
            return selected[0], selected[1], '-'.join(selected)
        else:
            print("Invalid selection. Please enter a number from 1 to 14.")

def error_trap(error_code):
    match error_code:
        case 1:
            clear_screen()
            print("Error! Only numbers are allowed!\n")
            print("Thanks for using Currency Calculator!\n")
            exit(1)
        case 2:
            clear_screen()
            print("Error! Selection out of Bounds!\n")
            print("Thanks for using Currency Calculator!\n")
            exit(1)
        case 3:
            clear_screen()
            print("Error! Exchange rate not found!\n")
            print("Thanks for using Currency Calculator!\n")
            exit(1)
        case 9:
            clear_screen()
            print("Error! Something went wrong!\n")
            print("Thanks for using Currency Calculator!\n")
            exit(1)
        case _:
            clear_screen()
            print("Thanks for using Currency Calculator!\n\n" + copyright + "2015-2023 Federico Paini\n")
            exit(0)

# Execution
display_menu()
primary_currency, secondary_currency, exchange = get_user_choice()

amount = input('Currency Amount ' + '(' + str(primary_currency) + ')' + ': ')
amount = strip_comma(amount)
amount = check_float(amount)
# check_File(file)  # File checking is commented out as it is not implemented in the code
dictionary = exchange_dictionary()

for conversion, rate in dictionary.items():
    if conversion == exchange:
        exchange_rate = rate

amount = float(amount)
exchange_rate = float(exchange_rate)
result = amount * exchange_rate

# Print out final results to terminal
clear_screen()
match primary_currency:
    case "USD":
        print("Your amount (USD): " + "${:,.2f}".format(amount))
    case "EUR":
        print("Your Amount (EUR): " + "{:,.2f}".format(amount))
    case "GBP":
        print("Your Amount (GPB): " + "{:,.2f}".format(amount))
    case "CAD":
        print("Your Amount (CAD): " + "{:,.2f}".format(amount))
    case "MEX":
        print("Your Amount (MEX): " + "{:,.2f}".format(amount))
    case "ARS":
        print("Your Amount (ARS): " + "{:,.2f}".format(amount))
    case "CNY":
        print("Your Amount (CNY): " + "{:,.2f}".format(amount))
    case "BRL":
        print("Your Amount (BRL): " + "{:,.2f}".format(amount))
    case _:
        print("Converts To: " + "{:,.2f}".format(amount))

match secondary_currency:
    case "USD":
        print("Your amount (USD): " + "${:,.2f}".format(result))
    case "EUR":
        print("Your Amount (EUR): " + "{:,.2f}".format(result))
    case "GBP":
        print("Your Amount (GPB): " + "{:,.2f}".format(result))
    case "CAD":
        print("Your Amount (CAD): " + "{:,.2f}".format(result))
    case "MEX":
        print("Your Amount (MEX): " + "{:,.2f}".format(result))
    case "ARS":
        print("Your Amount (ARS): " + "{:,.2f}".format(result))
    case "CNY":
        print("Your Amount (CNY): " + "{:,.2f}".format(result))
    case "BRL":
        print("Your Amount (BRL): " + "{:,.2f}".format(result))
    case _:
        print("Converts To: " + "{:,.2f}".format(result))

print("The conversion rate for %r and %r is: %8.5f" % (primary_currency, secondary_currency, exchange_rate))
