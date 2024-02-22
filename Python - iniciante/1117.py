contador_media = 0
lista_media = []
while contador_media != 2:
    valor_media = float(input())
    if valor_media >=0 and valor_media <= 10:
        contador_media +=1
        lista_media.append(valor_media)
    else:
        print('nota invalida')
media = sum(lista_media)/2
print('media =',media)  
    