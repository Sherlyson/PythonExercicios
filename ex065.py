i = menor = maior = somatoria = 0
opc = 'S'
while opc not in 'Nn':
    n = int(input("Insira um número: "))
    i += 1
    somatoria += n
    if i == 1:
        maior = n
        menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    opc = str(input("Você deseja continuar? (S/N) ")).upper().strip()
print("Você digitou {} números e a média foi {}".format(i, somatoria/i))
print("O maior valor inserido foi {} e o menor foi {}".format(maior, menor))
