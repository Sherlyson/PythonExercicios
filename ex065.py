i = 0
somatoria = 0
opc = 'S'
menor = 0
maior = 0
while opc not in 'Nn':
    n = int(input("Insira um número: "))
    i += 1
    if i == 1:
        maior = n
        menor = n
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    somatoria += n
    opc = str(input("Você deseja continuar? (S/N) ")).upper().strip()
print("Você digitou {} números e a média foi {}".format(i, somatoria/i))
print("O maior valor inserido foi {} e o menor foi {}".format(maior, menor))
