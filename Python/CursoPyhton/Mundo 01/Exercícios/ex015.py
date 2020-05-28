d = int(input('Quanto dias alugado? '))
km = float(input('Quantos Km rodados? '))
a = (d*60)+(km*0.15)
print('O total a pagar é de R${:.2f}'.format(a))
