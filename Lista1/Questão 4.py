n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if n1>n3 and n2>n3 :
    print('A soma dos maiores valores será:' ,n1 + n2)
elif n1>n2 and n3>n2 :
    print('A soma dos maiores valores será:' ,n1 + n3)
elif n2>n1 and n3>n1 :
    print('A soma dos maiores valores será:' ,n2 + n3)
else:
    print('Todos os valores não podem ser iguais')
        
        
        
        
    
