print("Bem-Vindo a Copiadora do Kauã de Souza")

#definindo função para deixar o terminal legivel com realces
def realce():
    print("__" * 20)

#chamando a função realce
realce()

preco_total = 0

escolha_servico = input('Entre com o tipo de serviço Desejado \n DIG - Digitalização\n ICO - '
                        'Impressão Colorida\n IPB - Impressão Preto Branco\n FOT - Fotocópia\n >> ').upper()

#bloco de repetição caso o usuario nao digite oque é pedido, ele ficara em um loop até que digite corretamente
while escolha_servico not in ['DIG', 'ICO', 'IPB', 'FOT']:
    print("Escolha inválida entre com o tipo de serviço novamente.\n")
    escolha_servico = input('Entre com o tipo de serviço Desejado \n DIG - Digitalização\n ICO - '
                            'Impressão Colorida\n IPB - Impressão Preto Branco\n FOT - Fotocópia\n >> ').upper()

#chamando a função realce
realce()

num_paginas = input("Entre com o numero de paginas: ")

while not num_paginas.isnumeric() or int(num_paginas) >= 20000:
    print("Não aceitamos tantas páginas de uma vez.")
    num_paginas = input("Entre com o numero de paginas: ")

# Convertendo para int o numero de paginas
try:
    num_paginas = int(num_paginas)
except ValueError:
    print("Erro ao converter número de páginas. Encerrando programa.")
    exit()

#chamando a função realce
realce()

#bloco para declarar um preço a escolha do serviço
if escolha_servico == 'DIG':
    preco = 1.10
elif escolha_servico == 'ICO':
    preco = 1.00
elif escolha_servico == 'IPB':
    preco = 0.40
elif escolha_servico == 'FOT':
    preco = 0.20

preco_total = preco * num_paginas

# Bloco que é feito o calculo do desconto
if num_paginas < 20:
    print(f"O total deu R${preco_total:.2f}")
else:
    if 20 <= num_paginas < 200:
        desconto = 0.15
        porcentagem = "15%"
    elif 200 <= num_paginas < 2000:
        desconto = 0.20
        porcentagem = "20%"
    elif 2000 <= num_paginas < 20000:
        desconto = 0.25
        porcentagem = "25%"

# Bloco para aplicar o desconto
try:
    preco_total_com_desconto = preco_total - (preco_total * desconto)
    print(f"O preço com desconto de {porcentagem} deu R${preco_total_com_desconto:.2f}")
except NameError:
    preco_total_com_desconto = preco_total
    print("Nenhum desconto aplicado.")

realce()

adc_servico = input("Deseja algum serviço?\n "
                    "1 - Encadernação Simples - R$ 15.00\n "
                    "2 - Encadernação Capa Dura - R$40.00\n "
                    "0 - Não Desejo mais nada.\n"
                    ">> ")

while adc_servico not in ["0", "1", "2"]:
    print("Você não digitou um número válido.")
    adc_servico = input("Deseja algum serviço?\n "
                        "1 - Encadernação Simples - R$ 15.00\n "
                        "2 - Encadernação Capa Dura - R$40.00\n "
                        "0 - Não Desejo mais nada.\n"
                        ">> ")

if adc_servico == "1":
    preco_total_com_desconto += 15
elif adc_servico == "2":
    preco_total_com_desconto += 40


#print que mostra o total do pedido
print(f"Total: R${preco_total_com_desconto:.2f} "
    f"(serviço: R${preco:.2f} * páginas: {num_paginas} + extra)")

