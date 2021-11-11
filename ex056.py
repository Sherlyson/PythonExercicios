midade = 0
idademv = 0
countm = 0
for i in range(1,5):
    print("----- {}º pessoa -----".format(i))
    nome = str(input("Insira o nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M ou F): ")).strip()
    if sexo in 'Mm' and idade > idademv:
        nomemv = nome
        idademv = idade
    if sexo in 'Ff' and idade < 20:
        countm+= 1
    midade += idade/4
print("A média de idade do grupo é {} anos".format(midade))
print("O nome do homem mais velho é {}".format(nomemv))
print("São {} as mulheres com menos de 20 anos".format(countm))