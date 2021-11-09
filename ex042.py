a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a<b+c and b<a+c and c<a+b:
    print('Esses segmentos formam um triângulo!')
    if a==b and b==c:
        print('O triângulo formado por esses segmentos é equilátero!')
    elif a==b or b==c or a==c:
        print('O triângulo formado por esses segmentos é isóceles!')
    else:
        print('O triângulo formado por esses segmentos é escaleno!')
else:
    print('Esses segmentos não formam um triângulo')
