jhon = input()
doc = input()
qtd_jhon = 1
qtd_doc = 1
for v1 in jhon:
    if v1 == 'a':
        qtd_jhon+=1
for v2 in doc:
    if v2 == 'a':
        qtd_doc+=1

if qtd_jhon >= qtd_doc:
    print('go')
else:
    print('no')
    