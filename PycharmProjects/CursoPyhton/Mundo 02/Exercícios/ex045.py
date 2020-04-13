from random import randint
from emoji import emojize
from time import sleep

pc = int(randint(1,3))
pedpc = emojize(':fist: PEDRA', use_aliases=True)
pappc = emojize(':hand: PAPEL', use_aliases=True)
tespc = emojize(':v: TESOURA', use_aliases=True)
ped = emojize('PEDRA :fist:', use_aliases=True)
pap = emojize('PAPEL :hand:', use_aliases=True)
tes = emojize('TESOURA :v:', use_aliases=True)
print('Vamos jogar Jokenpô!!!')
print('Eu já escolhi....')
us = int(input('Agora você Escolhe:\n[1]- {}    [2]- {}    [3]- {} ==> '.format(ped, pap, tes)))
if us == 1 or us == 2 or us == 3:
    print('Então vamos lá....')
    sleep(2)
    print('\n\033[1m{:^11}\033[m'.format('JO'))
    sleep(1)
    print('\033[1m{:^11}\033[m'.format('KEN'))
    sleep(1)
    print('\033[1m{:^11}\033[m'.format('PÔ'))
    if us == 1 and pc == 1:
        print('\n{} \033[1:31mvs\033[m {}'.format(ped, pedpc))
        print('\nEMPATAMOS!')
    elif us == 1 and pc == 2:
        print('\n{} \033[1:31mvs\033[m {}'.format(ped, pappc))
        print('\nGANHEI! HahaHA...')
    elif us == 1 and pc == 3:
        print('\n{} \033[1:31mvs\033[m {}'.format(ped, tespc))
        print('\nVOCÊ GANHOU!!!!')
    elif us == 2 and pc == 1:
        print('\n{} \033[1:31mvs\033[m {}'.format(pap, pedpc))
        print('\nVOCÊ GANHOU!!!!')
    elif us == 2 and pc == 2:
        print('\n{} \033[1:31mvs\033[m {}'.format(pap, pappc))
        print('\nEMPATAMOS!')
    elif us == 2 and pc == 3:
        print('\n{} \033[1:31mvs\033[m {}'.format(pap, tespc))
        print('\nGANHEI! HahaHA...')
    elif us == 3 and pc == 1:
        print('\n{} \033[1:31mvs\033[m {}'.format(tes, pedpc))
        print('\nGANHEI! HahaHA...')
    elif us == 3 and pc == 2:
        print('\n{} \033[1:31mvs\033[m {}'.format(tes, pappc))
        print('\nVOCÊ GANHOU!!!!')
    elif us == 3 and pc == 3:
        print('\n{} \033[1:31mvs\033[m {}'.format(tes, tes))
        print('\nEMPATAMOS!')
else:
    print('Opção inválida!')