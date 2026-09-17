def financial_data():
    initial_capital = float(input('Enter initial capital: '))
    time_years = float(input('Enter time: '))
    annual_rate = float(input('Enter annual rate (as integer): ')) / 100
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

    for i in range(2):

        initial_capital, time_years, annual_rate = financial_data()
        compound_final_capital = compound_interest(initial_capital, time_years, annual_rate)
        results.append(compound_final_capital)

    print(f"""Results for case A are: {results[0]:g}€;
            Results for case B are: {results[1]:g}€""")

    while True:

        retry = input('Do you want to retry? 1 = YES; ELSE = NO: ')

        if retry == '1':
            print('Ok, retry:')
            break
        else:
            print('Program ended, goodbye!')
            break
