cab = ' Conversor de Medídas '
print('='*60)
print('{:=^60}'.format(cab))
print('='*60)
m = float(input('\nDigite a metragem a ser convertida: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('='*60)
print('A Tabela de Conversão para a metragem digitada é:')
print('='*60)
print('{}km \n{}hm \n{}dam \n{}m \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(km, hm, dam, m, dm,cm, mm))