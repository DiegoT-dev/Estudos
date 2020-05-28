ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze',
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        pos = int(input('Digite um número de 0 a 20: '))
        if pos >= 0 and pos <= 20:
            break
    print(f'Você digitou o número {ext[pos]}')
    while True:
        perg = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if perg in 'SN':
            break
    if perg == 'N':
        break
print('Programa terminado!')
