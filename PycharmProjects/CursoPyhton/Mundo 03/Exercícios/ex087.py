matriz = [[[], [], []], [[], [], []], [[], [], []]]
somap = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c].append(n)
print('><'*20)
for c in matriz:
    for l in c:
        for n in l:
            if n % 2 == 0:
                somap += n
            print(f'[{n:^5}]', end='')
    print('\n', end='')
print('><'*20)
print(f'A soma dos valores pares é {somap}.')
somat = matriz[0][2][0] + matriz[1][2][0] + matriz[2][2][0]
print(f'A soma dos valores da terceira coluna é {somat}.')
for c in matriz[1]:
    for m in c:
        if m > maior:
            maior = m
print(f'O maior valor da segunda linha é o {maior}.')
