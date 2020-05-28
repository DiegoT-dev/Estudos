d = float(input('Quantos Km terá sua viajem? '))
if d > 200:
    print('Seu bilhete custará R${:.2f}.'.format(d * .45))
else:
    print('Se bilhete custará R${:.2f}.'.format(d * .5))
print('Tenha uma ótima viajem!')
