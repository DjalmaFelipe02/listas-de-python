f = input('Qual fruta você deseja: ')
kg = int(input('Quantos Kg você deseja: '))

if f == 'Morango' and kg <= 5 :
    v1 = kg*2
    print('O preço do Morango será de R$',v1)
elif f == 'Morango' and kg > 5 :
    if kg > 8:
        d1 = (kg*1.80)*10/100
        v2 = (kg*1.80)-d1
        print('O preço do Morango será de R$',v2)
    else :
        v3 = kg*1.80
        print('O preço do Morango será de R$',v3)
elif f == 'Maça' and kg <= 5 :
    v4 = kg*1.50
    print('O preço do Morango será de R$',v4)
elif f == 'Maça' and kg > 5 :
     if kg > 8 :
         d2 = (kg*1.10)*10/100
         v5 = (kg*1.10)-d2
         print('O preço do Morango será de R$',v5)
     else :
        v6 = kg*1.10
        print('O preço do Morango será de R$',v6)
        
        
    

