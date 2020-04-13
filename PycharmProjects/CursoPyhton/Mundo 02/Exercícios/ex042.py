r1 = float(input('Digite o lado 1: '))
r2 = float(input('Digite o lado 2: '))
r3 = float(input('Digite o lado 3: '))
if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    print('Essas medidas podem formar um triângulo!')
    resp = str(input('Gostaria de analizar que tipo de triângulo essas medidas formam? ')).strip().capitalize()[:1]
    if resp == 'S':
        print('Analisando...')
        if r1 == r2 and r1 == r3:
            print('Essas medidas formariam um triângulo EQUILÁTERO!!!')
        elif r1==r2 or r1 == r3 or r2 == r3:
            print('Essas medidas formariam um triângulo ISÓSCELES!!!')
        elif r1 != r2 and r2 != r3 and r1 != r3:
            print('Essas medidas formariam um triângulo ESCALENO!!!')
else:
    print('Essas medidas não formam um triângulo!')
