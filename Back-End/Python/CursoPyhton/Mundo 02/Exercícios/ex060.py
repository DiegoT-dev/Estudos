n = int(input('Digite um número qualque para saber seu fatorial: '))
c = n
fatorial = n
if n == 0 or n == 1:
    print('{}! = 1.'.format(n))
else:
    while c != 1:
        fatorial = fatorial * (c-1)
        c = c - 1
    print('{}! = {}.'.format(n, fatorial))
