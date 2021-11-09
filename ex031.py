d = float(input('Qual a distância da sua viagem, em Km? '))
if d<=200:
    p = d*0.5
else:
    p = d*0.45
print('Sua passagem custa {:.2f} R$'.format(p))
