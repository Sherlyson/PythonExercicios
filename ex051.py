n = int(input("Insira o primeiro termo da PA: "))
r = int(input("insira a razão da PA: "))
for a in range (1, 11):
    pa = n + (a-1) * r
    print('O termo {} da PA é {}'.format(a, pa))
