n = str(input('Digite seu nome completo: ')).strip()
f = int(len(n.split()))
print('Seu primeiro nome é {}.'.format(n.split()[0]))
print('Seu último nome é {}.'.format(n.split()[f-1]))
