n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número:'))
t1 = int
m1 = int
m2 = int
t3 = int
m3 = int
print('Você digitou os número {}, {} e {}'.format(n1, n2, n3))
print('Em ordem decrescente eles ficam assim....')
if n1 > n2:
    t1 = n1
    t2 = n2
else:
    t1 = n2
    t2 = n1
if n3 > t1:
    m1 = n3
    m2 = t1
    m3 = t2
else:
    if n3 > t2:
        m1 = t1
        m2 = n3
        m3 = t2
    else:
        m1 = t1
        m2 = t2
        m3 = n3
print('Maior: {}.'.format(m1))
print('Intermediário: {}.'.format(m2))
print('Menor: {}.'.format(m3))
