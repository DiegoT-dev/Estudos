n = c = s =0
print('Digite \033[1:31m999\033[m para parar de somar e contar')
while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        c += 1
        s += n
print('Você digitou {} números e a soma entre eles é {}.'.format(c, s))
