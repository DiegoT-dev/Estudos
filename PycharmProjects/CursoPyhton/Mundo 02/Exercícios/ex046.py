from time import sleep
from emoji import emojize
print('-='*20)
print('{:^39}'.format('Contagem Regressiva'))
print('-='*20)
contagem = str(input('\033[1:33m{:^40}\033[m'.format('PRESSIONE ENTER PARA COMEÇAR'))).strip()
if contagem == '':
    for c in range(10, -1, -1):
        print('{:-^39}'.format(c))
        sleep(1)
    print(emojize('\n\033[31m{}\033[m'.format(':fireworks:'*22, use_aliases=True)*5))
