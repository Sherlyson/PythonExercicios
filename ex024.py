cid = str(input('Digite a cidade que você nasceu: ')).strip()
n = cid.split()
print('santo' in n[0].lower())
#ou sem o split fazer apenas print(cid[:5 == 'Santo') cid até 5 pois Santo só tem 5 letras
