valor1 = input().lower()

if valor1 == 'vertebrado':
    valor2 = input().lower()
    
    if valor2 =='ave':
        valor3 = input().lower()
        
        if valor3 == 'carnivoro':
            print('aguia')
        elif valor3 =='onivoro':
            print('pomba')
            
    elif valor2 == 'mamifero':
        valor3 = input().lower()
        if valor3 =='onivoro':
            print('homem')
            
        elif valor3 == 'herbivoro':
            print('vaca')   
            
elif valor1 == 'invertebrado':
    valor2 = input().lower()
    
    if valor2 =='inseto':
        valor3 = input().lower()
        if valor3 =='hematofago':
            print('pulga')
        
        elif valor3 =='herbivoro':
            print('lagarta')
            
    elif valor2 == 'anelideo':
        valor3 = input().lower()
        
        if valor3 == 'hematofago':
            print('sanguessuga')
            
        elif valor3 == 'onivoro':
            print('minhoca')