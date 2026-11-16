############### ####### #################

# Exercício Final – Controle de Estoque da Loja
# Você está desenvolvendo um sistema simples para controlar o estoque de uma loja.
# Cada produto deve possuir:

# nome;
# categoria;
# preço;
# quantidade;
# valor em estoque;
# situação do estoque.

# Cada produto deverá ser armazenado em um dicionário, e todos os dicionários
# deverão ser armazenados em uma lista.

# 1. Calcular o valor em estoque
# Crie uma função chamada calcular_valor_estoque() que receba:

# preço do produto;
# quantidade em estoque.

# A função deve retornar o valor total do produto em estoque.

# 2. Classificar o estoque
# Crie uma função chamada classificar_estoque() que receba a quantidade e retorne:

# "Estoque baixo" se a quantidade for menor ou igual a 5;
# "Estoque normal" se a quantidade for maior que 5 e menor ou igual a 20;
# "Estoque alto" se a quantidade for maior que 20.


# 3. Exibir um produto
# Crie uma função chamada exibir_produto() que receba um produto e exiba algo como:

# Camisa Brasil | Vestuário | R$ 199.90 | 3 un. | Total: R$ 599.70 | Estoque baixo


# 4. Menu
# O programa deverá exibir o seguinte menu até que o usuário escolha a opção 6:

# 1 - Cadastrar produto
# 2 - Listar produtos
# 3 - Buscar produto
# 4 - Remover produto
# 5 - Resumo do estoque
# 6 - Sair

# Regras:

# Ao cadastrar, não permita nome ou categoria vazios.
# Ao listar, informe caso o estoque esteja vazio.
# Na busca, informe se o produto está ou não cadastrado.
# Ao remover, informe caso o produto não exista.


# 5. Resumo do estoque
# Ao escolher a opção 5, exiba:

# A quantidade de produtos cadastrados.
# A quantidade de categorias diferentes.
# O valor total do estoque.
# O produto com o maior valor em estoque.
# A média de preço dos produtos.
# Quantos produtos estão com estoque baixo.


# Requisitos:

# Utilize listas, dicionários e set.
# Utilize while para controlar o menu.
# Utilize for para percorrer os produtos.
# Utilize if, elif e else.
# Utilize try/except para validar o preço e a quantidade.
# Utilize len() para calcular a quantidade de produtos.
# Todas as funções devem possuir type hints e docstrings.
# calcular_valor_estoque() deve retornar float.
# classificar_estoque() deve retornar str.
# exibir_produto() deve retornar None.
# Os valores retornados pelas funções devem ser armazenados em variáveis e reutilizados.
# Não faça os cálculos de valor em estoque e classificação fora das funções.


#
# valor_estoque = calcular_valor_estoque(registro_quantidade,registro_preco)
# return valor_estoque


############## ###### ######################

######## Controle de Estoque da Loja ############


# 1
def calcular_valor_estoque(preco_produto: float, quantidade_estoque: int) -> float:
    """
        Calcula o valor do estoque
    Args:
        preco_produto: preço do produto
        quantidade_estoque:quantidade do produtos em estoque.
    Returns:
       Valor total do estoque
    """
    valor_estoque = preco_produto * quantidade_estoque
    return valor_estoque


# 2
def classificar_estoque(quantidade_estoque: int) -> str:
    """
    Classificação da quantidade de estoque
    Args:
    quantidade_estoque:quantidade do produtos em estoque.
    Returns:
    Classificação do nivel atual do estoque
    """
    if quantidade_estoque <= 5:
        classificacao = "Estoque baixo"
    elif quantidade_estoque <= 20:
        classificacao = "Estoque normal"
    else:
        classificacao = "Estoque alto"
    return classificacao


# 3
def exibir_produto(
    nome: str,
    categoria: str,
    preco_produto: float,
    quantidade_estoque: int,
    valor_estoque: float,
    classificacao: str,
) -> None:
    """
        Exibir dados do produto
    Args:
        nome: nome do produtos
        categoria:categoria do produto
        preco_produto: preço do produto,
        quantidade_estoque:quantidade do produtos em estoque.
        valor_estoque: valor do produto em estoque
        classificacao: classificação do estoque do produto
    """
    print(
        f"{nome} | {categoria} | R$ {preco_produto:.2f} | {quantidade_estoque} un. | Total: R$ {valor_estoque:.2f} | {classificacao}"
    )


# controle

lista_produtos = []

opcoes = [
    "1 - Cadastrar produto",
    "2 - Listar produtos",
    "3 - Buscar produto",
    "4 - Remover produto",
    "5 - Resumo do estoque",
    "6 - Sair",
]

print("\nSelecione uma das opções abaixo:")
for menu in opcoes:
    print(f" | {menu}")


while True:

    try:
        selecione_opcao = int(input("Selecione uma das opções: "))

        if selecione_opcao == 1:

            # Nome Produto
            while True:
                registro_nome_produto = (
                    input("Digite o nome do produto: ").strip().title()
                )
                if registro_nome_produto == "":
                    print("Nome vazio não pode ser cadastrado!")
                elif registro_nome_produto.isnumeric():
                    print("Erro! Digite apenas letras.")
                else:
                    break

            # Categoria Produto
            while True:
                registro_categoria = (
                    input("Digite a categoria do produto: ").strip().title()
                )
                if registro_categoria == "":
                    print("Categoria vazia não pode ser cadastrada!")
                elif registro_categoria.isnumeric():
                    print("Erro! Digite apenas letras.")
                else:
                    break

            # quantidade produto
            while True:
                try:
                    registro_quantidade = int(
                        input("Digite a quantidade de produtos no estoque: ")
                    )
                    if registro_quantidade >= 0:
                        break
                    else:
                        print("Erro! Digite número maior ou igual a zero.")
                except ValueError:
                    print("Erro! Digite um número válido.")

            # preco produto
            while True:
                try:
                    registro_preco = float(
                        input("Digite o preço de compra do produto: ")
                    )
                    if registro_preco >= 0:
                        break
                    else:
                        print("Erro! Digite número maior ou igual a zero.")
                except ValueError:
                    print("Erro! Digite um número válido.")

            # Guardar

            valor_estoque = calcular_valor_estoque(registro_preco, registro_quantidade)
            registro_classificacao = classificar_estoque(registro_quantidade)

            registro_produto = {
                "nome": registro_nome_produto,
                "categoria": registro_categoria,
                "quantidade": registro_quantidade,
                "preco": registro_preco,
                "situacao": registro_classificacao,
                "valor_estoque": valor_estoque,
            }
            lista_produtos.append(registro_produto)
            print("Sucesso! Cadastro do produto efetuado.")

        elif selecione_opcao == 2:

            quantidade_produtos = len(lista_produtos)

            if quantidade_produtos == 0:
                print("Aviso: O estoque está vazio")
            else:
                print(f"\nO estoque tem {quantidade_produtos} produtos cadastrados:\n")
                for registro_produto in lista_produtos:
                    exibir_produto(
                        registro_produto["nome"],
                        registro_produto["categoria"],
                        registro_produto["preco"],
                        registro_produto["quantidade"],
                        registro_produto["valor_estoque"],
                        registro_produto["situacao"],
                    )
        elif selecione_opcao == 3:
            produto_pesquisa = (
                input("Informe o nome do produto que deseja buscar: ").strip().title()
            )

            encontrado = False
            for registro_produto in lista_produtos:
                if registro_produto["nome"] == produto_pesquisa:
                    print("Produto encontrado:")
                    exibir_produto(
                        registro_produto["nome"],
                        registro_produto["categoria"],
                        registro_produto["preco"],
                        registro_produto["quantidade"],
                        registro_produto["valor_estoque"],
                        registro_produto["situacao"],
                    )
                    encontrado = True
                    break

            if not encontrado:
                print(f"Aviso: O produto {produto_pesquisa} não está cadastrado.")

        elif selecione_opcao == 4:
            produto_remover = (
                input("Informe o nome do produto que deseja remover: ").strip().title()
            )

            encontrado = False
            for registro_produto in lista_produtos:
                if registro_produto["nome"] == produto_remover:
                    lista_produtos.remove(registro_produto)
                    print(
                        f"Sucesso! O produto {produto_remover} foi removido do estoque."
                    )
                    encontrado = True
                    break

            if not encontrado:
                print(
                    f"Aviso: O produto {produto_remover} não foi encontrado no estoque."
                )

        elif selecione_opcao == 5:

            quantidade_produtos = len(lista_produtos)

            if quantidade_produtos == 0:
                print("Aviso: O estoque está vazio")
            else:
                # 1. começar os contadores
                valor_total = 0
                soma_precos = 0
                categorias = set()
                estoque_baixo = 0

                # 2. passar por cada produto somando
                for registro_produto in lista_produtos:
                    valor_total += registro_produto["valor_estoque"]
                    soma_precos += registro_produto["preco"]
                    categorias.add(registro_produto["categoria"])
                    if registro_produto["situacao"] == "Estoque baixo":
                        estoque_baixo += 1

                # 3. cálculos finais
                maior = max(
                    lista_produtos, key=lambda produto: produto["valor_estoque"]
                )
                media_precos = soma_precos / quantidade_produtos

                # 4. mostrar
                print("\n--- Resumo do estoque ---\n")
                print(f"Produtos cadastrados: {quantidade_produtos}")
                print(f"Categorias diferentes: {len(categorias)}")
                print(f"Valor total do estoque: R$ {valor_total:.2f}")
                print(
                    f"Maior valor em estoque: {maior['nome']} (R$ {maior['valor_estoque']:.2f})"
                )
                print(f"Média de preço: R$ {media_precos:.2f}")
                print(f"Produtos com estoque baixo: {estoque_baixo}")

        elif selecione_opcao == 6:
            print("\nCadastros finalizados ")
            break

        else:
            print("\nOpção inválida! Digite um número de 1 a 6.")
    except ValueError:
        print("\nOpção inválida! Digite um número de 1 a 6.")
