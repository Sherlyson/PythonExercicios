from random import randint
comp = randint(0, 5)
print('Eu pensei em um número, tente adivinhá-lo! ')
num = int(input('Em qual número eu pensei? '))
print('Hm...')
if comp == num:
    print('Você venceu, eu pensei no número {}'.format(comp))
else:
    print('Eu venci, pensei no número {} e não no {}'.format(comp, num))
