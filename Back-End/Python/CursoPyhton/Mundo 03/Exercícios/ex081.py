from time import sleep
n = list()
while True:
    n.append(int(input('Digite um valor: ')))
    while True:
        resp = str(input('Quer digitar mais um valor: [S/N] ')).strip().upper()[0]
        if resp in 'NS':
            break
    if resp == 'N':
        break
    print('¬-'*20)
print('¬-'*20)
print('Analisando os dados', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(1)
print(f'\n{"¬-"*20}')
print(f'Você digitou os seguintes números: {n}')
print(f'Foram digitados ao todo {len(n)} elementos')
n.sort(reverse=True)
print(f'Os número digitados em ordem decrescente: {n}')
print('O valor 5 ', end='')
if 5 in n:
    print(f'foi digitado e está na sua lista {n.count(5)}x.')
else:
    print('não aparece nenhuma vez.')
