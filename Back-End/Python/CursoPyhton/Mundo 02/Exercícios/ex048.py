soma = int(0)
for c in range(3, 501, 3):
    if c%2 == 1:
        soma = soma + c # soma += c
print('A soma é {}.'.format(soma))
