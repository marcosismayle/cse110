print() #give a space
print('Amusement Park Rides') #title
print() #give a space

# ask for the first rider age, height and if there are a second rider. 
first_rider_age = int(input('What is the age of the first rider? '))
first_rider_height = int(input('What is the height of the first rider? '))

may_ride = False #set "may_ride = False" globaly.

if first_rider_age >= 12 and first_rider_age <= 17:
    golden_passport1 = input('Is there a Golden Passport (yes/no)? ')

is_second_rider = input('Is there a second rider (yes/no)? ')

# If there are two riders.
if is_second_rider.lower() == 'yes':

    # ask the second rider age and height.
    second_rider_age = int(input('What is the age of the second rider? '))
    second_rider_height = int(input('What is the height of the second rider? '))

    if second_rider_age >= 12 and second_rider_age <= 17:
        golden_passport2 = input('Is there a Golden Passport (yes/no)? ')

    #No one under 36 inches may ever ride, either by themselves or with another rider.
    if first_rider_height < 36 or second_rider_height < 36:
        may_ride = False
    else:
    #If there are two riders and one of them is at least 18 years old, they may ride together.
        if first_rider_age >= 18 or second_rider_age >= 18 or golden_passport1.lower() == 'yes' or golden_passport2.lower() == 'yes':
            may_ride = True
        else:
            #If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.
            if first_rider_age >= 12 and second_rider_age >= 12 and first_rider_height >= 52 and second_rider_height >= 52:
                may_ride = True
    
            #If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. 
            elif (first_rider_age >= 16 and second_rider_age >= 14) or (first_rider_age >= 14 and second_rider_age >= 16):
                may_ride = True 
    
            else:
                may_ride = False

else:    
# if there are just one rider.
    if (first_rider_age >= 18 or golden_passport1.lower() == "yes") and first_rider_height >= 62:
        can_ride = True
    else:
        may_ride = False
    
# print the result to the users.
if may_ride:
    print() #give a space
    print('Welcome to the ride. Please be safe and have fun!')
    print() #give a space
else:
    print() #give a space
    print('Sorry, you may not ride.')
    print() #give a space
