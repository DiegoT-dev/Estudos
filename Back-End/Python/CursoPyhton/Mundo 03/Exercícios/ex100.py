def sorteio():
    print('Sorteando os valores...', end='')
    sleep(2)
    for c in range(0, 5):
        n = randint(0, 10)
        print(n, end=' ')
        numero.append(n)
        sleep(.5)
def somapar(lst):
    s = 0
    print(f'\nA soma dos valores pares entre {lst} é ', end='')
    for c in lst:
        if c % 2 == 0:
            s += c
    print(s)


from random import randint
from time import sleep
numero = list()
sorteio()
sleep(1)
somapar(numero)