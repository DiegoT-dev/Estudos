n = int(input('Escolha um número para a tabuada: '))
for c in range(0, 11):
    print('\033[31m{}\033[m x {:02} = \033[1:32m{:02}\033[m'.format(n, c, n*c))
