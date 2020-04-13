def contador(x, y, z):
    if x < y:
        print(f'Contagem de {x} até {y} de {z} em {z}:')
        for c in range(x, y+1, z):
            print(c, end=' ')
            sleep(1)
        print('FIM!')
        sleep(1)
    if x > y:
        if z < 0:
            t = z*(-1)
        elif z == 0:
            t = 1
        else:
            t = z
        print(f'Contagem de {x} até {y} tirando {t}:')
        for c in range(x, y-1, -t):
            print(c, end=' ')
            sleep(1)
        print('FIM!')
        sleep(1)
def sep():
    print('-='*30)


from time import sleep
contador(1, 10, 1)
sep()
contador(10, 0, 2)
sep()
print('Agora é sua vez...')
i = int(input('Ínicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
contador(i, f, p)
