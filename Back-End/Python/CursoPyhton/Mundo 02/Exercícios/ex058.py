from random import randint
tentativas = 1
pc = randint(0, 10)
print('Pensei em um número de 0 a 10.')
print('Tente adivinhar, que número foi esse? ', end='')
jog = int(input())
while jog != pc:
    tentativas += 1
    print('ERROU!!!!')
    print('....Tente denovo: ', end='')
    jog = int(input())
print('ACERTOU!!!....eu tinha pensado no número {}, e você acertou com {:02} tentativas.'.format(pc, tentativas))
