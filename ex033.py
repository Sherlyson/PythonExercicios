a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))
if a > b and a > c:
    print('O maior número é {}'.format(a))
    if b > c:
        print('O menor número é {}'.format(c))
    else:
        print('O menor número é {}'.format(b))
if b > a and b > c:
    print('O maior número é {}'.format(b))
    if a > c:
        print('O menor número é {}'.format(c))
    else:
        print('O menor número é {}'.format(a))
if c > a and c > b:
    print('O maior número é {}'.format(c))
    if a > b:
        print('O menor número é {}'.format(b))
    else:
        print('O menor número é {}'.format(a))
