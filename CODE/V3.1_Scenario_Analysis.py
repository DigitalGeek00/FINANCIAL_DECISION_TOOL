import math

def common_data_function():

    while True:
            try:
                initial_capital = float(input('Enter initial capital, without using dots: (E.g. 10000, 20000, etc): '))
            except ValueError: 
                print('Invalid value')
                continue
            if initial_capital < 0:
                print("""Invalid value
                Please, enter a value equal to or higher than 0.""")
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
    print(f"""SUMMARY: Initial capital = {initial_capital:.2f} €;
            Years invested = {time:.2f}""")
    input('Press ENTER to continue')
    
    return initial_capital, time

def annual_rate_function():

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
    print(f""" 
              Annual rate introduced is {annual_rate*100:.2f} %
    """)
    input('Press ENTER to continue.')
    return annual_rate
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
def ter_function():    
    while True:
    
        try:
            ter = float(input('Please, enter TER value as a float: '))
            print(f'TER introduced is = {ter:.2f}')
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
def scenario_type_function():

    while True:
        print("""SELECT SCENARIO TYPE: 
                 1. AS INDIVIDUAL VALUES:
                 2. AS RANGE: """)

        scenario = input('Select an option: ')

        if scenario == '1':
            scenario_list = []
            while True:
                try:
                    value = float(input('Enter annual rate (0 to finish): ')) / 100
                except ValueError:
                    print('Incorrect value.') 
                    continue
                if value == 0:
                    break
                elif value > 0:
                    scenario_list.append(value)
            print(scenario_list)    
            return scenario_list

        elif scenario == '2':
            while True:
                try:
                    minimum_value = float(input('Enter minimum value: ')) / 100
                except ValueError:
                    print('Incorrect value.') 
                    continue
                if minimum_value >= 0:
                    break
                else:
                    print('Enter a valid value.')
                    continue
            while True:
                try:
                    maximum_value = float(input('Enter maximum value: ')) / 100
                except ValueError:
                    print('Incorrect value.') 
                    continue
                if maximum_value > minimum_value:
                    break
                else:
                    print('Enter a valid value')
                    continue

            while True:
                try:
                    step_value = float(input('Enter step freq. value (steps between range values): ')) / 100
                except ValueError:
                    print('Incorrect value.') 
                    continue
                if step_value > 0:
                    break
                else:
                    print('Enter a valid value')
                    continue

            scenario_list = []

            current_value = minimum_value

            while current_value <= maximum_value:
                scenario_list.append(current_value)
                current_value = current_value + step_value
            return scenario_list  
        
def scenario_analysis(initial_capital, time, scenario_list):

    options = scenario_list
    results = []

    for option in scenario_list:
        compound_final_capital = compound_interest(
            initial_capital, 
            time, 
            option
            )
        results.append(compound_final_capital)

    for i in range(len(options)):
        print(f"""For annual rate {options[i] * 100} % 
        result is {results[i][0]:.2f} gross profit 
        & {results[i][1]:.2f} final capital.""")

while True:

    print("======================================== FINANCIAL DECISION TOOL ========================================")
    print("1. Investment analysis (To calculate through compound interest, net profit of an investment).")
    print("""2. Scenario analysis 
    (Compare both or more annual rate scenarios for same capital and time invested. 
    Results are gross profit and final capital.)""")
    print("3. Exit (bye!)")

    option = input('Select an option: ')

    if option == '1':
        print('User selected "Investment analysis":')
        initial_capital, time = common_data_function()
        annual_rate = annual_rate_function()
        compound_interests, compound_final_capital = compound_interest(initial_capital, time, annual_rate)
        profit = profit_function(compound_final_capital, initial_capital)
        print(f'Profit gross on your investment is: {profit:.2f} €')
        input('Press ENTER to continue.')

        gross_return = gross_return_function(profit, initial_capital)
        print(f'Gross return on your investment is: {gross_return:.2f} %')
        input('Press ENTER to continue.')

        input("""TER are taxes associated to some investment vehicles as index funds.
                For our pourpose, minimum TER allowed is higher than 0.""")

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

        def profit_ter_function(current_capital, initial_capital):
            profit_after_ter = current_capital - initial_capital
            return profit_after_ter

        profit_after_ter = profit_ter_function(current_capital, initial_capital)
        print(f'Profit after ter on your investment is: {profit_after_ter:.2f} €')
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
        print(f'Tax amount based on 19% are: {tax_amount:.2f} €')
        input('Press ENTER to continue.')
        print(f'Final profit is: {final_profit:.2f} €')
        input('Press ENTER to continue.')
        
    elif option == '2':
        print('User selected "Scenario analysis":')
        initial_capital, time = common_data_function()
        scenario_list = scenario_type_function()
        scenario_analysis(initial_capital, time, scenario_list)
        
    elif option == '3':
        print('Thank you for using. Bye.')
        break
    else:
        print('Invalid character, please select an available option.')
