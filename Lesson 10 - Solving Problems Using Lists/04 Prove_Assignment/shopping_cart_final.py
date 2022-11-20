"""
File: list_of_numbers.py
Author: Marcos Ismayle

Purpose: Practice using lists of numbers.
"""
import os

action = 0
#2. Create a list that will store the names of the items in the shopping cart.
items = []
# Store prices as well as names.
prices = []

os.system('cls')
#1. Have menu system that repeats until the user chooses quit.

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
        #3. Complete the option to add the name of the item to the list.
        item_name = input('What item would you like to add? ')
        items.append(item_name)
        # Change the add functionality to also ask for and store the price of the item.
        item_price = float(input(f'What is the price of \'{item_name}\'? '))
        prices.append(item_price)
        print()
        print(f'{item_name.capitalize()} has been added to the cart.')
        input('Press enter to continue.')
        os.system('cls')
    elif action == 2:
        if items == []:
            # if the shopping cart is empty.
            print('Shopping cart is empty.')
            print()
        elif items != []:
            #4. Complete the option to display the names of the items in the list.
            print('The contents of the shopping cart are:')
            # Change the display functionality to also display the prices of the items.
            for i in range(len(items)):

                print(f"{i+1}. {items[i]} - $ {prices[i]:.2f}") # When displaying the items, display a number in front of each item. The numbers should start with 1.


        input('Press enter to return to main menu.')       
        os.system('cls')
    elif action == 3:
        if items == []:
            # if the shopping cart is empty.
            print('Shopping cart is empty.')
            print()
            input('Press enter to return to main menu.')
            os.system('cls')            
                   
        elif items != []:    
            print('The contents of the shopping cart are:')

            for i in range(len(items)):
                print(f"{i+1}. {items[i]} - $ {prices[i]:.2f}")
            print()
            # Complete the option to remove an item from the shopping cart.
            remove = int(input('Which item would you like to remove? '))
            remove-=1
            while remove >= len(items):
                print('Sorry, that is not a valid item number.')
                input('Press enter to try again.')
                
                remove = int(input('Which item would you like to remove? '))
                remove-=1 # The number the user enters should be converted to a 0-based index and checked to make sure it is within the bounds of the list.
            if remove <= len(items):
                # Both the item name and price are removed from their respective lists.
                items.pop(remove)
                prices.pop(remove)
                print('Item removed.')
                print()

                input('Press enter to return to main menu.')
                os.system('cls')
    elif action == 4:
        if items == []:
            # if the shopping cart is empty.
            print('Shopping cart is empty.')
            print()
            input('Press enter to return to main menu.')
            os.system('cls')
        elif items != []:
            # Complete the option to display the total amount of the prices of all the items in the shopping cart.
            sum = 0
            for price in prices:
                sum += price
            print(f'The total price of the items in the shopping cart is $ {sum:.2f}')
            print()
            input('Press enter to return to main menu.')       
            os.system('cls')
if action == 5:
    print()
    print('Thank you. Goodbye.')
    print()
