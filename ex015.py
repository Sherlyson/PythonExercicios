d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
print('O total a pagar é de R${:.2f}'.format((d*60)+(0.15*km)))
