prec = float(input('Valor do produto: R$'))
print('Qual será a forma de pagamento? ')
print('[1] - À Vista')
print('[2] - Parcelado')
esc = int(input())
if esc == 1:
    print('Forma de pagamento?')
    print('[1] - Dinheiro / Cheque')
    print('[2] - Cartão')
    escv = int(input())
    if escv == 1:
        precfinal = prec - ((prec*10)/100)
        print('Você terá 10% de desconto')
        print('O valor do produto ficará de R${:.2f}.'.format(precfinal))
    elif escv == 2:
        precfinal = prec - ((prec*5)/100)
        print('Você terá 5% de desconto')
        print('O valor do produto ficará de R${:.2f}.'.format(precfinal))
elif esc == 2:
    parcelas = int(input('Em quantas parcelas deseja realizar a compra? '))
    if parcelas == 2:
        print('Você pagará o valor de R${:.2f} em 2x de R${:.2f}'.format(prec, prec/2))
    elif parcelas >= 3:
        precfinal = prec + ((prec*20)/100)
        print('Você pagara o valor de R${:.2f} em {}x de R${:.2f}.'.format(precfinal, parcelas, precfinal/parcelas))
else:
    print('Opção inválida.')