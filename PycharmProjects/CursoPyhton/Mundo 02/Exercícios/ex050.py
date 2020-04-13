soma = int(0)
print('__Somador dos números pares__\n')
for c in range(0, 6):
    n = int(input('Digite qualquer número: '))
    if n%2 == 0:
        soma += n
print('\nA soma dos números pares digitados é \033[1:31m{}\033[m.'.format(soma))