pessoas = list()
dado = dict()
while True:
    dado['nome'] = str(input('Nome: ')).strip().capitalize()
    dado['idade'] = int(input('Idade: '))
    while True:
        dado['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dado['sexo'] in 'MF':
            break
        else:
            print('Opção inválida')
    pessoas.append(dado.copy())
    while True:
        cont = str(input('Quer cadastrar mais uma pessoa? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
idade = 0
for p in pessoas:
    idade += p['idade']
print(f'A média de idade do grupo é {idade/len(pessoas):.2f} anos.')
mulheres = list()
paid = list()
for c in pessoas:
    if c['sexo'] == 'F':
        mulheres.append(c['nome'])
    if c['idade'] > idade/len(pessoas):
        paid.append(c['nome'])
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'As pessoas com idade acima de {idade/len(pessoas)} são: {paid}')

