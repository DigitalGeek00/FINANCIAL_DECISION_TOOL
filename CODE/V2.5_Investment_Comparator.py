def financial_data():

    while True:
        try:
            initial_capital = float(input('Enter initial capital: '))
        except ValueError:
            print('Invalid value')
            continue         
        if initial_capital < 0:
            print('Invalid value')
            print('Please enter a value equal or higher than 0')
            continue
        else:
            break
    print('Perfect, continue.')
    input('Press ENTER to continue')

    while True:
        try:
            time_years = float(input('Enter time: '))
        except ValueError:
            print('Invalid value.')
            continue
        if time_years <= 0:
            print('Invalid value.')
            continue
        else:
            break
    print('Perfect, continue.')
    input('Press ENTER to continue')

    while True:
        try:  
            annual_rate = float(input('Enter annual rate (as integer, program will convert value): ')) / 100
        except ValueError:
            print('Invalid value.')
            continue
        if annual_rate <= 0:
            print('Invalid value.')
            continue
        else:
            break
    print('Perfect, continue.')
    input('Press ENTER to continue')
    return initial_capital, time_years, annual_rate

def compound_interest(initial_capital, time_years, annual_rate):
    compound_final_capital = initial_capital * (1 + annual_rate) ** time_years
    return compound_final_capital

retry = '1'
while retry == '1':

    input("""=====================================================================================
        WELCOME TO INVESTMENT COMPARATOR. INTRODUCE VALUES FOR BOTH CASES.
        Press Enter to continue:
=====================================================================================""")

    results = []
    i_capital = []
    t_years = []
    a_rate = []

    for i in range(2):

        initial_capital, time_years, annual_rate = financial_data()
        i_capital.append(initial_capital)
        t_years.append(time_years)
        a_rate.append(annual_rate)
        compound_final_capital = compound_interest(initial_capital, time_years, annual_rate)
        results.append(compound_final_capital)

    print(f"""Summary:
    CASE A:
    Initial capital = {i_capital[0]:g} €;
    Time = {t_years[0]:g} years;
    Annual rate = {a_rate[0]:g} %.

    CASE B:
    Initial capital = {i_capital[1]:g} €;
    Time = {t_years[1]:g} years;
    Annual rate = {a_rate[1]:g} %.
     
    Results for case A are: {results[0]:g}€;
    Results for case B are: {results[1]:g}€""")

    while True:

        retry = input('Do you want to retry? 1 = YES; ELSE = NO: ')

        if retry == '1':
            print('Ok, retry:')
            break
        else:
            print('Program ended, goodbye!')
            break
