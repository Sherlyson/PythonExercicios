n = int(input("Insira um número: "))
s = n
i = 1
while n != 999:
    n = int(input("Insira outro número: "))
    if n != 999:
        s += n
        i += 1
print("{} foram digitados e a soma deles equivale a {}".format(i, s))