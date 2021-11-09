s = float(input('Insira o valor do seu salário: R$'))
if s > 1250:
    sn = s*0.1 + s
else:
    sn = s*0.15 + s
print('Quem recebia R${} vai passar a receber R${}'.format(s, sn))
