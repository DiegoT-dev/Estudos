classe = dict()
classe['nome'] = str(input('Nome: ')).strip().capitalize()
classe['média'] = float(input(f'Média de {classe["nome"]}: '))
if classe['média'] >= 7:
    classe['situação'] = 'Aprovado'
elif 7 > classe['média'] >= 5:
    classe['situação'] = 'Recuperação'
elif classe['média'] < 5:
    classe['situação'] = 'Reprovado'
for k, v in classe.items():
    print(f'{k.capitalize()} é igual a {v}.')
