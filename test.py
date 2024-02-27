while True:
    try:
        entrada = input()
        h = int(entrada[0])
        min = int(entrada[2:4])
        if h < 7:
            print('Atraso maximmo:', 0)
        elif h >= 7 and h < 8:
            if min == 00:
                print('Atraso maximmo:', 0)
            else:
                print('Atraso maximo:', min)
    except EOFError:
        break
    