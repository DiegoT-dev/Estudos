def fatorial(n=1, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado o fatorial.
    :param show: Aparece a decomposição do fatotrial por completa (Padrão = False) de forma opcional.
    :return: O valor final do fatorial
    '''
    print('-'*30)
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
    return f


print(fatorial(50, True))
