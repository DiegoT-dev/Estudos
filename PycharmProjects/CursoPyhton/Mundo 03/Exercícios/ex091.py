from random import randint
from time import sleep
from operator import itemgetter
rodada = dict()
for c in range(1, 5):
    rodada[f'jogador{c}'] = randint(1, 6)
print('Jogando os dados')
sleep(2)
for k, v in rodada.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
print()
print('Ranking da rodada:')
sleep(2)
##### Resolução Guanabara #####
ranking = sorted(rodada.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
##### Minha resolução ####
'''ranking = sorted(rodada.values(), reverse=True)
pp = dict()
for r in ranking:
    for k, v in rodada.items():
        if v == r and k not in pp:
            pp[k] = v
            break
c = 1
for k, v in pp.items():
    print(f'{c}º lugar: {k} com {v}')
    c += 1
    sleep(1)'''

