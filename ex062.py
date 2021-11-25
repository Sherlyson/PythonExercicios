p = int(input("Insira o primeiro termo da PA: "))
r = int(input("insira a razão da PA: "))
count = 0
t = p
extra = 10
while extra != 0:
    y = 0
    while y < extra:
        print('{} -> '.format(t), end='')
        t += r
        y += 1
        count += 1
    extra = int(input("Quantos termos você deseja ver a mais? "))
print("Foram exibidos {} termos da PA".format(count))