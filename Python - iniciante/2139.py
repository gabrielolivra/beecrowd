calendario = [
    ('1', 31),
    ('2', 29),
    ('3', 31),
    ('4', 30),
    ('5', 31),
    ('6', 30),
    ('7', 31),
    ('8', 31),
    ('9', 30),
    ('10', 31),
    ('11', 30),
    ('12', 31) 
]
while True:
    try:
        entrada = input().split()
        qtd_dias = 0
        if entrada[0] == '12':
            if entrada[1] == '24':
                print('E vespera de natal!')
            elif entrada[1] == '25':
                print('E natal!')
            else:
                print('Ja passou!')
        else:
            for i in range(int(entrada[0]),12+1 ):
                for chave, valor in calendario:
                    if i == int(chave):
                        qtd_dias+= valor
            print('Faltam',(qtd_dias- int(entrada[1]))-6,'dias para o natal!')
    except EOFError:
        break