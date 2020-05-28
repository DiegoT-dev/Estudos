from random import randint
from time import sleep
apostas = list()
jogo = list()
print(f'{"-"*30}\n\033[1:30m{"MEGA SENA":^30}\033[m\n{"-"*30}')
p = int(input('Quantos jogos você quer: '))
print('><'*20)
print('Gerando jogos......Aguarde......')
print('><'*20)
sleep(3)
for c in range(0, p):
    for n in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in jogo:
                break
        jogo.append(num)
    apostas.append(jogo[:])
    jogo.clear()
for i, c in enumerate(apostas):
    c.sort()
    print(f'Jogo {i+1}: {c}')
    sleep(1)
print('><'*20)
