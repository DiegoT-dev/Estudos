n = list()
ni = list()
np = list()
while True:
    n.append(int(input('Digite um valor: ')))
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'NS':
            break
    if resp == 'N':
        break
    print('¬-'*20)
print('¬-'*20)
for c in n:
    if c%2 == 0:
        np.append(c)
    else:
        ni.append(c)
print(f'Você digitou os seguintes números: {n}')
print(f'Os números pares digitados foram : {np}')
print(f'E os valores ímpares digitados foram: {ni}')
