from datetime import date
an = int(input('Qual o ano de nascimento do atleta? '))
aa = date.today().year
cat = aa - an
if cat <= 9:
    print('O atleta irá participar na categoria: \033[1:34mMIRIM\033[m.')
elif cat <= 14:
    print('O atleta irá participar da categoria: \033[1:34mINFANTIL\033[m.')
elif cat <= 19:
    print('O atleta irá participar da categoria: \033[1:34mJÚNIOR\033[m.')
elif cat <= 25:
    print('O atleta irá participar da categoria: \033[1:34mSÊNIOR\033[m.')
else:
    print('O atleta participara da categoria: \033[1:34mMASTER\033[m.')
