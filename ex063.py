n = int(input("Insira quantos elementos sua sequência terá: "))
i = 3
s = 0
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
while i < n:
    s = t1+t2
    print(' -> {}'.format(s), end='')
    t1 = t2
    t2 = s
    i += 1
print(' -> final')
