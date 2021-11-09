frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase!'.format(frase.lower().count('a')))
print('A letra A aparece pela primeira vez no índice {}'.format(frase.lower().find('a')))
print('A letra aparece pela ultima vez no índice {}'.format(frase.lower().rfind('a')))
