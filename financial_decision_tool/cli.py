from calculations import (usr_init_cap, usr_time, usr_annual_rate, ter_value, taxes_value,
                          contribution_value, simple_interest, compound_interest, inv_analysis, 
                          evolution_function, calculate_dca, comparator, scenario_list, scenario_analysis)

def menu():
    print("======================================== Financial Decision Tool - MENU ========================================")
    print("1. Interest of an investment (Simple/Compound)")
    print("2. Investment analysis")
    print("3. Annual evolution of an investment")
    print("4. DCA (Dollar-Cost Averaging)")
    print("5. Investment comparator (A-B / Different returns)")        
    print("6. Exit")

def menu_int():
    print("\n--- Interest Type ---")
    print("0. Return to main menu")
    print("1. Simple interest")
    print("2. Compound interest")

def menu_int2():
    print("\n--- Investment Comparator ---")
    print("0. Return to main menu")
    print("1. Case A-B")
    print("2. Different returns")

def run_cli():
    while True:
        menu()
        option = input("Select an option: ").strip()

        if option == '1':
            print('User selected "Interest of an investment".')
            while True:
                menu_int()
                menu_interno = input("Select an option: ").strip()

                if menu_interno == '0':
                    print("Returning to main menu...")
                    break

                elif menu_interno == '1':
                    initial_capital = usr_init_cap()
                    time = usr_time()
                    annual_rate = usr_annual_rate()
                    interests_s, simple_f_c = simple_interest(initial_capital, time, annual_rate)
                    
                    print(f'\nUser selected "Simple interest":')
                    print(f'Simple interests generated over {time} years are: {interests_s:.2f} €')
                    print(f'This result shows the final capital you have: {simple_f_c:.2f} €')
                    input('\nPress ENTER to return to menu.')
                    break
                elif menu_interno == '2':
                    initial_capital = usr_init_cap()
                    time = usr_time()
                    annual_rate = usr_annual_rate()
                    compound_f_c, interests_c = compound_interest(initial_capital, time, annual_rate)
                    print(f'\nUser selected "Compound interest":')
                    print(f'Compound interests generated over {time} years are: {interests_c:.2f} €')
                    print(f'This result shows the final capital you have: {compound_f_c:.2f} €')
                    input('\nPress ENTER to return to menu.')
                    break
                else:
                    print("Invalid option, try again.")

        elif option == '2':
            print('User selected "Investment analysis":')
            initial_capital = usr_init_cap()
            time = usr_time()
            annual_rate = usr_annual_rate()
            ter = ter_value()
            taxes = taxes_value()
            tax_rate, current_ter, tax_amount, compound_f_c, profit, final_profit, ter_total_effect = inv_analysis(initial_capital, time, annual_rate, ter, taxes)
            
            print(f"""SUMMARY:
                    Initial capital = {initial_capital:.2f} €
                    Time = {time} years
                    Annual rate = {annual_rate * 100:.2f} %
                    TER = {ter * 100:.2f} %;
                    Taxes applied = {tax_rate * 100:.2f} %

                    ACCUMULATED TER FEES = {current_ter:.2f} €
                    TOTAL IMPACT OF TER ON FINAL CAPITAL = {ter_total_effect:.2f} €
                    FINAL NOMINAL TAXES APPLIED = {tax_amount:.2f} €
                    FINAL GROSS CAPITAL = {compound_f_c:.2f} €
                    FINAL GROSS PROFIT = {profit:.2f} €
                    FINAL NET PROFIT = {final_profit:.2f} €
                    FINAL NET CAPITAL = {initial_capital + final_profit:.2f} €

                    """)
            input('Press ENTER to return to menu.')
        elif option == '3':
            print('User selected "Annual evolution of an investment":')
            initial_capital = usr_init_cap()
            time = usr_time()
            annual_rate = usr_annual_rate()
            gross_return, current_capital, accumulated_return = evolution_function(initial_capital, time, annual_rate)
            
            print(f'Gross return: {gross_return:.2f} €')
            print(f'Final capital: {current_capital:.2f} € ') 
            print(f'Accumulated return: {accumulated_return:.2f} %')
            input('Press ENTER to return to menu.')
        elif option == '4':
            print('User selected "DCA (Dollar-Cost Averaging)":')
            initial_capital = usr_init_cap()
            time = usr_time()
            annual_rate = usr_annual_rate()
            contribution = contribution_value()
            total_contribution, initial_capital_growth, contribution_growth, final_capital, investment_return, roi = calculate_dca(initial_capital, contribution, time, annual_rate)

            print(f"""
            Initial capital growth is: {initial_capital_growth:.2f}
            Contribution growth is: {contribution_growth:.2f}
            Return on investment is: {investment_return:.2f}
            """)
        
            print(f'This is the total capital aported: {total_contribution:.2f} €')
            print(f'This is the investment final capital: {final_capital:.2f} €')
            print(f'This is your investment return: {investment_return:.2f} €')
            print(f"Return on invested capital: {roi:.2f}%")
            input('Press ENTER to return menu.')
        elif option == '5':
            while True:
                menu_int2()
                menu_interno = input("Select an option: ").strip()
            
                if menu_interno == '0':
                    print("Returning to main menu...")
                    break
            
                elif menu_interno == '1':
                    print('User selected "Case A-B":')

                    i_capital, t_years, a_rate, results = comparator()   

                    print(f"""Summary:
                    CASE A:
                    Initial capital = {i_capital[0]:.2f} €
                    Time = {t_years[0]:.2f} years
                    Annual rate = {a_rate[0] * 100:.2f} %
                    Gross profit: {(results[0] - i_capital[0]):.2f} €

                    CASE B:
                    Initial capital = {i_capital[1]:.2f} €
                    Time = {t_years[1]:.2f} years
                    Annual rate = {a_rate[1] * 100:.2f} %
                    Gross profit: {(results[1] - i_capital[1]):.2f} €
                    
                    Final capital for case A: {results[0]:.2f}€
                    Final capital case B: {results[1]:.2f}€
                    """)  
                    
                    break
                elif menu_interno == '2':
                    print('User selected "Different returns":')
                    initial_capital = usr_init_cap()
                    time = usr_time()
                    rates = scenario_list()
                    results = scenario_analysis(initial_capital, time, rates)

                    for rate, result in zip(rates, results):
                        compound_f_c, interests_c = result
                        print(f"""
                        For annual rate {rate * 100:.2f}%
                        Gross profit: {interests_c:.2f} €
                        Final capital: {compound_f_c:.2f} €
                        """)
                else:
                    print("Invalid option, try again.")

        elif option == '6':
            print("Thanks for using!")
            break


if __name__ == "__main__":
    run_cli()
