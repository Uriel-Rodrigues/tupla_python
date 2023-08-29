#programa que teha uma tupla preenchida por uma contagem por extenso  de zero a vinte, seu programa deve ler o numero pelo
#teclado e mostralo por extenso

numeros = ('zero','um','dois','tres','quatro',
           'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito','dezenove','vinte')

while True:
    n = int(input('digite um numero de 0 a 20 veja ele por extenso [999 para sair]: '))
    if n == 999:
        break
    print('- - - - - - - - - - - - NUMERO POR EXTENSO - - - - - - - - - - - -')
    print(f'o numero digitado foi {n} e por extenso se escreve',f'{numeros[n]}'.upper())
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print('programa - NUMERO POR EXTENSO - finalizado..... ')