sa = float(input('Digite o salário atual do funcionário: R$'))
if sa > 1250:
    sf = sa + ((sa*10)/100)
else:
    sf = sa + ((sa*15)/100)
print('O novo salário do funcionário será de R${:.2f}'.format(sf))
