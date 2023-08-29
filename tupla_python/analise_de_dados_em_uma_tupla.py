# programa que leia 4 valores pelo teclado guadios em uma tupla e no fim mostre
# quantas vezes apareceu o valor 9
# em que posição foi digitado o primeiro valor 3
# quais foram os numeros pares

numeros = (int(input('digite o numero [1]: ')),int(input('digite o numero [2]: ')),
        int(input('digite o numero [3]: ')),int(input('digite o numero [4]: ')))

print('-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'o numero 9 apareceu: {numeros.count(9)}x')
print('-=-=-=-=-=-=-=-=-=-=-=-=')
if 3 in numeros:
    print(f'o numero 3 foi digitado prela 1° vez na posição: {numeros.index(3)+1}º')
else:
    print('numero 3 nao encontrado')
print('-=-=-=-=-=-=-=-=-=-=-=-=')
print('os numeros pares foram: ',end=' ')
for n in numeros:
    if n%2 == 0:
        print(f'{n}',end=' ')

'''#USANDO O FOR PRA FAZER UMA TUPLA

num = ()
for n in range(1, 5):
    numeros = int(input(f'digite o [{n}]º para a tupla: '))

    num = num + (numeros,)

print(f'os numeros digitados foram: {num}')
print('-='*15)
print(f'o numero 9 apareceu {num.count(9)}')
print('-='*15)
print(f'o numero 3 foi digitado pela 1° vez na posição {num.index(3)}°')
print('-='*15)
print(f'os numeros pare digitados foram: ',end=' ')
for n in num:
    if n%2 == 0:
        print(f'{n}',end=' ')'''
