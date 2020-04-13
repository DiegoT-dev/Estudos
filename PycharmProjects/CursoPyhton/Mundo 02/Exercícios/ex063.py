print('Sequência de Fibonacci')
n = int(input('Quantos termos você que mostrar da Sequência de Fibonacci? '))
fi = 0
pfi = 1
c = 0
while c < n:
    print(fi, end=' ')
    ufi = fi
    fi = pfi + ufi
    pfi = ufi
    c +=1
