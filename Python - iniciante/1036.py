valores = input().split()
a, b, c = map(float, valores)
delta = b*b-4*a*c
delta_r = delta ** 0.5
if a == 0.0 or delta < 0.0:
    print('Impossivel calcular')
else:
    x1 = ((- b + delta_r) / (2 * a))
    x2 = ((- b - delta_r) / (2 * a))
    print('R1 = 'f'{x1:.5f}')
    print('R2 = 'f'{x2:.5f}')