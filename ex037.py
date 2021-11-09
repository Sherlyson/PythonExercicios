n = int(input('Digite um número inteiro: '))
print('Escolha uma da bases para conversão: ')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para binário equivale a {}'.format(n, bin(num)[2:]))
elif op == 2:
    print('{} convertido para octal equivale a {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} convertido para hexadecimal equivale a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')
