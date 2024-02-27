alcool = 0
gasolina = 0
disel = 0
while True:
    valor = int(input())
    if valor == 1:
        alcool+=1
    elif valor == 2:
        gasolina+=1
    elif valor == 3:
        disel +=1
    elif valor == 4:
        break
print('MUITO OBRIGADO')
print('Alcool:', alcool)
print('Gasolina:', gasolina)
print('Diesel:', disel)