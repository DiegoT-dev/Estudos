idadetot = int()
homemvelho = str
idadehv = int(0)
mulheres20 = int (0)
for c in range(0, 4):
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().capitalize()[0:1]
    if sexo == 'M':
        if idade > idadehv:
            idadehv = idade
            homemvelho = nome
    elif sexo == 'F':
        if idade < 20:
            mulheres20 += 1
    idadetot += idade
print('Neste grupo temos os seguintes dados:\nA média de idade do grupo é {}\nO nome do homem mais velho é {} e tem {} anos\nTem {} mulheres abaixo de 20 anos'.format(idadetot/4, homemvelho, idadehv, mulheres20))
