nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiusculas é: ', nome.upper())
print('Seu nome em minusculas é: ', nome.lower())
ndividido = nome.split()
print('Seu nome tem {} letras ao todo'.format(len(ndividido[0]) + len(ndividido[1]) + len(ndividido[2]) + len(ndividido[3])))
#Guanabara fez len(nome) - nome.count('') ao inves de separar tudo, minha forma fica errada
print('Seu primeiro nome tem {} letras'.format(len(ndividido[0])))
#Guanabara fez nome.find(''), visto que o find indica aonde começa o primeiro espaço. como se contam os indices de 0
#o espaço começa no indice que representa exatamente a quantidade de letras do primeiro nome