n = list()
while True:
    n.append(int(input('Digite um valor: ')))
    if len(n) > 1:
        msg = str('Valor adicionado com sucesso...')
        for c in range(0, len(n)-1):
            if n[-1] == n[c]:
                n.pop()
                msg = str('Valor duplicado! Não será adicionado...')
                break
        print(msg)
    else:
        print('Valor adicionado com sucesso...')
    while True:
        p = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if p in 'SN':
            break
    if p == 'N':
        break
n.sort()
print('-='*30)
print(f'Você digitou {n}')
