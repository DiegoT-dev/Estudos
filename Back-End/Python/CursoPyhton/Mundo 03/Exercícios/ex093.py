dados = dict()
gols = list()
tot = 0
dados['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols na {c}ª partida? ')))
dados['gols'] = gols[:]
for c in dados['gols']:
    tot += c
dados['total'] = tot ## Para somar dados da lista poderia fazer ---> sum(gols)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'{"":5}=> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
