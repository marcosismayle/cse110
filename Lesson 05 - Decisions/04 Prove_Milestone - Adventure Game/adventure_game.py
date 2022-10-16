print() # space in the top

# Variables with the stories.

first_scenario = 'You wake up but are still very tired after a long night\'s sleep. Blurred view. You can make out a silhouette of someone approaching. It\'s a Mage. He informs you that you have been chosen to help him on a great adventure and he needs your answer urgently. Do you ACCEPT or DECLINE the invitation? '

scenario_accept = 'The adventure will beggin' # temporary scenario

scenario_decline = 'You will return to home' # temporary scenario

# Print the first scenario and ask for an user input.
user_choice = input(f'{first_scenario}')

# While loop to accept only expected entries.
while user_choice.upper() not in('ACCEPT', 'DECLINE'):
  user_choice = input(
    f'''
        !!!Invalid entry!!!
     Try again.
     {first_scenario}''')
else:
    if user_choice.upper() == 'ACCEPT':
        #accept = input(f'{scenario_accept}')
        print(scenario_accept) #temporary output
    elif user_choice.upper() == 'DECLINE':
        #decline =  input(f'{scenario_decline}')
        print(scenario_decline) #temporary output

print('Under development')