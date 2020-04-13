def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
def ParOuImpar(num=0):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Impar'


#n = int(input(('Digite um valor: ')))
#print(f'O fatorial de {n} é {fatorial(n)}.')
#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial()
#print(f'Os resustados são {f1}, {f2}, {f3}.')
n = int(input('Digite um número: '))
print(ParOuImpar(n))
