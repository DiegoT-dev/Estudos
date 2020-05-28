# Laço de repetição while com break
s = int()
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma dos números é igual a {}.'.format(s))
print(f'A soma vale {s}.')
