n = list()
for c in range(0, 5):
    n.append(int(input(f'Digite o {c+1}º número: ')))
print('-='*30)
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {max(n)} e ele está na posição: ', end='')
for c, v in enumerate(n):
    if v == max(n):
        print(c+1, end='... ')
print(f'\nO menor valor digitado foi {min(n)} e ele está na posição: ', end='')
for c, v in enumerate(n):
    if v == min(n):
        print(c+1, end='... ')
