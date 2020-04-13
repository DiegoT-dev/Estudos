classe = list()
aluno = list()
notas = list()
while True:
    nome = str(input('Nome: ')).capitalize().strip()
    aluno.append(nome)
    for c in range(1, 3):
        nota = float(input(f'Nota {c}: '))
        notas.append(nota)
    aluno.append(notas[:])
    classe.append(aluno[:])
    notas.clear()
    aluno.clear()
    while True:
        resp = str(input('Continuar Cadastrando? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('¬-'*30)
print(f'{"Nº.":<3} {"NOME":<15}{"MÉDIA":^7}')
print('-'*30)
for c in range(0, len(classe)):
    print(f'{c:<3} {classe[c][0]:<15}{(classe[c][1][0]+classe[c][1][1])/2:^7.1f}')
while True:
    print('-' * 30)
    opcao = int(input('Mostrar a nota de qual aluno? (999 p/ interromper) '))
    if opcao == 999:
        break
    elif opcao + 1 > len(classe):
        print('Opção Inválida.')
    else:
        print(f'Notas de {classe[opcao][0]} são {classe[opcao][1]}')
print('-'*30)
print('FIM DO PROGRAMA')
