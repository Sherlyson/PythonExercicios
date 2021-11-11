maior = 0
menor = 999
for i in range(1,6):
    peso = float(input("Insira o {}º peso: ".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso registrado foi {} kg, enquanto o menor foi {} kg".format(maior, menor))