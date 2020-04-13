'''sexo = str(input('Digite seu sexo [M/F]: ')).strip()
teste = 0
if sexo != 'M' or sexo != 'F':
    teste = 1
    while not teste == 0:
        print('Dado iválido...')
        sexo = str(input('Digite seu sexo [M/F]: ')).strip()
        if sexo == 'M' or sexo == 'F':
            teste = 0
print('Passou!')'''
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido. Digite novamente seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo registrado com sucesso.')
