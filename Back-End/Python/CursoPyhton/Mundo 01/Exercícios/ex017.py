import math
cab = '='
cab2 = 'Cálculo da Hipotenusa'
print(cab*40)
print('{:^40}'.format(cab2))
print(cab*40)
cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
hip = math.hypot(cato, cata)
print('A hipotenusa do triangulo com lados {} e {} é {:.2f}.'.format(cato, cata, hip))
