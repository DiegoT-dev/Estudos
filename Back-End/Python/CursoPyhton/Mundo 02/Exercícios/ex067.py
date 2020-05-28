while True:
    n = int(input('Quer ver a Tabuada de que valor? '))
    print('~' * 40)
    if n < 0:
        break
    else:
        c = 1
        while c != 11:
            print(f'{n:02} x {c:02} = {n*c:02}')
            c += 1
        print('~'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
