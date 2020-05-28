from datetime import date
meni = int(0)
maii = int(0)
for c in range(0,7):
    ano = int(input('Digite o ano de nascimento de uma pessoa: '))
    idade = date.today().year - ano
    if idade < 21:
        meni += 1
    else:
        maii += 1
print('Dos 7 anos digitados você tem:\n{:02} Pessoas Menores de idade\n{:02} Pessoas Maiores de idade'.format(meni, maii))
