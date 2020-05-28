print('{0} Palíndromo {0}'.format('*'*20))
frase = str(input('Digite qualquer frase: ')).strip().upper().split()
frase2 = ''.join(frase)
frase3 = frase2[::-1]
if frase2 == frase3:
    print('Essa frase é um Palíndromo!')
else:
    print('Essa frase não é um Palíndromo!')
