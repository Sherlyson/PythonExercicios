preco = float(input('Qual o preço do produto? R$'))
print('''Qual será a condição de pagamento deste produto?
[1] À vista em dinheiro ou cheque
[2] Á vista no cartão
[3] Em até 2x no cartão
[4] Em 3x ou mais no cartão''')
op = int(input('Sua opção: '))

if op == 1:
    print('O valor a ser pago é R$ {:.2f}'.format(preco*0.9))
elif op == 2:
    print('O valor a ser pago é R$ {:.2f}'.format(preco*0.95))
elif op == 3:
    print('O valor a ser pago é R$ {:.2f}, sendo 2x de R${}'.format(preco, preco/2))
elif op == 4:
    p = int(input('Quantas parcelas? '))
    print('O valor a ser pago é R$ {:.2f}, sendo {}x de R${}'.format(preco*1.2, p, (preco*2)/2))
else:
    print('Opção Inválida!')