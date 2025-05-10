print('Bem Vindo a Loja do Kaua De Souza')

valor = int(input('Entre com o valor do produto: ')) #Função INPUT para receber um valor do usuario
quantidade = int(input('Entre com a quantidade do produto: '))

valor_total = valor * quantidade #Calculo para atribuir o valor total do produto a uma variavel

#Determina a porcentagem de desconto com base no valor total sem desconto
if valor_total < 2500:
    print("Voce não tem nenhum desconto")
    desconto = 0
elif 2500 <= valor_total <= 6000:
    print("Voce tem um desconto de 4%")
    desconto = 0.04
elif 6000 <= valor_total <= 10000:
    print("Voce tem um desconto de 7%")
    desconto = 0.07
else:
    print("Você tem um desconto de 11%")
    desconto = 0.11

valor_total_com_desconto = valor_total - (valor_total * desconto) #Calcula o valor total com desconto aplicado

print(f'Valor do produto SEM desconto: R${valor_total}') #Mostra o valor do produto SEM desconto na tela
print(f'Valor do produto COM desconto: R${valor_total_com_desconto}') #Mostra o valor do produto COM desconto na tela


