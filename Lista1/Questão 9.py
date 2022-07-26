com = input('Tipo de combustível: ')
li = int(input('Quantos litros de combustível: '))

if com == 'Álcool' or 'alcool' and li <= 20 :
     d1 = (li*0.90)*3/100
     v1 = (li*0.90)-d1
     print('O preço do Álcool será de R$',v1)

elif com == 'Álcool'or 'alcool' and li > 20 :
     d2 = (li*0.90)*5/100
     v2 = (li*0.90)-d2
     print('O preço do Álcool será de R$',v2)

elif com == 'Gasolina' or 'gasolina' and li <= 20 :
     d3 = (li*1.20)*4/100
     v3 = (li*1.20)-d3
     print('O preço da Gasolina será de R$',v3)
     
elif com == 'Gasolina' or 'gasolina' and li > 20 :
    d4 = (li*1.20)*6/100
    v4 = (li*1.20)-d4
    print('O preço da Gasolina será de R$',v4)

else:
     print('Combustível não identificado')    
