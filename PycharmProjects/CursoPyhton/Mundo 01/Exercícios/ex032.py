ano = int(input('Digite um ano para descobrir se ele é bissexto: '))
if ano%400 == 0:
    print('O ano {} {} Bissexto'.format(ano, 'é'if ano>=2020 else 'foi' ))
else:
    if ano%100 == 0:
        print('O ano {} não {} Bissexto.'.format(ano, 'é'if ano>=2020 else 'foi'))
    else:
        if ano%4 == 0:
            print('O ano {} {} Bissexto.'.format(ano, 'é'if ano>=2020 else 'foi'))
        else:
            print('O ano {} não {} Bissexto.'.format(ano, 'é'if ano>=2020 else 'foi'))
# Para analizar o ano da máquina
# Bibliote datetime módulo date
# = date.today().year
