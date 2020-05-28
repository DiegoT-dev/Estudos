n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
op = 0
while not op == 5:
    op = int(input('Escolha uma operação:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos valore\n[5] Sair\n'))
    if op == 1:
        print('\033[1:31mA soma de {} e {} é {}.\033[m'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('\033[1:31mA multiplicação de {} e {} é {}.\033[m'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('\033[1:31mEntre {} e {} o maior é {}.\033[m'.format(n1, n2, n1))
        elif n1 < n2:
            print('\033[1:31mEntre {} e {} o maior é {}.\033[m'.format(n1, n2, n2))
        else:
            print('\033[1:31m{} e {} são Iguais.\033[m'.format(n1, n2))
    elif op == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
print('Finalizado!')
