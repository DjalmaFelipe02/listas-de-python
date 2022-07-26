cont = 0
maior = 0
menor = 0

for h in range(15):
    idade = float(input('Digite sua altura: '))
    cont = cont + 1

    if cont == 1:
       maior = idade
       menor = idade
       
    elif idade > maior:
            maior = idade
            
    elif idade < menor:
            menor = idade       


print('O MAIOR idade digitada foi:',maior)
print('O MENOR idade digitada foi:',menor)
