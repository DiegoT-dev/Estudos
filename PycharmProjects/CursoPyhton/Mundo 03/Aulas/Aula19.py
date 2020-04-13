# Variáveis Compostas:
# _____________ Dicionários ________________
# Variáveis compostas podem comecar de 3 formas: () / [] / {}
# Dicionários são representadas por {}
# Variáveis em dicionario podem ser declaradas com 'variavel' = dict()
# Dicionários são variaveis compostas onde eu posso personalizar os indices
##########################################################
'''pessoas = {'nome': 'Diego', 'sexo': 'M', 'idade': 34}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''
'''estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = list()
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['uf'])'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).capitalize().strip()
    estado['sigla'] = str(input('Sigla: ')).upper().strip()
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')
