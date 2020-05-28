def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif 5 <= r['média'] < 7:
            r['situação'] = 'RAZOÁVEL'
        elif r['média'] < 5:
            r['situação'] = 'RUIM'
    return r

#Programa
resp = notas(8, 4, 8, 6.5, 7.8, 10, sit=True)
print(resp)
