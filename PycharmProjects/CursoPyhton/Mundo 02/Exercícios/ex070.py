barato = ''
cmm = total = mp = 0
while True:
    print('_¬'*30)
    produto = str(input('Produto: ')).strip().capitalize()
    preco = float(input('Valor: R$'))
    if mp == 0 or preco < mp:
        mp = preco
        barato = produto
    if preco > 1000:
        cmm += 1
    total += preco
    print('_¬'*30)
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
print('-'*20, 'Fechamento de Caixa', '-'*20)
print(f'Valor total da compra: R${total:.2f}.')
print(f'Você comprou {cmm} produtos acima de R$1000.00')
print(f'O produto desta compra mais barato foi: {barato} por R${mp}.')
