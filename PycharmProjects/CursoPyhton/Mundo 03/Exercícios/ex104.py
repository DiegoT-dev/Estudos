def leiaInt(x):
    n = input(x).strip()
    while True:
        if n.isnumeric():
            break
        else:
            print('\033[0:31mERRO! Digite apenas números.\033[m')
            n = input(x)
    return n


n = leiaInt('Digite um número: ')
print(f'{n} é um número.')