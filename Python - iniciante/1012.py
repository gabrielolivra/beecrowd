A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

pi= 3.14159

a_triangulo= (A*C)/2
a_circulo= pi*C**2
a_trapezio=((A+B)*C)/2
a_quadrado= B*B
a_retangulo= A*B

print("TRIANGULO: {:.3f}".format(a_triangulo))
print("CIRCULO: {:.3f}".format(a_circulo))
print("TRAPEZIO: {:.3f}".format(a_trapezio))
print("QUADRADO: {:.3f}".format(a_quadrado))
print("RETANGULO: {:.3f}".format(a_retangulo))