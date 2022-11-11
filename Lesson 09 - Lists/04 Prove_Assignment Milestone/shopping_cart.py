"""
File: list_of_numbers.py
Author: Marcos Ismayle

Purpose: Practice using lists of numbers.
"""
import os

action = 0
items = []

os.system('cls')
while action != 5:
    action = int(input(f'''
Welcome to the Shopping Cart Program!

    Please select one of the following: 
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit

Please enter an action: '''))
    print()
    if action == 1:
        item_name = input('What item would you like to add? ')
        items.append(item_name)
        print()
        print(f'{item_name.upper()} has been added to the cart.')
        input('Press enter to continue.')
        os.system('cls')
    elif action == 2:
        os.system('cls')
        print('The contents of the shopping cart are:')

        for item in items:
            print(item)

        input('Press enter to return to main menu.')       
        os.system('cls')
os.system('cls')
print()
print('Thank you. Goodbye.')
print()