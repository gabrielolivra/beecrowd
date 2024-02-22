while True:
    try:
        valor = input().split()
        if int(valor[0]) > int(valor[1]):
            print('Decrescente')
        elif int(valor[0]) < int(valor[1]):
            print('Crescente')
        elif valor[0] == valor[1]:
            break
    except EOFError:
        break