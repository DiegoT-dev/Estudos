def lin():
    print('-='*30)
def maior(lst):
    lin()
    print('Analisando os valores passados...')
    sleep(2)
    if len(lst) != 0:
        for c in lst:
            print(f'\033[1:32m{c}\033[m', end=' ')
            sleep(.5)
        print(f'\nForam informados ', end='')
        sleep(2)
        print(f'{len(lst)} valores ao todo.')
        sleep(1)
        print(f'O maior valor informado é ', end='')
        sleep(2)
        print(f'{max(lst)}.')
    else:
        print('Não foi informado nenhum número')
    sleep(1)
def escolhendo():
    n = list()
    x = randint(0, 10)
    if x != 0:
        for c in range(0, x):
            n.append(randint(0, 100))
    maior(n)
    n.clear()


from random import randint
from time import sleep
for c in range(0, randint(1, 6)):
    escolhendo()

