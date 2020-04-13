galera = list()
pessoa = list()
maip = menp = 0
while True:
    pessoa.append(str(input('Nome: ')).capitalize())
    pessoa.append(float(input('Peso: ')))
    galera.append(pessoa[:])
    pessoa.clear()
    while True:
        perg = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if perg in 'SN':
            break
    if perg == 'N':
        break
print('¬-'*40)
print(f'Foram cadastradas {len(galera):02} pessoas.')
for c, p in enumerate(galera):
    if c == 0:
        maip = menp = p[1]
    else:
        if p[1] > maip:
            maip = p[1]
        elif p[1] < menp:
            menp = p[1]
print(f'O maior peso foi de {maip:.1f}kg. Peso de:', end=' ')
for c in galera:
    if maip in c:
        print(c[0], end=' ')
print(f'\nO menor peso foi de {menp:.1f}kg. Peso de:', end=' ')
for c in galera:
    if menp in c:
        print(c[0], end=' ')
