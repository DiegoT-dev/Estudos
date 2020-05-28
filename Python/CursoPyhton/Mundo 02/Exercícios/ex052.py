from emoji import emojize
print('{0} Número Primo {0}'.format('*'*20))
n = int(input('Digite um número para saber se ele é ou não primo: '))
frase = emojize('É Primo.')
for c in range(2, n):
    if n % c == 0:
        frase = frase.replace('É', '\033[1:31mNão é\033[m')
print('\nO número {} {}'.format(n, frase), end=' ')
if frase == 'É Primo.':
    print(emojize(':thumbsup:', use_aliases=True))
elif frase == '\033[1:31mNão é\033[m Primo.':
    print(emojize(':thumbsdown:', use_aliases=True))
