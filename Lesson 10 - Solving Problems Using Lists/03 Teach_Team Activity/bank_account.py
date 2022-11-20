"""
File: bank_account.py
Author: Marcos Ismayle

Purpose: Track bank accounts and the balances in each one.
"""

accounts_names = []
balances = []
account_name = ''
current_balance = 0

print()
print('Enter the names and balances of bank accounts (type: quit when done)')
while account_name != 'quit':
    account_name = input('What is the name of this account? ')
    
    
    if account_name != 'quit':
        current_balance = float(input('What is the balance? '))
        accounts_names.append(account_name)
        balances.append(current_balance)

print()
print('Account Information:')
for i in range(len(accounts_names)):
    account_name = accounts_names[i]
    current_balance = balances[i]
    print(f"{account_name} - $ {current_balance:.2f}")

print()
total = 0
for balance in balances:
    if account_name != 'quit':
        total += balance

        average = total / len(balances)

print(f'Total: $ {total:.2f}')
print(f'Average: $ {average:.2f}')
print()