palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for c in palavras:
    print(f'\nNa palavra \033[1:31m{c.upper()}\033[m temos as vogais: ', end='')
    for v in c:
        if v in 'aeiou':
            print(f'\033[1:30m{v}\033[m', end=' ')
