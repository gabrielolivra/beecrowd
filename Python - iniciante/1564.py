while True:
    try:
        l = int(input())
        if l == 0:
            print('vai ter copa!')
        elif l > 0:
            print('vai ter duas!')
    except EOFError:
        break