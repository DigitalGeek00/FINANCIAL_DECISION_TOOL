import math

def financial_data():

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
        if time < 1:
            print('Please, enter a value equal to or higher than 1.')
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
        The annual rate introduced is {annual_rate*100:.2f} %.
    """)
    input('Press ENTER to continue.')
    return initial_capital, time, annual_rate

def simple_interest(initial_capital, time, annual_rate):
    simple_interests = initial_capital * time * annual_rate
    simple_final_capital = initial_capital + simple_interests
    return simple_interests, simple_final_capital

def compound_interest(initial_capital, time, annual_rate):
    compound_final_capital = initial_capital * (1 + annual_rate) ** time
    compound_interests = compound_final_capital - initial_capital
    return compound_interests, compound_final_capital

def calculate_dca(initial_capital, monthly_contribution, time, annual_rate):
    time_months = math.floor(time * 12 + 0.5)
    monthly_rate = ((1 + annual_rate) ** (1 / 12)) - 1
    total_contribution = initial_capital + (monthly_contribution * time_months)
    initial_capital_growth = (
        initial_capital * (1 + monthly_rate) ** time_months
    ) - initial_capital
    contribution_growth = monthly_contribution * (
        ((1 + monthly_rate) ** time_months - 1)
        / monthly_rate
    ) - (monthly_contribution * time_months)
    final_capital = (
        total_contribution
        + initial_capital_growth
        + contribution_growth
    )
    investment_return = final_capital - total_contribution
    return (
        total_contribution, 
        initial_capital_growth, 
        contribution_growth, 
        final_capital, 
        investment_return
    )

while True:
    print('==============================')
    print('WELCOME TO FINANCE CALCULATOR TOOL: ')
    print('==============================')
    print('1. Simple interest')
    print('2. Compound interest')
    print('3. DCA Strategy')
    print('4. Exit')

    option = input('Select an option: ')

    if option == '1':
        print('User selected simple interest')
        initial_capital, time, annual_rate = financial_data()
        simple_interests, simple_final_capital = simple_interest(initial_capital, time, annual_rate)
        print(f'Simple interests generated over {time} years are: {simple_interests:.2f} €')
        input('Press ENTER to know your final capital.')
        print(f'This result shows the final capital you have: {simple_final_capital:.2f} €')
        input('Press ENTER to return menu.')

    elif option == '2':
        print('User selected compound interest')
        initial_capital, time, annual_rate = financial_data()
        compound_interests, compound_final_capital = compound_interest(initial_capital, time, annual_rate)
        print(f'Compound interests generated over {time} years are: {compound_interests:.2f} €')
        input('Press ENTER to see final capital.')
        print(f'This result shows the final capital you have: {compound_final_capital:.2f} €')
        input('Press ENTER to return menu.')

    elif option == '3':
        print('User selected DCA Strategy')
        initial_capital, time, annual_rate = financial_data()
        while True:
            try:
                monthly_contribution = float(input('Enter monthly contributions without using dots (E.g. 100, 200,...): '))
            except ValueError:
                print('Invalid value')
                continue
            if monthly_contribution <= 0:
                print('Please, enter a higher value than 0.')
                continue
            else:
                break
        total_contribution, initial_capital_growth, contribution_growth, final_capital, investment_return = calculate_dca(initial_capital, monthly_contribution, time, annual_rate)
        print(f"""
            Initial capital growth is: {initial_capital_growth:g}
            Contribution growth is: {contribution_growth:g}
            Return on investment is: {investment_return:g}
        """)
        
        print(f'This is the total capital aported: {total_contribution:g} €')
        input('Press ENTER to continue.')
        print(f'This is the investment final capital: {final_capital:g} €')
        input('Press ENTER to continue.')
        print(f'This is your investment return: {investment_return:g} €')
        input('Press ENTER to return menu.')

    elif option == '4':
        print('See you soon!')
        break

    else:
        print('Option not available now.')
