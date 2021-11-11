from datetime import date
anoa = date.today().year
maior = 0
menor = 0
for i in range(1,8):
    anon = int(input("Insira o {}º ano de nascimento: ".format(i)))
    if anoa-anon >= 21:
        maior += 1
    else:
        menor += 1
print("{} pessoas são maiores e {} pessoas são menores!".format(maior, menor))