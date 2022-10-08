
print() #give a space

# Ask the user for the price of a child and an adult meal and
# store these values properly into variables as floating point numbers.
child_meal = float(input('What is the price of a child\'s meal? '))
adult_meal = float(input('What is the price of an adult\'s meal? '))

# Ask the user for the number of adults and children and
# store these values properly into variables as integers.
child_qtt = int(input('How many children are there? '))
adult_qtt = int(input('How many adults are there? '))

# Ask the user for the sales tax rate and store the value properly
# as a floating point number.
tax_rate = float(input('What is the sales tax rate? '))

# Compute and display the subtotal.
subtotal = (child_meal * child_qtt) + (adult_meal * adult_qtt)
print() #give a space

print(f'Subtotal: ${subtotal:.2f}')

# Compute and display the sales tax.
sales_tax = subtotal * (tax_rate / 100)

print(f'Sales tax: ${sales_tax:.2f}')

# Compute and display the total.
total = subtotal + sales_tax

print(f'Total: ${total:.2f}')
print() #give a space

# Ask the user for the payment amount and store the value
# properly as a floating point number.
payment_amount = float(input('What is the payment amount? '))

# Compute and display the change.
# Extra:
# It was set an while loop to ask the user for a payment amount until
# payment is equal or greater than total.

while payment_amount <= total:
  payment_amount = float(input(
    f'''
        !!!ALERT!!!
     Insufficient value.
     It's missing ${(total - payment_amount):.2f}.

What is the payment amount? '''))
else:
    print(f'Change: ${(payment_amount - total):.2f}')
print()
