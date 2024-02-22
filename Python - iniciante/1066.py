valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())
valor5 = int(input())
lista_valor = [valor1, valor2, valor3, valor4, valor5]
par = 0
impar = 0
positivo = 0
negativo = 0
for valor in lista_valor:
    if valor > 0:
        positivo+=1
    elif valor < 0:
        negativo+=1    
    if valor %2 == 0:
        par +=1
    else:
        impar +=1  
print(par, 'valor(es) par(es)')
print(impar, 'valor(es) impar(es)')
print(positivo, 'valor(es) positivo(s)')
print(negativo, 'valor(es) negativo(s)')