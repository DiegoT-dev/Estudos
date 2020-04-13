dados = list()
gol = list()
jogador = dict()
print('-='*30)
while True:
    jogador['nome'] = str(input('Nome: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, partidas+1):
        gol.append(int(input(f'Quantos gols na {c}ª partida? ')))
    jogador['gols'] = gol[:]
    tot = 0
    for c in gol:
        tot += c
    gol.clear()
    jogador['total'] = tot
    dados.append(jogador.copy())
    while True:
        cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        print('-='*30)
        break
    print('-='*30)
print(f'{"cod.:":^9} {"Nome":<20} {"Total de Gols"}')
for c, j in enumerate(dados):
    print(f'{c:^9} {j["nome"]:<20} {j["total"]:^13}')
while True:
    print('-' * 50)
    det = int(input('Mostrar dados de qual jogador? (999 p/ Sair) Cod.: '))
    if det == 999:
        print('-' * 50)
        break
    elif det > len(dados)-1:
        print(f'Erro! O jogador com o cod.: {det} não existe. Tente novamente!')
    else:
        print(f'{"--":>5} LEVANTAMENTO DO JOGADOR \033[3:33m{dados[det]["nome"].upper()}\033[m')
        for i, v in enumerate(dados[det]['gols']):
            print(f'{"":7}=> Na partida {i + 1}, fez {v} gols.')
print(f'{"->"*6} Finalizando {"<-"*6}')
