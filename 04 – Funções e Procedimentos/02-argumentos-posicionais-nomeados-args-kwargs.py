# Argumento Posicional
def cadastrar_produto2(
    nome:str,
    preco: float,
    estoque: int
) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque} unidades")

# cadastrar_produto2("Teclado", 150.0, 20)
# Teclado -> nome
# 150.0 -> preco
# 20 -> estoque

# Argumento Nomeado
# cadastrar_produto2(
#     "Mouse",      
#     200.50, 
#     estoque=50    
# )

# Parâmetros com valores padrão


# *args
def calcular_total_modo_raiz(
    valor1: float,
    valor2: float,
    valor3: float
) -> float:
    return valor1 + valor2 + valor3

total = calcular_total_modo_raiz(89.90, 200.0, 510.0)
# print(total)

def calcular_total(*valores: float) -> float:
    # print(valores)
    return sum(valores)

total2 = calcular_total(89.90, 200.0, 510.0, 731.21, 922.2)
# print(total2)

def mostrar_produtos(*produtos: str) -> None:
    print(produtos)

# mostrar_produtos("Teclado", "Fone de Ouvido", "Mouse")

def calcular_total_pedido(*valores: float) -> float:
    # total = 0
    # print(valores)
    # for valor in valores:
    #     total += valor
        
    return sum(valores)

total3 = calcular_total_pedido(
    120.0,
    89.90,
    45.50,
    199.90,
    491.34
)

# print(f"Total do pedido: R${total:.2f}")

# Parâmetros Normais + *args
def registrar_pedido(
    numero_pedido: int,
    *produtos: str
) -> None:
    print(f"Pedido #{numero_pedido}")
    
    for produto in produtos:
        print(f"- {produto}")
        
# registrar_pedido(
#     1025,
#     "Notebook",
#     "Mouse",
#     "Fone de ouvido"
# )

# **kwargs
def cadastrar_cliente(**dados) -> None:
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    
# cadastrar_cliente(
#     nome="Luiza",
#     email="luiza@élegal.com",
#     cidade="Recife"
# )

# Parâmetros normais + **kwargs
def cadastrar_cliente2(
    nome: str,
    email: str,
    **dados_adicionais
) -> None:
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    
    for k, v in dados_adicionais.items():
        print(f"{k.capitalize()}: {v.capitalize()}")
        
# cadastrar_cliente2(
#     nome="Luiza",
#     email="luiza@élegal.com",
#     cidade="Recife",
#     estado="Pernambuco",
#     profissao="Engenheira de Dados"
# )

# *args e **kwargs juntos
def registrar_venda(
    cliente: str,
    *produtos: str,
    **dados_adicionais
) -> None:
    print(f"Cliente: {cliente}")
    
    print("\nProdutos")
    for produto in produtos:
        print(f"- {produto.capitalize()}")
        
    print("\nInformações da Venda")
    for k, v in dados_adicionais.items():
        print(f"{k.capitalize()}: {v}")
        
# registrar_venda(
#     "Luiza",
#     "Notebook",
#     "Telefone",
#     "Mouse",
#     forma_pagamento="pix",
#     vendedor="Caio",
#     entrega=True
# )

# Unpacking (desempacotar) com *
def cadastrar_produto(
    nome: str,
    preco: float,
    estoque: int = 0,
    # ativo: bool = True
) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque}")
    #print(f"Ativo: {ativo}")
    
# cadastrar_produto("Fone de Ouvido", 300.0, estoque=50)
produto = ["Teclado", 4500.0, 120]
produto2 = ("Notebook", 5000.0, 3)
# cadastrar_produto(
#     produto[0],
#     produto[1],
#     produto[2]
# )
cadastrar_produto(*produto)
cadastrar_produto2(*produto2)

# Unpacking (desempacotar) com **
cadastrar_produto2(
    nome="Mouse",
    preco=300.0,
    estoque=8
)
produto3 = {
    "nome": "Mouse",
    "preco": 300.0,
    "estoque": 8
}
cadastrar_produto2(**produto3)

# * -> desempacota como argumentos POSICIONAIS (tupla)
# ** -> desempacota como argumentos NOMEADOS (dicionário)

"""
def funcao(*args)
* está recebendo (tupla)

def funcao(**kwargs)
** estão recebendo (dicionário)

funcao(*lista)
* está desempacotando

funcao(**dicionario)
** estão desempacotando
Precisamos que as chaves do dicionário sejam correspondentes aos parâmetros
"""

# / - Parâmetros somente POSICIONAIS (tudo a esquerda)
def calcular_desconto(
    preco: float,
    desconto: float,
    / # Tudo que aparece antes da / deve ser passado como um argumento posicional
) -> float:
    return preco - (preco * desconto)

calcular_desconto(500, 0.10)
#calcular_desconto(preco=500, desconto=0.10)
#calcular_desconto(500, desconto=0.10)

def registrar_venda2(
    codigo: int,
    /,
    cliente: str
) -> None:
    print(codigo)
    print(cliente)
    
registrar_venda2(500, "Luiza")
registrar_venda2(500, cliente="Luiza")

# * - Parâmetros somentos NOMEADOS (tudo a direita)
def exportar_relatorio(
    nome_arq: str,
    *,
    incluir_cabecalho: bool,
    compactar: bool
) -> None:
    print(nome_arq)
    print(incluir_cabecalho)
    print(compactar)
    
exportar_relatorio("vendas.csv", incluir_cabecalho=True, compactar=True)
# Atenção: esse * não é o *args
def funcao(*args):
    pass

def funcao(a, *, b): 
    ...
    
# / e * juntos
def processar_pagamento(
    numero_pedido: int, # ARG. POSICIONAL
    valor: float,       # ARG. POSICIONAL
    /, # / -> separador que indica que tudo a esquerda deve ser passado como um argumento POSICIONAL
    forma_pagamento: str, # ARG. TANTO PODE SER POSICIONAL QUANTO NOMEADO
    *, # * -> separador que indica que tudo a direita deve ser passado como um argumento NOMEADO
    enviar_comprovante: bool = True # ARG. NOMEADO
) -> None:
    print(f"Pedido: {numero_pedido}")
    print(f"Valor: R$ {valor:.2f}")
    print(f"Pagamento: {forma_pagamento}")
    print(f"Enviar comprovante: {enviar_comprovante}")
    
processar_pagamento(
    1050,
    500,
    "Pix",
    enviar_comprovante=True
)

def funcao(
    a, # ARG. POSICIONAL
    b, # ARG. POSICIONAL
    /, # SEPARADOR (TUDO A ESQUERDA É UM ARGUMENTO OBRIGATÓRIAMENTE POSICIONAL)
    c, # RECEBE ARG. POSICIONAL OU NOMEADO
    d, # RECEBE ARG. POSICIONAL OU NOMEADO
    *args, # RECEBE ARG. POSICIONAL EXTRA (EMPACOTA NUMA TUPLA)
    e, # COMO O *ARGS JÁ CAPTURA OS ARGUMENTOS POSICIONAIS QUE SOBRAREM, O PARÂMETRO e E f FICA SENDO OBRIGATORIAMENTE COMO ARGUMENTOS NOMEADODS
    f,
    **kwargs # NOMEADOS RESTANTES (QUE VAO SER EMPACOTADOS COMO UM DICIONÁRIO)
):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("args:", args)
    print("e:", e)
    print("f:", f)
    print("kwargs:", kwargs)


funcao(
    1,
    2,
    3,
    4,
    5,
    6,
    e=7,
    f=8,
    nome="Lu",
    idade=20
)