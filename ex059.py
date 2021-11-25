opc = 0
num = int(input("Insira um número: "))
ndois = int(input("Insira outro número: "))
while opc != 5:
    print("=-----MENU-----")
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair")
    opc = int(input("Opção -> "))
    if opc == 1:
        res = num + ndois
        print("O resultado da soma é {}".format(res))
    elif opc == 2:
        res = num * ndois
        print("O resultado da multiplicação é {}".format(res))
    elif opc == 3:
        if num > ndois:
            print("{} é maior que {}".format(num, ndois))
        elif ndois > num:
            print("{} é maior que {}".format(ndois, num))
        else:
            print("Os números inseridos são iguais.")
    elif opc == 4:
        num = int(input("Insira um número: "))
        ndois = int(input("Insira outro número: "))
    elif opc == 5:
        print("Finalizando...")
    else:
        print("Opção inválida! Tente novamente")
print("fim")