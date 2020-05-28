nome = str(input('Qual é o seu nome? ')).strip().capitalize()
if nome == 'Diego':
    print('Que nome lindo você tem!')
else:
    print('Que nome normalzinho....')
print('Tenha um bom dia, {}!'.format(nome.capitalize()))
