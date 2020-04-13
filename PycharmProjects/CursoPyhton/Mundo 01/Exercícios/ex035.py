r1 = float(input('Digite o lado 1: '))
r2 = float(input('Digite o lado 2: '))
r3 = float(input('Digite o lado 3: '))
if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    print('Essas medidas podem formar um triângulo!')
else:
    print('Essas medidas não formam um triângulo!')
