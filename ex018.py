from math import cos, sin, tan, radians
ang = int (input('Insira um ângulo: '))
print('O ângulo {} tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}!'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
