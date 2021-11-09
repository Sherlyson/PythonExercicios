vel = int(input('Qual a velocidade atual do carro? '))
if vel>80:
    print('Você foi multado por exceder o limite de velocidade que é de 80Km/h!\n Você deve pagar uma multa de {:.2f}R$'.format((vel-80)*7))
print('Tenha um bom dia! Dirija com segurança!')
