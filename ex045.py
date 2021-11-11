from random import randint
print('Vamos jogar pedra, papel ou tesoura!')
jog = int(input('''Escolha entre pedra, papel e tesoura: 
[1] para pedra
[2] para papel
[3] para tesoura
Sua opção: '''))
pc = randint(1, 3)
if jog == pc:
    print('Você e o computador escolheram a mesma opção, o que gerou um empate!')
elif jog == 1:
    if pc == 2:
        print('DERROTA! Você escolheu pedra e o computador papel!')
    else:
        print('VITÓRIA! Você escolheu pedra e o computador tesoura!')
elif jog == 2:
    if pc == 1:
        print('VITÓRIA! Você escolheu papel e o computador pedra!')
    else:
        print('DERROTA! Você escolheu papel e o computador tesoura!')
elif jog == 3:
    if pc == 1:
        print('DERROTA! Você escolheu tesoura e o computador pedra!')
    else:
        print('VITÓRIA! Você escolheu tesoura e o computador p  apel!')
