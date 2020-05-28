num = [[], []]
for c in range(0, 7):
    n = (int(input('Digite um número: ')))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
for c in num:
    c.sort()
print('¬-'*30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
