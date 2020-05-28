from time import sleep
print('Vou descobrir dos números que você digitar qual é o maior...')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
print('Ok....deixa eu pensar')
sleep(2)
print('.')
sleep(2)
print('.')
sleep(2)
print('.')
sleep(2)
print('Pronto....')
sleep(1)
if n1 == n2:
    print('Pensou que ia me enganar?...os dois números que você digitou são iguais...')
elif n1 > n2:
    print('O primeiro valor é maior...')
    sleep(1)
    print('\033[1:36m{}\033[m > {}'.format(n1, n2))
elif n1 < n2:
    print('O segundo valor é maior')
    sleep(1)
    print('{} < \033[1:36m{}\033[m'.format(n1, n2))
