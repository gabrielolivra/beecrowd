while True:
    parentese = 0
    try:
        entrada = input()
        for i in entrada:
            if i == '(':
                parentese += 1
            elif i == ')':
                parentese -= 1
            if parentese < 0:
                break
        if parentese == 0:
            print('correct')
        else:
            print('incorrect')
    except EOFError:
        break