exp = list(str(input('Digite sua expressão: ')).strip())
pilha = list()
'''msg = str('Sua expressão é válida!')
tot = totr = len(exp)
for c in range(0, len(exp)):
    if ' ' in exp:
        exp.remove(' ')
if exp.count('(') != exp.count(')'):
    msg = str('Sua expressão está errada')
else:
    for c in range(0, tot):
        if exp[c] == '(':
            for f in range(tot-1, c, -1):
                if exp[f] == ')':
                    tot -= 1
                    msg = str('Sua expressão é válida!')
                    break
                else:
                    msg = str('Sua expressão está errada!')
print(msg)'''
for c in exp:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(c)
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
