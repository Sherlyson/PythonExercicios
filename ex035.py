a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a<b+c and b<a+c and c<a+b:
    print('Esses segmentos formam um triângulo!')
else:
    print('Esses segmentos não formam um triângulo')
