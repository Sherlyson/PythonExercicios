from random import randint
tentativas = 1
comp = randint(0, 10)
print('Eu pensei em um número, tente adivinhá-lo! ')
num = int(input('Em qual número eu pensei? '))
print('Hm...')
while num != comp:
    print("Boa tentativa, mas você errou :(")
    num = int(input("Tente novamente, insira outro número: "))
    tentativas += 1
print("Parabéns, você acertou! Você precisou de {} tentativas para acertar".format(tentativas))