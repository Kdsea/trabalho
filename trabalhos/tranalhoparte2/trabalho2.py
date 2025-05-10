print('-'*7, 'Bem-Vindo a Loja do Kauã de Souza', '-'*8)
print('-'*50)
print('-'*20, 'CARDÁPIO', '-'*20)
print('-'*50)
print('---|  Tamanho  |  Cupuaçu (CP)  |  Açaí  (AC) |---')
print('---|     P     |    R$ 9.00     |   R$ 11.00  |---')
print('---|     M     |    R$ 14.00    |   R$ 16.00  |---')
print('---|     G     |    R$ 18.00    |   R$ 20.00  |---')
print('-'*50)

#dicionario que contem todas a informações necessárias
sabores = {
    'CP': {'nome': 'Cupuaçu', 'P': 9.00, 'M': 14.00, 'G': 18.00},
    'AC': {'nome': 'Açaí', 'P': 11.00, 'M': 16.00, 'G': 20.00}
}

preco_total = 0 #variavel que contem o preço total que é chamado no final da compra


#bloco de codigo para repetição caso o usuario digite algo errado
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ').upper()
    while sabor not in sabores:
        print('Sabor inválido. Tente novamente.\n')
        sabor = input('Entre com o sabor desejado (CP/AC): ').upper()

    tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
    while tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente.\n')
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()

    preco = sabores[sabor][tamanho]
    preco_total += preco

    #mostra o pedido atual
    print(f"Você pediu um {sabores[sabor]['nome']} tamanho {tamanho}: R$ {preco:.2f}")

    continuar = input('\nDeseja mais alguma coisa? (S/N): ').upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja mais alguma coisa? (S/N): ').upper()
    if continuar == 'N': #se escrever N ele sai do loop e continua o codigo
        break

#mostra o pedido final com alteração no valor caso o usuario peça mais alguma coisa
print(f"\nValor total a pagar: R$ {preco_total:.2f}")
