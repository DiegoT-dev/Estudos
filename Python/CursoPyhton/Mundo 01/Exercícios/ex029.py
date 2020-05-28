vl = float(input('A que velocidade se encontra o carro? '))
if vl > 80:
    print('Ele está acima da velocidade!!!\nVocê será MULTADO.\nO valor a ser cobrado na multa é de R${:.2f}.'.format((vl-80)*7))
else:
    print('Velocidade aceita nesta via.\nTenha uma boa Viajem!')
