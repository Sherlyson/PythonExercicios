n = int(input("Insira um número para calcularmos seu fatorial: "))
c = n
fat = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print('{}'.format(fat))
