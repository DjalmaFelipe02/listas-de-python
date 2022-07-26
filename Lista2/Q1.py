impares_mult3 = []

for n in range(1,501,2):
    if n % 3 == 0:
        impares_mult3.append(n)
            

soma_impar_mult3 = sum(impares_mult3)

print('A soma de todos os valores ímpares múltiplos de 3 é:', soma_impar_mult3)
    
