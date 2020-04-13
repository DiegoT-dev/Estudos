from time import sleep
n = int(input('Digite um número qualquer: '))
print('Escolha agora a base de conversão para o número escolhido!')
print('[\033[1:34m1\033[m] - Binário')
print('[\033[1:34m2\033[m] - Octal')
print('[\033[1:34m3\033[m] - Hexadecimal')
escolha = int(input('Sua opção: '))
print('Convertendo...')
sleep(2)
if escolha == 1:
    print('O número {} convertindo em Binário é \033[1:35m{:2}\033[m'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('O número {} convertindo em Octal é \033[1:35m{}\033[m'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('O número {} convertindo em Hexadecimal é \033[1:35m{}\033[m'.format(n, hex(n)[2:]))
