peso = float(input('Insira o seu peso: '))
alt = float(input('Insira a sua altura (em metros): '))
imc = peso / alt**2
if imc < 18.5:
    print('Seu IMC é {:.2f}. Vocẽ está abaixo do peso'.format(imc))
elif 25 > imc >=18.5:
    print('Seu IMC é {:.2f}. Vocẽ está com o peso ideal'.format(imc))
elif 30 > imc >= 25:
    print('Seu IMC é {:.2f}. Vocẽ está com sobrepeso'.format(imc))
elif 40 > imc >= 30:
    print('Seu IMC é {:.2f}. Vocẽ está obeso'.format(imc))
else:
    print('Seu IMC é {:.2f}. Vocẽ está com obesidade mórbida'.format(imc))