import os
import time
import sys

def print_style(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    return ''


#print() # space in the top

# Complete Game
# Variables with the stories.

# Level 1 - one possible scenario
scenario_1st = '''

You wake up but you are feeling very tired. Your eyes are blurred.
But you can see a silhouette of someone besides your bed. It is a Mage.
He says to you that you have been chosen to help him on a great adventure.
Do you ACCEPT or DECLINE the invitation? '''

# Level 2 - two possible scenarios

scenario_2nd = '''

The adventure will begin. You are not in your bedroom anymore. Seems like you
are in a forest. You have a bag with you with some stuff inside of it.
You open it and there are some useful objects.
Did you catch a FLASHLIGHT or your MOBILE? '''
scenario_3rd = '''

Oh no! The Mage really needs your help. But it is ok.
You will return to bed and wake up as if nothing has happened at night.

'''

# Level 3 - two possible scenarios

scenario_4th = '''

Now it is better. You can see a tight path ahead with leafy trees along,
looking older than the earth itself. And the Mage is looking unto you when
suddenly a very loud noise comes from the forest.
Do you SCREAM in terror or SHINE in the direction of the sound to find out what is going on? '''
scenario_5th = '''

You think it is so strange your bag is with you prepared for the trip.
You do not remember when you pick it up in your bedroom. But you are happy
to have your mobile with you.
Do you turn on the MOBILE flashlight or make a CALL for your mom to say you are ok
or you start to LOOK a picture from a very important person in your life? '''

# Level 4 - four possible scenarios
scenario_6th = '''

The Mage comes to you and says: “Be quiet, do not be afraid. Let us go out of here,
it is dangerous being outside at night.” '''
scenario_7th = '''

In the middle of the trees, you can see two small glowing circles coming in your direction.
“We have to go, NOW!” says the Mage. '''
scenario_8th = '''

You do not know why your mobile is here, but maybe some resources may be useful like
the flashlight. Now you can see that you do not have signal to make a call or to use the internet.
“Where I am?” you think. '''
scenario_9th = '''

It was not a good idea. There is no signal. You are not able to communicate
with someone using your phone.
“Where I am?” you think. '''

scenario_10th = '''

You are thinking when you will return and see this person again. You do not know.
'''

os.system('cls')
input(
'''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░╔╗╔╗╔╗░░╔╗░░░░░░░░░░░░░░╔╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░║║║║║║░░║║░░░░░░░░░░░░░╔╝╚╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░║║║║║╠══╣║╔══╦══╦╗╔╦══╗╚╗╔╬══╦╗░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░║╚╝╚╝║║═╣║║╔═╣╔╗║╚╝║║═╣░║║║╔╗╠╝░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░╚╗╔╗╔╣║═╣╚╣╚═╣╚╝║║║║║═╣░║╚╣╚╝╠╗░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╚╝╚╝╚══╩═╩══╩══╩╩╩╩══╝░╚═╩══╩╝░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░╔═══╗░╔╗░░░░░░░░╔╗░░░░░░░░░╔═══╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░║╔═╗║░║║░░░░░░░╔╝╚╗░░░░░░░░║╔═╗║░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░║║░║╠═╝╠╗╔╦══╦═╬╗╔╬╗╔╦═╦══╗║║░╚╬══╦╗╔╦══╗░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░║╚═╝║╔╗║╚╝║║═╣╔╗╣║║║║║╔╣║═╣║║╔═╣╔╗║╚╝║║═╣░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░║╔═╗║╚╝╠╗╔╣║═╣║║║╚╣╚╝║║║║═╣║╚╩═║╔╗║║║║║═╣░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░╚╝░╚╩══╝╚╝╚══╩╝╚╩═╩══╩╝╚══╝╚═══╩╝╚╩╩╩╩══╝░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░┌─┐░░░┌─┬─┐┌─┐░░┌┐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│┼├┬┬─┤─┤─┤│┬┼─┬┤└┬─┬┬┐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│┌┤┌┤┴┼─├─││┴┤│││┌┤┴┤┌┘░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░└┘└┘└─┴─┴─┘└─┴┴─┴─┴─┴┘░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')

os.system('cls')
user_choice = input(print_style(scenario_1st))

while user_choice.upper() not in('ACCEPT', 'DECLINE'):
  
  os.system('cls')
  user_choice = input(print_style(
    f'''
        !!!Invalid entry!!!
     Try again.
        {scenario_1st}'''))
else:
    if user_choice.upper() == 'ACCEPT':

        os.system('cls')
        user_choice = input(print_style(scenario_2nd))

        while user_choice.upper() not in('FLASHLIGHT', 'MOBILE'):
            
            os.system('cls')
            user_choice = input(print_style(
            f'''
                    !!!Invalid entry!!!
                Try again.
                {scenario_2nd}'''))
        else:
            if user_choice.upper() == 'FLASHLIGHT':
                
                os.system('cls')
                user_choice = input(print_style(scenario_4th))

                while user_choice.upper() not in('SCREAM', 'SHINE'):
                    
                    os.system('cls')
                    user_choice = input(print_style(
                    f'''
                        !!!Invalid entry!!!
                    Try again.
                    {scenario_4th}'''))
                else:
                    if user_choice.upper() == 'SCREAM':

                        os.system('cls')
                        print(print_style(scenario_6th))

                    elif user_choice.upper() == 'SHINE':

                        os.system('cls')
                        print(print_style(scenario_7th))

            elif user_choice.upper() == 'MOBILE':
                
                os.system('cls')
                user_choice = input(print_style(scenario_5th))

                while user_choice.upper() not in('MOBILE', 'CALL', 'LOOK'):
                    
                    os.system('cls')
                    user_choice = input(print_style(
                    f'''
                            !!!Invalid entry!!!
                        Try again.
                        {scenario_5th}'''))
                else:
                    if user_choice.upper() == 'MOBILE':

                        os.system('cls')
                        print(print_style(scenario_8th))

                    elif user_choice.upper() == 'CALL':

                        os.system('cls')
                        print(print_style(scenario_9th))

                    elif user_choice.upper() == 'LOOK':

                        os.system('cls')
                        print(print_style(scenario_10th))

    elif user_choice.upper() == 'DECLINE':
        
        os.system('cls')
        print(print_style(scenario_3rd))
