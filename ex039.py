from datetime import date
anon = int(input('Informe o seu ano de nascimento: '))
anoa = date.today().year
idade = anoa - anon
if idade < 18:
    print('Você deverá se alistar no exército em {}'.format(anon + 18))
elif idade == 18:
    print('Está na hora de você se alistar!')
else:
    print('Voce deveria ter se alistado em {}'.format(idade - 18, anon + 18))
