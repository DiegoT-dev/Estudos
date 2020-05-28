n = list()
for c in range(0, 5):
    x = int(input('Digite um valor: '))
    if c == 0:
        n.append(x)
        print('Valor adicionado...')
    else:
        for c in range(0, len(n)):
            if x < n[c]:
                n.insert(c, x)
                print(f'Valor adicionado na posição {c}...')
                break
        if x > n[-1]:
            n.append(x)
            print('Valor adicionado no final da lista...')
print('¬-'*30)
print(f'Os valores digitados, em ordem, foram: {n}')
