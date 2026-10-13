def savings_capacity(income, expenses):

        total_savings_capacity = income - expenses

        return total_savings_capacity

def savings_rate(total_savings_capacity, income):

    total_savings_rate = (total_savings_capacity / income)*100

    return total_savings_rate

def non_invested_savings(total_savings_capacity, contributions):

    total_non_invested_savings = total_savings_capacity - contributions

    return total_non_invested_savings

input('Welcome, press ENTER to start: ')

income = float(input('Enter net income: '))

while income <= 0:
    print('Please, enter a higher value than 0.')
    income = float(input('New value: '))
        
print('Perfect')
input('Press ENTER to continue')

expenses = float(input('Enter monthly expenses: '))

while income <= expenses or expenses <= 0:
    print('Income must be higher than expenses')
    expenses = float(input('New value: '))
        
print('Perfect')

total_savings_capacity = (savings_capacity(income, expenses))

print(f'Your savings capacity is {total_savings_capacity} €')

input('Press ENTER to calculate savings rate depending on data offered')

total_savings_rate = savings_rate(total_savings_capacity, income)
print(f'Your savings rate is {total_savings_rate:.1f} %')

input('Press ENTER to calculate non-invested savings. First declare montlhly contributions:')

contributions = float(input('Enter monthly contributions: '))

while contributions <= 0 or contributions > total_savings_capacity:
        print('Please, enter a higher value than 0')
        contributions = float(input('New value: '))
        
print(f'Perfect, your monthly contributions are: {contributions} €')
input('Press ENTER to continue')

total_non_invested_savings = non_invested_savings(total_savings_capacity, contributions)

print(f'Your non-invested savings are {total_non_invested_savings} €')
