n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
md = (n1+n2)/2
if md < 5:
    print('REPROVADO')
elif 7 > md > 5:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')