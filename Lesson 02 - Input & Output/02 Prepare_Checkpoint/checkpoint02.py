first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

output = 'Your name is {1}, {0} {1}.' .format(first_name.capitalize(), last_name.capitalize())
print(output)