from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano do primeiro registro: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratação'] + 35) - nasc
print('-='*40)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
