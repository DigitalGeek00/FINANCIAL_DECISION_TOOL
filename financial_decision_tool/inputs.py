from validations import (value_higher_zero, 
                         value_equal_high_zero)

def get_positive_number(prompt, error_message):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please, enter a valid number")
            continue
        if value_higher_zero(value):
            return value
        else:
            print(error_message)


#usr_data:
def usr_init_cap():
    return get_positive_number(
        "Enter initial capital: ", 
        "Capital must be greater than 0"
    )

def usr_time():
    return get_positive_number(
        "Enter time: ", 
        "Time must be greater than 0"
    )
def usr_annual_rate():
    return get_positive_number(
        "Enter annual rate (%): ", 
        "Annual rate must be greater than 0"
    ) / 100

def ter_value():
    while True:
        try:
            ter = float(input("Enter TER value in basis points (bps): ")) / 10000
        except ValueError:
            print("Please, enter a valid number")
            continue
        if value_equal_high_zero(ter):
            return ter
        else:
            print("Ter must be equal or higher zero")
            continue

# Assumption: taxable investments incur taxes upon sale.
def taxes_value():
    return get_positive_number(
        "Enter taxes: ", 
        "Taxes must be greater than 0"
    ) / 100

def contribution_value():
    return get_positive_number(
        "Enter contribution: ", 
        "Contribution must be greater than 0"
    )

def scenario_list():
    rates = []
    while True:
        try:
            value = float(input("Enter annual rates (0 to finish): "))
        except ValueError:
            print("Please, enter a valid number")
            continue
        if value == 0:
            break
        elif value < 0:
            print("Annual rate must be greater than 0")
            continue

        rates.append(value / 100)
        
    return rates
