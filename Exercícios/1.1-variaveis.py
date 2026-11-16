# Exercicios de variaveis

nome = "Luiza"  # str  — texto sempre entre aspas (duplas ou simples)
idade = 25  # int  — número inteiro
estado = "Pernambuco"  # # str  — texto sempre entre aspas (duplas ou simples)
tem_cachorro = True  # bool — True ou False (com maiúscula)
altura = 1.58  # float — número com ponto flutuante

print(nome)
print(idade)
print(estado)
print(tem_cachorro)
print(altura)

# REATRIBUIÇÃO
# ----------------------------------------------------------
# Variáveis podem ter seu valor trocado a qualquer momento
# A etiqueta agora aponta para outro valor (para outro objeto na memória que contêm o novo alor)

idade = 30
print(idade)  # 30

idade = 50
print(idade)  # 50

idade = "Luiza Vieira"  # "Luiza Vieira"
print(idade)

#----------
# Exercicios:
# Variáveis

print("__Exercio Complementar__")
cliente = "Camila"
doce = "brigadeiro"
preco = 2.50
quantidade = 4

# Cálculo
total = preco * quantidade

# Saída
print("Cliente:", cliente)
print("Produto:", doce)
print("Quantidade:", quantidade)
print("Preço unitário: R$", preco)
print("Total da compra: R$", total)


print("__Exercio Complementar Input__")

cliente = input("Digite seu nome: ")
doce = input("Digite o nome do doce: ")
preco = float(input("Digite o preço do doce: "))
quantidade = int(input("Digite a quantidade: "))

# Cálculo
total = preco * quantidade

# Saída
print("Cliente:", cliente)
print("Produto:", doce)
print("Quantidade:", quantidade)
print("Preço unitário: R$", preco)
print("Total da compra: R$", total)
