reg = 1
adultos = homem = mulher = 0
while True:
    print('-='*30)
    idade = int(input(f'Digite a idade da {reg}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {reg}ª pessoa [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Inválido. ', end='')
        sexo = str(input(f'Digite o sexo da {reg}ª pessoa [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        adultos += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    print('-=' * 30)
    cont = str(input('Quer cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        print('Inválido. ', end='')
        cont = str(input('Quer cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    if cont == 'S':
        reg += 1
    else:
        break
print('+~'*30)
print(f'Foram cadastrados:\n{adultos} pessoas maiores de idades;\n{homem} homens;\n{mulher} mulheres abaixo de 20 anos.')