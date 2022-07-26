conti = True
values = []
pares = []
impares = []

while conti == True:

    value = int(input('Digite um número:'))
    values.append(value)
    if value <= 0:
        conti = False
        break
    
media_geral = sum(values)/len(values)

for p in values:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)

media_pares = sum(pares)/len(pares)

print('Quantidade de números pares:', len(pares))
print('Quantidade de números ímpares:', len(impares))
print('Média dos valores pares:', media_pares)
print('Média Geral:', media_geral)




