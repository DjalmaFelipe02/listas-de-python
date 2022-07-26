a = float(input('Digite sua primeira nota:' ))
b = float(input('Digite sua segunda nota:' ))
c = float(input('Digite sua terceira nota:' ))

media_geral = (a+b+c)/3
media_aproveitamento = (a+b*2+c*3+media_geral)/7

if media_aproveitamento >= 9:
    print('Sua Média de Aproveitamento teve nota A')
elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:
    print('Sua Média de Aproveitamento teve nota B')
elif media_aproveitamento >= 6 and media_aproveitamento < 7.5:
    print('Sua Média de Aproveitamento teve nota C')
else :
    print('Sua Média de Aproveitamento teve nota D')
    
    
    
