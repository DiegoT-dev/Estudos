print('{0} Progressão Aritmética {0}'.format('*'*10))
pt = int(input('Digite o Primeiro Termo da \033[1:30mPA\033[m: '))
rz = int(input('Digite qual a Razão para essa \033[1:30mPA\033[m: '))
termos = int(input('Quantos termos da \033[1:30mPA\033[m você quer mostrar? '))
tf = pt + (termos-1)*rz
print('\n(', end='')
for c in range(pt, tf+1, rz):
    print('\033[1:30m{}\033[m'.format(c), end=',')
print('...)')
print('\nEsses são os {} termos da PA.'.format(termos))
