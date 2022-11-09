"""
File: list_of_numbers.py
Author: Marcos Ismayle

Purpose: Practice using lists of numbers.
"""

numbers = []
number_input = 1
print()
print('Enter a list of numbers, type 0 when finished. ')
print()
while number_input != 0:
    number_input = int(input('Enter number: '))
    numbers.append(number_input)

print()
sum = 0
for number in numbers[:-1]:
    sum += number

average = sum / len(numbers[:-1])
print(f'The sum is: {sum}')
print(f'The average is: {average}')
print(f'The largest number is: {max(numbers)}')
print()