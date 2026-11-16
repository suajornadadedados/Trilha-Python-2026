# PARTIDA

# Brasil x México

# Titulares:
# Alisson
# Marquinhos
# Gabriel Magalhães
# Bruno Guimarães
# Raphinha
# Rodrygo
# Vini Jr.

# Gols:
# Vini Jr.
# Rodrygo
# Vini Jr.

# México marcou 1 gol.
# """


# jogadores = [
#     "Alisson",
#     "Marquinhos",
#     "Gabriel Magalhães",
#     "Bruno Guimarães",
#     "Raphinha",
#     "Rodrygo",
#     "Vini Jr.",
# ]

# print(type(jogadores))
# print(jogadores)
# print(jogadores[0])
# print(jogadores[1])
# print(jogadores[2])
# print(jogadores[3])
# print(jogadores[-1])

# jogadores.append("Endrick")
# print(jogadores)
# print(jogadores[-1])

# jogadores[3] = "Neymar"
# print(jogadores)

# print("Jogadores do Brasil")

# ### USO DO FOR enumerando a posição####

# for i, jogador in enumerate(jogadores):
#     print(f" - {jogador} | Posição: {i}")


# ##
# autores_gols = [
#     "Vini Jr.",
#     "Rodrygo",
#     "Vini Jr.",
# ]

# quantidade_gols = len(autores_gols)
# print(quantidade_gols)

# # transformar lista en set - não repete


# jogadores_que_marcaram_gols = set(autores_gols)
# print(jogadores_que_marcaram_gols)
# quantidade_de_jogadores_que_marcaram_gols = len(jogadores_que_marcaram_gols)
# print(quantidade_de_jogadores_que_marcaram_gols)

##################################################
###### #### #### EXERCÍCIOS #### #### #### ####
##################################################
# """
# Exercício 1 — Cadastro de Figurinhas

# Você foi contratado para desenvolver um sistema simples para controlar um álbum de figurinhas da Copa do Mundo.

# O programa deve permitir que o usuário cadastre figurinhas até que ele digite a palavra "fim".

# Ao final, exiba:

# Todas as figurinhas cadastradas.
# A quantidade total de figurinhas.
# A primeira figurinha cadastrada.
# A última figurinha cadastrada.

# Desafio: não permita que o usuário cadastre uma figurinha vazia.
# """
# Precisie de ajuda do Claude #####

# Erro 1: a lista foiriada dentro do laço
# Erro 2: o for percorre as letras da palavra
# Erro 3: o enumerate final usa a variável errada- suei figurinha e ra era para usar album

# album_figurinhas = []  # criada uma vez, fora do laço

# while True:
#     figurinha = input(
#         "Digite o nome do jogador da sua figurinha ou escreva 'fim' para encerrar: "
#     ).strip()

#     if figurinha.lower() == "fim":
#         print("Cadastro de figurinhas encerrado")
#         break
#     elif figurinha == "":
#         print("Figurinha vazia não pode ser cadastrada!")
#     else:
#         album_figurinhas.append(figurinha)

# print("\nFigurinhas cadastradas:")
# for i, jogador in enumerate(album_figurinhas, start=1):
#     print(f" | Figurinha {i} - {jogador}")

# print(f"\nTotal de figurinhas: {len(album_figurinhas)}")

# if album_figurinhas:
#     print(f"Primeira figurinha: {album_figurinhas[0]}")
#     print(f"Última figurinha: {album_figurinhas[-1]}")


####################### fim  ##################################

# """
# Exercício 2 — Estatísticas da Partida

# Crie um programa que solicite ao usuário as seguintes informações de uma partida:

# Seleção mandante
# Seleção visitante
# Gols da seleção mandante
# Gols da seleção visitante

# Armazene essas informações em um dicionário.

# Depois:

# Exiba todas as informações utilizando um for com .items().
# Informe qual seleção venceu a partida.
# Caso os gols sejam iguais, informe que a partida terminou empatada.

# Desafio: utilize try/except para garantir que a quantidade de gols seja um
# número inteiro válido.
# """

# print("\nDigite os dados da partida solicitados abaixo:")

# mandante = input("Digite a Seleção mandante: ")
# visitante = input("Digite a Seleção visitante: ")

# while True:
#     try:
#         gols_mandante = int(input("Digite os gols da seleção mandante: "))
#         if gols_mandante >= 0:
#             print("Número inteiro válido cadastrado")
#             break
#         else:
#             print("Digite um número maior ou igual a 0")
#     except ValueError:
#         print("Digite um número inteiro válido, maior ou igual a 0")

# while True:
#     try:
#         gols_visitante = int(input("Digite os gols da seleção visitante: "))
#         if gols_visitante >= 0:
#             print("Número inteiro válido cadastrado")
#             break
#         else:
#             print("Digite um número maior ou igual a 0")
#     except ValueError:
#         print("Digite um número inteiro válido, maior ou igual a 0")

# partida = {
#     "mandante": mandante,
#     "visitante": visitante,
#     "gols_mandante": gols_mandante,
#     "gols_visitante": gols_visitante,
# }

# print("\nDados da partida:")

# for chave, valor in partida.items():
#     print(f" | {chave}: {valor}")

# print("\nResultado da Partida")

# if gols_mandante > gols_visitante:
#     resultado = f"Vitória do {mandante}"
# elif gols_mandante < gols_visitante:
#     resultado = f"Vitória do {visitante}"
# else:
#     resultado = "Partida terminou empatada"

# print(resultado)


################## FIM ################################

# Exercício 3 — Seleções Classificadas

# Durante a fase de grupos, várias seleções foram sendo classificadas.
# Peça ao usuário para informar o nome de 8 seleções.
# Armazene essas seleções em um set.
# Ao final:

# Exiba todas as seleções classificadas.
# Informe quantas seleções diferentes foram cadastradas.

# Depois pergunte ao usuário o nome de uma seleção e informe se ela está classificada utilizando o operador in.

# Desafio: explique por que, mesmo digitando uma seleção repetida, ela aparece apenas uma vez no conjunto.
# """

####### ######################################################
#######  TESTES QUSE CORRETOS MAS SEM VALIDAÇÃO DE QUANTIDADE DE SELEÇÕES ###3
# #################################################################################


# selecoes_classificadas = set()  # transformar em set
# print(selecoes_classificadas)

# while True:
#     try:
#         selecoes = (
#             input("Digite o nome de 8 seleções classificadas ou 'fim' para encerrar: ")
#             .strip()
#             .title()
#         )
#         if selecoes == "Fim":
#             print("Cadastro de seleções encerrado")
#             break

#         elif selecoes == "":
#             print("Seleção vazia não pode ser cadastrada!")
#             selecoes = (
#                 input("Digite o nome da seleção classificada ou 'fim' para encerrar: ")
#                 .strip()
#                 .title()
#             )
#         elif any(caractere.isdigit() for caractere in selecoes):
#             print("Não digite números.")
#             selecoes = (
#                 input("Digite o nome da seleção classificada ou 'fim' para encerrar: ")
#                 .strip()
#                 .title()
#             )

#         else:
#             print("Entrada válida.")
#             selecoes_classificadas.add(selecoes)

#     except TypeError:
#         print("Erro digite informação correta")
#         selecoes = (
#             input("Digite o nome da seleção classificada ou 'fim' para encerrar: ")
#             .strip()
#             .title()
#         )
# print("\nselecoes_classificadas:")
# print(selecoes_classificadas)
# print(type(selecoes_classificadas))

########### ############# CORRETO   #######################

# selecoes_classificadas = set()
# cadastros = 0  # conta as entradas válidas, inclusive as repetidas

# while cadastros < 8:
#     print("\nSeleções Classificadas:")
#     selecao = (
#         input(
#             f"Digite o nome de 8 seleções classificadas ou fim para encerrar - Cadastradas: {cadastros + 1} de 8 :  "
#         )
#         .strip()
#         .title()
#     )

#     if selecao == "Fim":
#         print("Cadastro de seleções encerrado")
#         break
#     elif selecao == "":
#         print("Seleção vazia não pode ser cadastrada!")
#     elif any(caractere.isdigit() for caractere in selecao):
#         print("Não digite números.")
#     else:
#         print("Entrada válida.")
#         selecoes_classificadas.add(selecao)
#         cadastros += 1

# print("\nSeleções classificadas:")
# for selecao in selecoes_classificadas:
#     print(f" | {selecao}")

# print(f"\nSeleções diferentes cadastradas: {len(selecoes_classificadas)}")

# print("\nPesquise se sua seleção foi classificada")
# busca_selecao = input("Digite o nome da seleção que deseja pesquisar: ").strip().title()

# if busca_selecao in selecoes_classificadas:
#     print("Seleção Classificada !!!")
# else:
#     print("Seleção Não Classificada")


# # Desafio: explique por que, mesmo digitando uma seleção repetida, ela aparece apenas uma vez no conjunto.
# # o Set (conjunto) não aceita repetidos


# Desafio: um set (conjunto) só guarda elementos únicos.
# Quando usamos .add() com um valor que já existe no conjunto,
# o Python verifica que ele já está lá e simplesmente não adiciona de novo.
# Por isso, se o usuário digitar "Brasil" duas vezes, ele aparece uma vez só,
# e len() conta apenas as seleções diferentes.


################## FIM ################################
############################################################

# """
# Exercício 4 — Menu do Álbum

# Desenvolva um programa que simule um álbum de figurinhas.

# Utilize uma lista para armazenar as figurinhas e exiba o seguinte menu:

# 1 - Adicionar figurinha
# 2 - Remover figurinha
# 3 - Buscar figurinha
# 4 - Mostrar álbum
# 5 - Encerrar

# O menu deve permanecer sendo exibido até que o usuário escolha a opção 5.

# Regras:

# Ao adicionar, a figurinha deve ser inserida no final da lista.
# Ao remover, informe caso a figurinha não exista.
# Na busca, informe se a figurinha está ou não no álbum.
# Ao mostrar o álbum, exiba todas as figurinhas utilizando um for.

# Desafio: utilize if, elif, else e while.
# """
#### incio        ###3

# album_figurinhas = []  # criada uma vez, fora do laço
# opcoes = {"Adicionar": 1, "Remover": 2, "Buscar": 3, "Mostrar": 4, "Encerrar": 5}
# opcoes2 = [
#     "1 - Adicionar figurinha",
#     "2 - Remover figurinha",
#     "3 - Buscar figurinha",
#     "4 - Mostrar álbum",
#     "5 - Encerrar",
# ]

# while True:

#     print("\nSelecione uma das opções abaixo:")
#     for opcoes in opcoes2:
#         print(f" | {opcoes}")

#     try:
#         selecione_opcao = int(input("Selecione uma das opções: "))

#         if selecione_opcao == 1:
#             adicionar_figurinha = input(
#                 "Digite o nome do jogador da sua figurinha: "
#             ).strip()

#             if adicionar_figurinha == "":
#                 print("Figurinha vazia não pode ser cadastrada!")
#             else:
#                 album_figurinhas.append(adicionar_figurinha)
#                 print(
#                     f"Sucesso! A figurinha {adicionar_figurinha} foi adicionada ao álbum"
#                 )

#         elif selecione_opcao == 2:
#             fig_remover = input(
#                 "Informe o nome da figurinha que deseja excluir do album de Figurinhas: "
#             ).strip()
#             if fig_remover in album_figurinhas:
#                 posicao = album_figurinhas.index(fig_remover) + 1
#                 album_figurinhas.remove(fig_remover)
#                 print(
#                     f"Sucesso! A figurinha {fig_remover} foi removida da posição {posicao}"
#                 )
#             else:
#                 print(f"Aviso: A figurinha {fig_remover}  não foi encontrada no album")

#         elif selecione_opcao == 3:
#             fig_pesquisa = input(
#                 "Informe o nome da figurinha que deseja buscar no album de Figurinhas: "
#             ).strip()
#             if fig_pesquisa in album_figurinhas:
#                 posicao = album_figurinhas.index(fig_pesquisa) + 1
#                 print(
#                     f"Sucesso! A figurinha {fig_pesquisa} foi encontrada na posição {posicao}"
#                 )
#             else:
#                 print(
#                     f"Aviso: A figurinha  {fig_pesquisa} pesquisada não foi encontrada no album"
#                 )

#         elif selecione_opcao == 4:
#             quantidade_figurinhas = len(album_figurinhas)

#             if quantidade_figurinhas == 0:
#                 print("Aviso: O Album de figurinhas está vazio")
#             else:
#                 print("\nAlbum de Figurinhas:")
#                 print(
#                     f"O Album de figurinhas tem {quantidade_figurinhas} figurinhas cadastradas:"
#                 )
#                 for i, jogador in enumerate(album_figurinhas, start=1):
#                     print(f" | Figurinha {i} - {jogador}")

#         elif selecione_opcao == 5:
#             print("Cadastro de figurinhas encerrado")
#             break
#         else:
#             print("\nDigite uma das opções válidas 1 ao 5:")

#     except ValueError:
#         print("\nDigite uma das opções válidas 1 ao 5:")


################## FIM ################################
# """
# Exercício 5 — Ranking de Artilheiros

# Crie uma lista de dicionários para armazenar informações de jogadores.

# O programa deverá perguntar quantos jogadores o usuário deseja cadastrar.

# Para cada jogador, solicite:

# Nome
# Seleção
# Quantidade de gols

# Cada jogador deverá ser armazenado como um dicionário dentro da lista.

# Ao final:

# Exiba todos os jogadores cadastrados.
# Informe qual jogador marcou mais gols.
# Informe a média de gols dos jogadores cadastrados.

# Desafio: utilize try/except para validar a quantidade de gols informada pelo usuário.
# """

# artilheiros = []
# total_gols = 0

# # Pergunta quantos jogadores cadastrar
# while True:
#     try:
#         quantidade = int(input("Quantos jogadores deseja cadastrar? "))
#         if quantidade > 0:
#             break
#         else:
#             print("Digite um número maior que zero.")
#     except ValueError:
#         print("Digite um número inteiro válido.")

# # Cadastro: repete até ter a quantidade pedida
# while len(artilheiros) < quantidade:
#     print(f"\nInforme os dados do artilheiro {len(artilheiros) + 1} de {quantidade}:")

#     # Nome
#     while True:
#         registro_nome = input("Digite o nome do jogador: ").strip().title()
#         if registro_nome == "":
#             print("Nome vazio não pode ser cadastrado!")
#         elif registro_nome.isnumeric():
#             print("Erro! Digite apenas letras.")
#         else:
#             break

#     # Seleção
#     while True:
#         registro_selecao = (
#             input("Digite o nome da Seleção do jogador: ").strip().title()
#         )
#         if registro_selecao == "":
#             print("O jogador precisa estar vinculado a uma Seleção.")
#         elif registro_selecao.isnumeric():
#             print("Erro! Digite apenas letras.")
#         else:
#             break

#     # Gols
#     while True:
#         try:
#             registro_gols = int(input("Digite a quantidade de gols do jogador: "))
#             if registro_gols >= 0:
#                 break
#             else:
#                 print("Erro! Digite número maior ou igual a zero.")
#         except ValueError:
#             print("Erro! Digite um número inteiro.")

#     # Guardar
#     jogador = {
#         "nome": registro_nome,
#         "selecao": registro_selecao,
#         "gols": registro_gols,
#     }
#     artilheiros.append(jogador)
#     total_gols += registro_gols
#     print("Sucesso! Cadastro efetuado.")

# print("\nCadastros finalizados ")

# # Exiba todos os jogadores cadastrados
# print("\nJogadores cadastrados:")
# for i, jogador in enumerate(artilheiros, start=1):
#     print(f" | {i} - {jogador['nome']} - {jogador['selecao']} - {jogador['gols']} gols")

# quantidade_artilheiros = len(artilheiros)
# print(f"\nTotal de artilheiros cadastrados: {quantidade_artilheiros}")

# # Informe qual jogador marcou mais gols
# artilheiro = max(artilheiros, key=lambda jogador: jogador["gols"])
# print(
#     f"O artilheiro é {artilheiro['nome']} ({artilheiro['selecao']}) com {artilheiro['gols']} gols."
# )

# # Informe a média de gols dos jogadores cadastrados.
# media_gols = total_gols / quantidade_artilheiros
# print(f"A média de gols por artilheiro é de {media_gols:.1f}")


################## FIM ################################
# """
# Desafio Final — Sistema da Copa do Mundo

# Desenvolva um programa para cadastrar partidas da Copa do Mundo.

# O programa deverá permanecer em execução até que o usuário decida encerrá-lo.

# Para cada partida, solicite:

# Seleção mandante
# Seleção visitante
# Gols da seleção mandante
# Gols da seleção visitante

# Cada partida deverá ser armazenada em um dicionário, e
# todos os dicionários deverão ser armazenados em uma lista.

# Ao finalizar o cadastro, exiba:

# A quantidade de partidas cadastradas.
# Todas as partidas registradas.
# Quantas partidas terminaram empatadas.
# A partida com o maior número total de gols.
# A média de gols por partida.

# Requisitos:

# Utilize listas e dicionários.
# Utilize while para controlar o cadastro.
# Utilize for para percorrer as partidas.
# Utilize if, elif e else para identificar o resultado de cada jogo.
# Utilize try/except para validar os gols informados.
# Utilize len() para calcular a quantidade de partidas cadastradas.
# """


partidas = []
total_gols = 0
resultado = ""

# # opção para encerrar cadastro
while True:
    opcao = input(
        "Deseja continuar o cadastro de partidas? Digite sim ou não: "
    ).lower()

    if opcao == "não" or opcao == "nao":
        print("Cadastro finalizado.")
        break

    elif opcao == "sim":
        print("Informe os dados da partida.")

    else:
        print("Digite apenas 'sim' ou 'não'.")
        continue

    # selecao_mandante
    while True:
        selecao_mandante = input("Digite o nome da Seleção mandante: ").strip().title()
        if selecao_mandante == "":
            print("Nome vazio não pode ser cadastrado!")
        elif selecao_mandante.isnumeric():
            print("Erro! Digite apenas letras.")
        else:
            break

    # selecao_visitante
    while True:
        selecao_visitante = (
            input("Digite o nome da Seleção visitante: ").strip().title()
        )
        if selecao_visitante == "":
            print("O jogador precisa estar vinculado a uma Seleção.")
        elif selecao_visitante.isnumeric():
            print("Erro! Digite apenas letras.")
        else:
            break

    # gols_mandante
    while True:
        try:
            gols_mandante = int(input("Digite a quantidade de gols do mandante: "))
            if gols_mandante >= 0:
                break
            else:
                print("Erro! Digite número maior ou igual a zero.")
        except ValueError:
            print("Erro! Digite um número inteiro.")

    # gols_visitante
    while True:
        try:
            gols_visitante = int(input("Digite a quantidade de gols do visitante: "))
            if gols_visitante >= 0:
                break
            else:
                print("Erro! Digite número maior ou igual a zero.")
        except ValueError:
            print("Erro! Digite um número inteiro.")

    total_gols_partida = gols_mandante + gols_visitante
    print(f"Total de gols na partida foi de {total_gols_partida} gols")

    # Resultado
    if gols_mandante > gols_visitante:
        resultado = f"Vitória de {selecao_mandante}"
    elif gols_visitante > gols_mandante:
        resultado = f"Vitória de {selecao_visitante}"
    else:
        resultado = "Empate"
        print(resultado)

    # Guardar
    dados_partida = {
        "selecao_mandante": selecao_mandante,
        "selecao_visitante": selecao_visitante,
        "gols_mandante": gols_mandante,
        "gols_visitante": gols_visitante,
        "total_gols": total_gols_partida,
        "resultado": resultado,
    }

    partidas.append(dados_partida)
    total_gols += total_gols_partida
    print("Sucesso! Cadastro efetuado.")

# A quantidade de partidas cadastradas
quantidade_partidas = len(partidas)
print(f"\nForam cadastradas {quantidade_partidas} partidas")

if quantidade_partidas > 0:

    # Todas as partidas registradas + contagem de empates
    empates = 0
    print("\nPartidas cadastradas:")
    for i, dados_partida in enumerate(partidas, start=1):
        print(
            f" | {i} - {dados_partida['selecao_mandante']} {dados_partida['gols_mandante']} x "
            f"{dados_partida['gols_visitante']} {dados_partida['selecao_visitante']}"
            f" | {dados_partida['resultado']} | {dados_partida['total_gols']} gols"
        )
        if dados_partida["resultado"] == "Empate":
            empates += 1

    # Quantas partidas terminaram empatadas
    print(f"\nPartidas empatadas: {empates}")

    # A partida com o maior número total de gols
    maior = max(partidas, key=lambda partida: partida["total_gols"])
    print(
        f"Partida com mais gols: {maior['selecao_mandante']} {maior['gols_mandante']} x "
        f"{maior['gols_visitante']} {maior['selecao_visitante']} ({maior['total_gols']} gols)"
    )

    # A média de gols por partida
    media_gols = total_gols / quantidade_partidas
    print(f"Média de gols por partida: {media_gols:.1f}")
else:
    print("Nenhuma partida foi cadastrada.")

################## FIM ################################
#########################
