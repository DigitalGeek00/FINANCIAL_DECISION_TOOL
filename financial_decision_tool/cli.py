from calculations import (simple_interest, compound_interest, inv_analysis, evolution_function)

def menu():
    print("======================================== Financial Decision Tool - MENU ========================================")
    print("1. Interest of an investment")
    print("2. Investment analysis")
    print("3. Annual evolution of an investment")
    print("4. DCA (Dollar-Cost Averaging)")
    print("5. Investment comparator")        
    print("6. Exit")

def menu_int():
    print("\n--- Interest Type ---")
    print("0. Return to main menu")
    print("1. Simple interest")
    print("2. Compound interest")


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
                    initial_capital, time, annual_rate = usr_data()
                    interests_s, simple_f_c = simple_interest(initial_capital, time, annual_rate)
                    
                    print(f'\nUser selected "Simple interest":')
                    print(f'Simple interests generated over {time} years are: {interests_s:.2f} €')
                    print(f'This result shows the final capital you have: {simple_f_c:.2f} €')
                    input('\nPress ENTER to return to menu.')
                    break
                elif menu_interno == '2':
                    initial_capital, time, annual_rate = usr_data()
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
            initial_capital, time, annual_rate = usr_data()
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
        elif option == '3':
            print('User selected "Annual evolution of an investment":')
            initial_capital, time, annual_rate = usr_data()
            gross_return, current_capital, accumulated_return = evolution_function(initial_capital, time, annual_rate)
            
            print(f'Gross return: {gross_return:.2f} €')
            print(f'Final capital: {current_capital:.2f} € ') 
            print(f'Accumulated return: {accumulated_return:.2f} %')
            input('Press ENTER to return to menu.')

#Usr_data
def usr_data():
    initial_capital = float(input("Enter initial_capital: "))
    time = float(input("Enter time: "))
    annual_rate = float(input("Enter annual_rate: ")) / 100
    return initial_capital, time, annual_rate
def ter_value():
    ter = float(input("Enter TER value in basis points (bps): ")) / 10000
    return ter
def taxes_value():
    taxes = float(input("Enter TAXES value: ")) / 100
    return taxes

if __name__ == "__main__":
    run_cli()
