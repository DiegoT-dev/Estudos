aluno = str(input('Digite o nome do Aluno: '))
n1 = float(input('Qual é a primeira nota do {}: '.format(aluno)))
n2 = float(input('Qual é a segunda nota do {}: '.format(aluno)))
m = (n1+n2)/2
print('A média do aluno {} é de:\n {:^20,.1f}'.format(aluno, m))
