b = int(input())
g = int(input())

if g %2!=0:
    new_g = g-1
    qtd_g = new_g/2
    r = qtd_g - b
    if r == 0:
        print('Amelia tem todas bolinhas!')
    else:
        if r > 0:
            print(f'Faltam {r:.0f} bolinha(s)')
        else:
            print('Amelia tem todas bolinhas!')
else:
    qtd_g = g/2
    r = qtd_g - b
    if r == 0:
        print('Amelia tem todas bolinhas!')
        
    else:
        if r > 0:
            print(f'Faltam {r:.0f} bolinha(s)')
        else:
            print('Amelia tem todas bolinhas!')