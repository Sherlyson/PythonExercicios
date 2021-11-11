n = int(input("Insira um número: "))
div = 0
for a in range(1,n+1):
    if n%a==0:
            div += 1
if div == 2:
    print("{} é primo".format(n))
else:
    print("{} não é primo pois pode ser dividido por {} números".format(n,div))
