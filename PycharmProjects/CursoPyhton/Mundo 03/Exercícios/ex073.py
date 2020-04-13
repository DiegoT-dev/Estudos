cb = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
      'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
      'Bahia', 'Vasco da gama', 'Atlético-MG', 'Fluminense', 'Botafogo',
      'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
#for c in range(0, 5):
#    print(cb[c])
print('A tabela do Brasileirão 2019:')
print(cb)
print('Os 05 primeiro colocados foram: ')
print(cb[:5])
print('Os 04 últimos: ')
print(cb[-4:])
print('Em ordem alfabética:')
print(sorted(cb))
print('Colocação da Chapecoense:')
print(f'{cb.index("Chapecoense")+1}ª posição')
