# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ()
while True:
    palavra = str(input('digite uma palavra: '))
    escolha = str(input('que parar [SIM/NAO] ?: ')).strip().upper()[0]

    tupla = tupla + (palavra,)
    if escolha not in 'SIMNAO':
        nescolha = ' '
        while nescolha not in ('SIMNAO'):
            nescolha = str(input('escolha invalida, quer parar [SIM/NAO] ?: ')).strip().upper()[0]

        if nescolha in 'SIM':
            break
    if escolha in 'SIM':
        break
print('-'*40)
print(f'{"CAÇA VOGAIS":^40}')
print('-'*40)
vogais = 'AaEeIiOoUu'
for p in tupla:
    print(f'\n{p.upper()} possui as vogais: ', end=' ')
    for letra  in p:
        if letra in vogais :
            print(f' {letra}',end=' ')


