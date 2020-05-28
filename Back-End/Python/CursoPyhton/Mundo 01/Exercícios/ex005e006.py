n = int(input('Digite um número: '))
an = n-1
s = n+1
md = n*2
mt = n*3
rq = n**(1/2)
print('Analisando o valor {0}, seu antecessor é {2} e o sucessor é {1}.'.format(n, s, an))
print('E o dobro de {0} é {1}, \nO triplo de {0} é {2} \nE a raiz quadrada de {0} é {3:.2f}.'.format(n, md, mt, rq))
