m = float(input('Digite o número de maças: '))

if m >= 12:
    p1 = m*1
    print('O preço ficará R$',p1)
elif m < 12:
    p2 = m*1.30
    print('O preço ficará R$',p2)
    
