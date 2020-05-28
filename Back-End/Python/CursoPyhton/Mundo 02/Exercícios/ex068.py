from random import randint
from time import sleep
print('-'*20, 'PAR ou ÍMPAR', '-'*20)
jogadas = 0
while True:
    print('~~'*30)
    escolha = str(input('Escolha [0] PAR [1] IMPAR: ')).strip()[0]
    while escolha not in '01':
        print('Opção Inválida. Tente novamente!')
        escolha = str(input('Escolha [0] PAR [1] IMPAR: ')).strip()[0]
    print('-='*20, '\033[1:30m')
    if escolha == '0':
        print('Jogador [PAR] vs [IMPAR] Computador')
    else:
        print('Jogador [Impar] vs [Par] Computador')
    print('\033[m-=' * 20)
    n = int(input('Agora escolha um número para jogarmos: '))
    pc = randint(0, 10)
    for c in range(3, 0, -1):
        print(f'{c}', end='...')
        sleep(1)
    print(f'\nJogador {n} vs {pc} Computador')
    if (n + pc)%2 == 0:
        if escolha == '0':
            print('Você ganhou!!!Mais uma vez...')
            jogadas += 1
        else:
            print('Você perdeu!!!')
            break
    else:
        if escolha == '0':
            print('Você perdeu!!!')
            break
        else:
            print('Você ganhou!!! Mais uma vez...')
            jogadas += 1
print('~~'*30)
print(f'Você ganhou um total de {jogadas} jogadas.')
