n = 1
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

while n > 0:
    n = int(input("Digite um Número:"))
    
    if n >= 0 and n <= 25:
        cont1 = cont1 + 1
        
    elif n >= 26 and n <= 50:
        cont2 = cont2 + 1
        
    elif n >= 51 and n <= 75:
        cont3 = cont3 + 1
        
    elif n >= 76 and n <= 100:
        cont4 = cont4 + 1

print("A quantidade de números entre 0 e 25 é:",cont1,)
print("A quantidade de números entre 26 e 50 é:",cont2,)
print("A quantidade de números entre 51 e 75 é:",cont3,)
print("A quantidade de números entre 76 e 100 é:",cont4,) 
