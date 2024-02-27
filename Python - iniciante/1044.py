valor = input().split()
valor1 = int(valor[0])
valor2 = int(valor[1])
if valor1 > valor2:
    if valor1 % valor2 == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    if valor2 % valor1 == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
        