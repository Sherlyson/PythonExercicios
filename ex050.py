s = 0
for a in range(0,6):
    n = int(input("Insira o {} valor: ".format(a)))
    if n%2 == 0:
        s+= n
print(s)