people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

min_age = 99999999999999
youngest = ''

for person in people:
        
    parts = person.split()

    person_name = parts[0]
    person_age = int(parts[1])

    min_age = min(person_age, min_age)    
    
    if person_age == min_age:
    
        youngest =  person_name
    
print(f'The younguest person is {youngest.capitalize()} with {min_age} years old.')