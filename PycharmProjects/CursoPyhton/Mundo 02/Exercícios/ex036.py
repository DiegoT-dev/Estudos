from time import sleep
print('\033[1:30:47m-=\033[m'*20)
print('\033[1:37:40m<'*11,'\033[1:34:40mTeste Financeiro','\033[1:37:40m>\033[m'*11)
print('\033[1:30:47m-=\033[m'*20)
valor = float(input('Qual o valor pretendido da casa: R$'))
sal = float(input('Qual é o seu salário: R$'))
anos = int(input('Em quantos anos você pretende finaciar o imóvel? '))
sleep(.5)
print('Verificando....')
sleep(1)
if anos > 0:
    prest = valor/(anos*12)
else:
    prest = 0
if prest == 0:
    print('Você escolheu pagar o imóvel a vista!')
elif prest > ((sal*30)/100):
    print('\033[1:31mSeu financiamento foi negado!\033[m')
    print('As parcelas ultrapassam 30% de sua renda me mensal!')
    print('Parcelas de {}x de R${:.2f}.'.format(anos*12, prest))
    print('Para financiar o imóvel escolha mais anos ou complemente sua renda...')
elif prest < ((sal*30)/100):
    print('\033[1:32mFinanciamento APROVADO\033[m')
    sleep(.5)
    print('Calculando Parcelas....')
    sleep(3)
    print('Você pagará R${:.2f} ao mês!'.format(prest))
