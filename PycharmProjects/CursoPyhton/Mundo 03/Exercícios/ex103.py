def ficha(x, y):
    if x == '':
        x = '<desconhecido>'
    return (f'O jogador {x} fez {y} gol(s) no campeonato.')


print('-'*30)
n = str(input('Nome do Jogador: ')).capitalize().strip()
while True:
    t = input('Número de Gols: ')
    if t == '':
        t = int(0)
        break
    elif t.isnumeric():
        t = int(t)
        break
print(ficha(n, t))
