nome = str(input('Digite seu nome completo ')).strip()
print('Seu primeiro nome é: {}'.format(nome[:nome.find(' ')]))
print('Seu último nome é: {}'.format(nome[nome.rfind(' '):]))
