from datetime import date
anon = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - anon
if idade < 9:
    print('A categoria desse atleta é MIRIM')
elif 14 > idade >= 9:
    print('A categoria desse atleta é INFANTIL')
elif 19 > idade >= 14:
    print('A categoria desse atleta é JUNIOR')
elif 20 > idade >= 19:
    print('A categoria desse atleta é SÊNIOR')
else:
    print('A categoria desse atleta é MASTER')