#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = () #aqui criamos uma tupla vazia

while True:
    Pnome = str(input('digite o nume do produto: ')) #pedimos o nome do produto
    Ppreço = float(input('digite o valor do produto:R$ ')) #pedimos o preço do produto

    produtos = produtos + (Pnome, Ppreço,) #adicionamos os valores digitados na tupla

    continuar = str(input('gostaria de continuar [SIM/NAO]: ')).strip().upper()[0] #opção para saida do laço
    if continuar not in 'S': #condição para parar o laço infinito
        break #comando para saida do laço

print('------------ TABELA DE PREÇOS ------------')

for n in range(0,len(produtos)):
    if n%2 == 0:
        print(f'{produtos[n]:.<30}',end=' ')
    elif n%2 == 1:
        print(f'R${produtos[n]}')

print('------------------------------------------')