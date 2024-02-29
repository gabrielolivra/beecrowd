def jogo(first, num1, num2):
    if first == '0':
        if (num1 + num2)%2 == 0:
            return 'Jogador 2'
        else:
            return 'Jogador 1'
    else:
        if (num1 + num2)%2 == 0:
            return 'Jogador 1'
        else:
            return 'Jogador 2'
         
entrada = input().split()
primeiro = entrada[0]
jogador1 = int(entrada[1])
jogador2 = int(entrada[2])
roubou = entrada[3]
mentiu = entrada[4]
if roubou == '1' and mentiu == '0':
    print('Jogador 1 ganha!')
elif roubou == '1' and mentiu == '1':
    print('Jogador 2 ganha!')
elif roubou == '0' and mentiu == '1':
    print('Jogador 1 ganha!')
else:
    resultado = jogo(primeiro, jogador1, jogador2)
    print(resultado, 'ganha!')