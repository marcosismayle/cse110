print()
print('Olá! Que tal um joguinho?')
print()
print('Vamos começar com algumas informações ok!')
print()

adjective = input('Digite um adjetivo: ')
animal = input('Um animal: ')
first_verb = input('Um verbo: ')
exclamation = input('Uma exclamação: ')
second_verb = input('Outro verbo: ')
third_verb = input('E pra terminar, outro verbo: ')

output = '''
                  ▄▀▄     ▄▀▄
                 ▄█░░▀▀▀▀▀░░█▄
             ▄▄  █░░░░░░░░░░░█  ▄▄
            █▄▄█ █░░▀░░┬░░▀░░█ █▄▄█
»»———————————————————　★　—————————————————————««
    
    Sua história é:
    
    Outro dia, eu estava realmente em apuros.
    Tudo começou quando vi um {0} {1} {2}
    no corredor.
    \"{3}!\" Eu gritei.
    Mas tudo que eu conseguia pensar em fazer era
    {4} repetidamente. Milagrosamente,
    isso o fez parar, mas não antes dele
    {5} bem na frente da minha família.

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