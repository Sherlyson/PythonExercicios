sexo = str(input("Insira o seu sexo: [M/F] ")).strip().upper()
while sexo not in 'MmFf':
    print("O valor inserido é inválido, por favor, insira novamente usando [M/F]")
    sexo = str(input("Insira o seu sexo: [M/F] ")).strip().upper()[0]
print("fim")
