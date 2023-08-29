#programa que vai gerar 5 numeros aleatorios e colocalos em uma tupla depois disso, mostre a listagem
#de numeros gerados e tambem indique o menor valor e o maior valor que estão na tupla

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10),)

print('os numeros sorteados foram: ')
maior = 0
menor = 0
cont = 0
for n in numeros:
    print(f'{n}',end='  ')

    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont = cont + 1

print(f'\no maor numerfoi {maior} e o menor foi {menor}')

#tambem pode ser feito dessa forma para determinar o maior e o menor
# print(f'o maior numero é {max(numeros)}
# print(f'o menor numero é {min(numeros)}