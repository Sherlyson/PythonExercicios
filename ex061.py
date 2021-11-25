n = int(input("Insira o primeiro termo da PA: "))
r = int(input("insira a razão da PA: "))
c = 1
while c < 11:
    pa = n + (c - 1) * r
    print('O termo {} da PA é {}'.format(c, pa))
    c+= 1