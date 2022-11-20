"""
File: shopping_list.py
Author: Marcos Ismayle

Purpose: Practice working with list indexes.
"""

print()

shopping_list = []
item_name =''

print('Please enter the items of the shopping list (type: quit to finish):')

while item_name != 'quit':
    item_name = input('Item: ')
    
    if item_name != 'quit':
        shopping_list.append(item_name)

print()
print('The shopping list is:')
for item in shopping_list:
    print(item)
print()

print('The shopping list with indexes is:')
for i in range(len(shopping_list)):
    item_name = shopping_list[i]
    print(f"{i}. {item_name}")

print()

item_index = int(input('Which item would you like to change? '))
shopping_list[item_index] = input('What is the new item? ')

print()

print('The shopping list with indexes is:')
for i in range(len(shopping_list)):
    item_name = shopping_list[i]
    print(f"{i}. {item_name}")

print()