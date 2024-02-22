valor = float(input())

if (valor>=0 and valor<= 400.00):
	p_r= valor*0.15
	total=valor+p_r
	porcentagem=15
  
elif(valor>=400.01 and valor<=800.00):
	p_r=valor*0.12
	total=valor+p_r
	porcentagem=12
  
elif(valor>=800.01 and valor<=1200.00):
    p_r=valor*0.1
    total=valor+p_r
    porcentagem=10
  
elif(valor>=1200.01 and valor<=2000.00):
	p_r=valor*0.07
	total=valor+p_r
	porcentagem=7
  
elif(valor>2000.00):
 p_r=valor*0.04
 total=valor+p_r
 porcentagem= 4

print("Novo salario: {:.2f}".format(total))
print("Reajuste ganho: {:.2f}".format(p_r))
print("Em percentual:",porcentagem,"%")