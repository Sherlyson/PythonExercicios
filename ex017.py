from math import hypot
co = float(input('Insira o tamanho do cateto oposto: '))
ca = float(input('Insira o tamanho do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa do seu triangulo retangulo é {:.2f}'.format(h))
