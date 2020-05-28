def cab(msg):
    print(f'{msg:^30}\n{"-"*30}')
def área(lst):
    a = 1
    for n in lst:
        a *= n
    print(f'A área de um terreno {lst[0]}x{lst[1]} é de {a:.1f}m²')
def cham(txt):
    x.append(float(input(f'{txt} (m): ')))


x = list()
cab('Controle de Terreno')
cham('Largura')
cham('Comprimento')
área(x)
