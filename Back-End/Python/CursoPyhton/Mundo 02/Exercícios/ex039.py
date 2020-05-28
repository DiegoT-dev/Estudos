from datetime import date
from time import sleep
an = int(input('Em que ano você nasce? '))
gen = str(input('Seu gênero? [\033[1:31mH\033[m] Homem / [\033[1:31mM\033[m] Mulher: ')).strip().capitalize()
aa = date.today().year
hoje = date.today()
limite = date(date.today().year, 6, 30)
restam = limite - hoje
if gen == 'M':
    print('Seu alistamento não é obrigatório')
    resp = str(input('Deseja se alistar mesmo assim? ')).strip().capitalize()[:1]
    if resp == 'N':
        print('Obrigado pela consulta....Terminando programa')
        sleep(1)
    else:
        if aa - an < 18:
            print('Você deverá se alistar no ano de {}.'.format(an + 18))
        elif aa - an == 18:
            print('Esse ano você pode se alistar.')
            print('Você tem {} dias para se alistar.'.format(restam.days))
            print('Procure a junta militar mais próxima!')
        elif aa - an == 18 and restam.days < 0:
            print('Você poderia se alistar esse ano...mas já perdeu o prazo')
        else:
            print('Você já tem mais de 18 anos...não pode mais se alistar!!!')
else:
    if aa - an < 18:
        print('Você obrigatoriamente deverá se alistar no ano de {}.'.format(an+18))
    elif aa - an == 18:
        print('Esse ano você deve se alistar.')
        print('Você tem {} dias para se alistar.'.format(restam.days))
        print('Procure a junta militar mais próxima!')
    elif aa - an == 18 and restam.days < 0:
        print('Você deveria se alistar esse ano...mas já perdeu o prazo')
    else:
        print('Você já tem mais de 18 anos...já deve ter se alistado!!!')
