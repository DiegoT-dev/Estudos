n = (int(input('Digite um número: ')),
     int(input('Digite um outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite um último número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
print(f'O valor 3 ', end='')
if 3 in n:
    print(f'apareceu na {n.index(3)+1}ª posição')
else:
    print('não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
