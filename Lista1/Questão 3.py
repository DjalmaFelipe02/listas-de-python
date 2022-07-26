at = int(input('Digite o ano em que você está: '))
an = int(input('Digite o ano em que você nasceu: '))

idade = at - an

if idade >= 18:
    print('Você está apto para votar')
else :
    print('Você não está apto para votar')
