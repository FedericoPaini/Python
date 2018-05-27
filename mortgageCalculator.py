#!/usr/bin/python

__author__ = 'Federico'

# Must have data

property_value = 1000
percent_annual_interest = 4.9
mortgage_years = 1
percent_down = 20.0

#Derived data

pmi_breakeven = property_value * 0.2
money_down = property_value * (percent_down/100.0)
principal = property_value - money_down
loan_to_value = principal/property_value
payment_number = mortgage_years * 12

if percent_down < 20.0:
    pmi_required = True
else:
    pmi_required = False
    pmi_stop = 0

#functions
def format_currency(value):
    return "${:,.2f}".format(value)

def pmt(principal, percent_annual_interest, mortgage_years, payment_number):
    monthly_interest = percent_annual_interest/(100 * 12)
    monthly_payment = principal * ( monthly_interest / (1 - (1 + monthly_interest) ** (- payment_number)))
    return monthly_payment

def get_pmi_rate(loan_to_value, mortgage_years, pmi_required ):
    if pmi_required == False:
        return 0
    else:
        if mortgage_years < 25:
            if loan_to_value <= 0.85:
                pmi_rate = 0.0030
            elif loan_to_value <= 0.90 and loan_to_value > 0.85:
                pmi_rate = 0.0049
            elif loan_to_value <= 0.95 and loan_to_value > 0.90:
                pmi_rate = 0.0067
            elif loan_to_value <= 0.97 and loan_to_value > 0.95:
                pmi_rate = 0.0110
            else:
                pmi_rate = 0
        else:
            if loan_to_value <= 0.85:
                pmi_rate = 0.0035
            elif loan_to_value <= 0.90 and loan_to_value > 0.85:
                pmi_rate = 0.0054
            elif loan_to_value <= 0.95 and loan_to_value > 0.90:
                pmi_rate = 0.0072
            elif loan_to_value <= 0.97 and loan_to_value > 0.95:
                pmi_rate = 0.0115
            else:
                pmi_rate = 0

    return pmi_rate

def get_mortgage_schedule(pmi_required, property_value, percent_annual_interest, mortgage_years,
                          payment_number, pmi_rate, percent_down, pmt, pmi_breakeven):
    intr = 0
    intr_applied = 0
    money_down = property_value * (percent_down/100.0)
    starting_balance = property_value - money_down
    monthly_pmi_pmt = ( starting_balance * pmi_rate )/12
    total_pmi_paid = 0
    total_cost = 0
    pmi_stop = 0

    mortgage_payment_table = []

    for n in range(0, payment_number):
        entry = {}

        intr = ( starting_balance * ( percent_annual_interest / (12 * 100.0) ))
        intr_applied = pmt - intr
        end_balance = starting_balance - intr_applied

        entry['intr'] = intr
        entry['intr_applied'] = intr_applied
        entry['end_balance'] = end_balance

        while end_balance >= (property_value - pmi_breakeven):
            total_pmi_paid += monthly_pmi_pmt
            pmi_stop = n+2
            break

        entry['month'] = n + 1
        entry['starting_balance'] = starting_balance
        entry['pmt'] = pmt
        entry['monthly_pmi_pmt'] = monthly_pmi_pmt + pmt
        entry['intr_applied'] = intr_applied
        entry['intr'] = intr
        starting_balance = entry['end_balance']
        total_cost += pmt

        mortgage_payment_table.append(entry)

    return mortgage_payment_table

def get_total_cost(mortgage_payment_table):
    total_cost = 0.0
    lenght = len(mortgage_payment_table)
    for key in range(0, lenght):
        for k, v in mortgage_payment_table[key].items():
            if k == 'pmt':
                total_cost += v
    return total_cost
    
    
    
pmi_rate = get_pmi_rate(loan_to_value, mortgage_years, pmi_required)

pmt = pmt(principal, percent_annual_interest, mortgage_years, payment_number)

montly_pmi_pmt = ( principal * pmi_rate )/12
mortgage_months = mortgage_years * 12

#Mortgage schedule printout

print '====== Mortgage Schedule ======'
print
starting_balance = principal
total_pmi_paid = 0
total_cost = 0
months_array = []
starting_balance_array = []
pmt_array = []
montly_pmi_pmt_array = []
intr_applied_array = []
intr_array = []
end_balance_array = []

print("%4s | %13s | %13s | %13s | %13s | %13s | %13s" %
        ("#", "Start Bal.", "Payment", "Pmt with PMI", "Principal", "Interest", "End Bal"))

print("-" * 100)

for n in range(1, mortgage_months + 1):
    intr = starting_balance * (percent_annual_interest / (12 * 100.0) )
    intr_applied = pmt - intr
    end_balance = starting_balance - intr_applied

    while end_balance >= (property_value - pmi_breakeven):
        total_pmi_paid += montly_pmi_pmt
        pmi_stop = n+1
        break

    print("%4s | %13s | %13s | %13s | %13s | %13s | %13s" %
           (n, format_currency(starting_balance),
           format_currency(pmt),
           format_currency(montly_pmi_pmt + pmt),
           format_currency(intr_applied),
           format_currency(intr),
           format_currency(end_balance)))

    # Create arrays for Table payment

    months_array.append(n)
    starting_balance_array.append(starting_balance)
    pmt_array.append(pmt)
    montly_pmi_pmt_array.append(montly_pmi_pmt + pmt)
    intr_applied_array.append(intr_applied)
    intr_array.append(intr)
    end_balance_array.append(end_balance)

    starting_balance = end_balance
    total_cost += pmt

mortgage_payment_table = [months_array, starting_balance_array, pmt_array, montly_pmi_pmt_array,
                          intr_applied_array, intr_array, end_balance_array] #mortgage schedule table

#Variables Printouts

print "\n"
print '-------------- Mortgage Info-----------------'
print 'Principal', format_currency(principal)
print 'Money down: ', format_currency(money_down)
print 'PMI breakeven 20%: ', format_currency(pmi_breakeven - money_down)
print 'PMI Required: ', pmi_required
print 'Loan-to-Value ratio: ', loan_to_value
print 'PMI Rate: ', (pmi_rate * 100),'%'
print "----------------------------------------------\n"

print '--------------- Payment Info -----------------'
print 'Total cost of the loan', format_currency(total_cost)
print 'Total Intrest Paid', format_currency(n * pmt - principal)
print 'Annual Mortgage Payment: ', format_currency(pmt * 12)
print 'Annual PMI: ', format_currency(principal * pmi_rate)
print 'Montly mortgage Payment: ', format_currency (pmt)
print 'Montly PMI Payment: ', format_currency(montly_pmi_pmt)
print 'Monltly payment', format_currency(montly_pmi_pmt + pmt)
print 'PMI Stop Payment at year: ', round(pmi_stop / 12)
print "----------------------------------------------\n"

print mortgage_payment_table