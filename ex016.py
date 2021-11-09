from math import trunc
n = float(input('Insira um número: '))
print('O número {} tem a parte inteira {}'.format(n, trunc(n)))
'''também há como fazer usando int() ao inves de trunc, o mesmo exclui a necessidade de importação de bibliotecas'''
