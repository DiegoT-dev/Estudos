def cab(txt):
    teste = "Acessando o manual do comando '" + txt+"'"
    cont = len(teste)+4
    print('\033[30:44m~\033[m' * cont)
    print(f'\033[30:44m  {teste}  \033[m')
    print('\033[30:44m~\033[m' * cont)
def ajuda(fun):
    sleep(2)
    print('\033[7:30m', end='')
    help(fun)
    print('\033[m', end='')
    sleep(1)


from time import sleep
while True:
    print('\033[30:42m~~\033[m'*20)
    print(f'\033[30:42m{"SISTEMA DE AJUDA PyHELP":^40}\033[m')
    print('\033[30:42m~~\033[m'*20)
    x = str(input('Função ou Biblioteca -> ')).strip().lower()
    if x == 'fim':
        break
    cab(x)
    ajuda(x)
sleep(1)
print('\033[30:41m~~\033[m'*20)
print(f'\033[30:41m{"ATÉ LOGO!!!":^40}\033[m')
print('\033[30:41m~~\033[m'*20)