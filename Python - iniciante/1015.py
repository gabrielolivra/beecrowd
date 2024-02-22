import math
valor_x = [float(x) for x in input().split()]
valor_y = [float(y) for y in input().split()]
x1 = valor_x[0]
y1 = valor_x[1]
x2 = valor_y[0]
y2 = valor_y[1]
distancia = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
print(f"{distancia:.4f}"