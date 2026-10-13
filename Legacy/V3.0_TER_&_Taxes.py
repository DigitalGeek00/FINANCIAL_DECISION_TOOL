import math

def financial_data_function():

    while True:
        try:
            initial_capital = float(input('Enter initial capital, without using dots: (E.g. 10000, 20000, etc): '))
        except ValueError: 
            print('Invalid value')
            continue
        if initial_capital < 0:
            print('Invalid value')
            print('Please, enter a value equal to or higher than 0.')
            continue
        else:
            break
    print('Perfect, continue.')
    input('Press ENTER to continue')

    while True:
        try:
            time = float(input('Enter years invested: '))
        except ValueError:
            print('Invalid value')
            continue
        if time < 0:
            print('Please, enter a value equal to or higher than 0.')
            continue
        else:
            break
    print('Perfect, continue.')
    input('Press ENTER to continue')

    while True:
        try:
            annual_rate = float(input('Enter annual rate, use int or float: (E.g. 2, 4, 2.3, etc): ')) / 100
        except ValueError:
            print('Invalid value')
            continue
        if annual_rate <= 0:
            print('Please, enter a value higher than 0.')
            continue
        else:
            break
    print(f"""Well done, your summary is:
        Initial capital = {initial_capital:g} €;
        Years invested: {time:g};
        The annual rate introduced is {annual_rate*100:g} %.
    """)
    input('Press ENTER to continue.')
    return initial_capital, time, annual_rate
def compound_interest(initial_capital, time, annual_rate):
    compound_final_capital = initial_capital * (1 + annual_rate) ** time
    compound_interests = compound_final_capital - initial_capital
    return compound_interests, compound_final_capital
def profit_function(compound_final_capital, initial_capital):
    profit = compound_final_capital - initial_capital
    return profit
def gross_return_function(profit, initial_capital):
    gross_return = (profit / initial_capital) * 100
    return gross_return

initial_capital, time, annual_rate = financial_data_function()
compound_interests, compound_final_capital = compound_interest(initial_capital, time, annual_rate)
profit = profit_function(compound_final_capital, initial_capital)
print(f'Profit gross on your investment is: {profit:g} €')
input('Press ENTER to continue.')

gross_return = gross_return_function(profit, initial_capital)
print(f'Gross return on your investment is: {gross_return:g} %')
input('Press ENTER to continue.')

def ter_function():    
    while True:
    
        try:
            ter = float(input('Please, enter ter value as a float: '))
            print(f'TER introduced is = {ter:g}')
        except ValueError:
            print('Invalid value')
            continue
        if ter <= 0:
            print('Please, enter a higher value than 0.')
            continue
        else:
            break
    ter = ter / 100
    return ter

ter = ter_function()
full_years = math.floor(time)
fractional_years = time - full_years
current_capital = initial_capital

for i in range(full_years):

    annual_return = current_capital * annual_rate
    current_capital += annual_return
    annual_ter = current_capital * ter
    current_capital -= annual_ter
    final_annual_return = annual_return - annual_ter

if fractional_years > 0:

    months = fractional_years * 12
    fractional_rate = annual_rate * (months / 12)
    fractional_return = current_capital * fractional_rate

    monthly_ter_rate = ter / 12
    fractional_ter_rate = months * monthly_ter_rate
    fractional_ter_return = current_capital * fractional_ter_rate

    final_fractional_return = fractional_return - fractional_ter_return
    current_capital += final_fractional_return

#Beneficio final después de comisiones:

def profit_ter_function(current_capital, initial_capital):
    profit_after_ter = current_capital - initial_capital
    return profit_after_ter

profit_after_ter = profit_ter_function(current_capital, initial_capital)
print(f'Profit after ter on your investment is: {profit_after_ter:g} €')
input('Press ENTER to continue.')

input("""For calculation purposes, a 19% tax rate is applied to investment profits. 

This is a general estimate and does not represent your actual tax liability. 

Please consider your applicable IRPF tax bracket and verify your final tax obligations externally.

Press ENTER to continue.""")

tax_rate = 0.19

def tax_amount_function(profit_after_ter, tax_rate):
    tax_amount = profit_after_ter * tax_rate
    final_profit = profit_after_ter - tax_amount
    return tax_amount, final_profit

tax_amount, final_profit = tax_amount_function(profit_after_ter, tax_rate)
print(f'Tax amount based on 19% are: {tax_amount:g} €')
input('Press ENTER to continue.')
print(f'Final profit is: {final_profit:g} €')
input('Press ENTER to continue.')
