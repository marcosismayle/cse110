print('Please enter the following information: ')
print('')

first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID number: ')
hair_color = input('Hair color: ')
eyes_color = input('Eyes color: ')
month = input('Month: ')
training = input('Training: ')


output ='''
The ID Card is: 
---------------------------------
{1}, {0}
{4}
ID: {5}

{2}
{3}

Hair: {6}       Eyes: {7}
Month: {8}     Training: {9}
---------------------------------
'''.format(
        first_name.capitalize(),
        last_name.upper(),
        email.lower(),
        phone,
        job_title.title(),
        id_number,
        hair_color.capitalize(),
        eyes_color.capitalize(),
        month.capitalize(),
        training.capitalize()
    )

print(output)
