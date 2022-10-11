print()
print('Hello! Let\'s play a game?')
print()
print('Give me the following informations to start: ')
print()

adjective = input('An Adjective: ')
animal = input('An Animal: ')
first_verb = input('A Verb: ')
exclamation = input('An Exclamation: ')
second_verb = input('Another verb: ')
third_verb = input('Another verb: ')

output = '''
                  ▄▀▄     ▄▀▄
                 ▄█░░▀▀▀▀▀░░█▄
             ▄▄  █░░░░░░░░░░░█  ▄▄
            █▄▄█ █░░▀░░┬░░▀░░█ █▄▄█
»»———————————————————　★　—————————————————————««
    
    Your story is:
    
    The other day, I was really in trouble.
    It all started when I saw a very {0}
    {1} {2} down the hallway.
    \"{3}!\" I yelled.
    But all I could think to do was to
    {4} over and over. Miraculously,
    that caused it to stop, but not before it
    tried to {5} right in front of my family.

»»———————————————————  ★　—————————————————————««
              ツ Ⓕ Ⓤ Ⓝ Ⓝ Ⓨ ツ

'''.format(
        adjective.lower(),
        animal.lower(),
        first_verb.lower(),
        exclamation.capitalize(),
        second_verb.lower(),
        third_verb.lower(),
    )

print(output)