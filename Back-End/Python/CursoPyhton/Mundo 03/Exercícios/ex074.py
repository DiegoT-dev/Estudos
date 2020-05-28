from random import randrange
n = (randrange(99), randrange(99), randrange(99),
     randrange(99), randrange(99))
maior = menor = 0
print('Os número sorteados foram:', end=' ')
for c in range(0, len(n)):
    print(n[c], end=' ')
    if c == 0:
        maior = n[c]
        menor = n[c]
    elif n[c] > maior:
        maior = n[c]
    elif n[c] < menor:
        menor = n[c]
print(f'\nO maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')
#
#Resposta do Guanabara sem IF:
#print(f'\nO maior valor sorteado foi {max(n)}')
#print(f'O menor valor sorteado foi {min(n)}')