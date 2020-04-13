matriz = [[[], [], []], [[], [], []], [[], [], []]]
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c].append(n)
print('><'*20)
for c in matriz:
    for l in c:
        for n in l:
            print(f'[{n:^5}]', end='')
    print('\n', end='')
