cont50 = cont20 = cont10 = cont1 = 0
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Qual o valor do saque? R$ '))
if valor > 50:
    while True:
        if valor < 50:
            break
        else:
            valor -= 50
            cont50 += 1
    print(f'Total de {cont50} notas de R$50.')
if valor > 20:
    while True:
        if valor < 20:
            break
        else:
            valor -= 20
            cont20 += 1
    print(f'Total de {cont20} notas de R$20.')
if valor > 10:
    while True:
        if valor < 10:
            break
        else:
            valor -= 10
            cont10 += 1
    print(f'Total de {cont10} notas de R$10.')
if valor > 0:
    while True:
        valor -= 1
        cont1 += 1
        if valor == 0:
            break
    print(f'Total de {cont1} notas de R$1.')
print('='*30)
print('O BANCO CEV agradece! Tenha um bom dia.')
