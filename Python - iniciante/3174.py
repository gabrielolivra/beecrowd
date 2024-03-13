info = []
qtd = int(input())
bonecos = 0
arquitetos = 0
musicos = 0
desenhistas = 0
for i in range(qtd):
    entrada = input().split()
    info.append([entrada[1], entrada[2]])
for k in info:
    if k[0] == 'bonecos':
        bonecos+=int(k[1])
    elif k[0] == 'arquitetos':
        arquitetos+=int(k[1])
    elif k[0] == 'musicos':
        musicos+=int(k[1])
    elif k[0] == 'desenhistas':
        desenhistas+=int(k[1])
resultado = (bonecos // 8) + (arquitetos // 4) + (musicos // 6) + (desenhistas // 12)
print(resultado)