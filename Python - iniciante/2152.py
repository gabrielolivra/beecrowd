entrada = int(input())
for i in range(entrada):
    text = input().split()
    hora = text[0]
    min = text[1]
    if len(min) == 1:
        min = '0'+min
    status = text[2]
    if len(hora) == 2:
        if status =='1':
            print(f'{hora}:{min} - A porta abriu!')
        else:
            print(f'{hora}:{min} - A porta fechou!')
    else:
        if status =='1':
            print(f'0{hora}:{min} - A porta abriu!')
        else:
            print(f'0{hora}:{min} - A porta fechou!')
        
