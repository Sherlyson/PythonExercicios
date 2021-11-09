v = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o seu salário? R$'))
t = float(input('Em quanto tempo voce pretende pagar a casa (em anos)? '))
p = v / (t*12)

if p > s*0.3:
    print('Seu empréstimo foi negado! O valor da parcela (R$ {:.2f}) excede 30% de seu salário (R$ {:.2f})'.format(p, s*0.3))
else:
    print('Empréstimo aprovado! O valor da parcela será R${:.2f}'.format(p))
