age = input('How old are you? ')
next_age = int(age) + 1
output = 'On your next birthday,you will be ' + str(next_age) + '.'
print(output)

print()

carton_qtt = input('How many egg cartons do you have? ')
total = 12 * int(carton_qtt)
print('You have ' + str(total) + ' eggs.')

print()

cookies = input('How many cookies do you have? ')
people = input('How many people are there? ')
result = float(cookies) / float(people)
print(f'Each person may have {result:,.2f} cookies.')