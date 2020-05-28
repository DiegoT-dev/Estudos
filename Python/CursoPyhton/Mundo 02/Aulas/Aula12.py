# Condiçõe aninhadas
# if ---- elif ----else
nome = str(input('Diga seu nome: ')).capitalize()
if nome == 'Diego':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome =='Maria' or nome == 'Paulo':
    print('Seu nome é bem pupular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('É um belo nome feminino!')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia {}!'.format(nome))
