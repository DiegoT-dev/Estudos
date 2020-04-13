def escreva(txt):
    n = len(txt)+4
    print(f'{"~"*n}')
    print(f'  {txt} ')
    print(f'{"~"*n}')
    print()


while True:
    msg = str(input('Frase para cabeçalho: ')).strip()
    escreva(msg)
    p = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if p == 'N':
        break
