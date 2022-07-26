conti = True
values = []
positivos = []
negativos = []
while conti == True:
    value = int(input('Digite um número:'))
    values.append(value)
    continuar = input('Deseja inserir mais um novo valor? ' )
    if continuar != 's':
        conti = False
        break

media = sum(values)/len(values)

for n in values:
    if n > 0:
        positivos.append(n)
    elif n < 0:
        negativos.append(n)

porcentagem_positivos = (len(positivos)) / len(values) * 100
porcentagem_negativos =  (len(negativos)) / len(values)*100 

print('Positivos:',len(positivos))
print('Negativos:',len(negativos))
print('Porcentagem dos números negativos:',porcentagem_negativos)
print('Porcentagem dos números positivos:',porcentagem_positivos)
print('Média dos valores digitados:',media)
