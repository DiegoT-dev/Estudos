from time import sleep
nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
n1 = float(input('Qual foi a primeira nota do aluno {}: '.format(nome)))
n2 = float(input('Qual foi a segunda nota do aluno {}: '.format(nome)))
mf = (n1+n2)/2
print('Calculando Média...')
sleep(1)
print('Aguarde uns instantes')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('A média final do aluno {} foi de \033[1:34m{:.1f}\033[m'.format(nome, mf))
resp = str(input('Gostaria de analizar se o aluno passou de ano? ')).strip().capitalize()[:1]
if resp == 'S':
    print('Analizando parâmetros de fim do ano.')
    sleep(3)
    if mf <= 5.0:
        print('O aluno {} está:\n\033[1:30:41m REPROVADO \033[m'.format(nome))
    elif mf > 5.0 and mf <=6.9:
        print('O aluno {} está:\n\033[1:30:43m EM RECUPERAÇÃO \033[m'.format(nome))
    elif mf >= 7.0:
        print('O aluno {} está:\n\033[1:30:42m APROVADO \033[m'.format(nome))
else:
    print('Finalizando consulta...')
    sleep(1)
