s = 0
for a in range (3,501,3):
    d = a%2
    if d !=0:
        s += a
print("A soma dos multiplos de 3, que são ímpares, até 500 é {}".format(s))