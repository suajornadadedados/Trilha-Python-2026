# from ast import While

# gols_brasil = "3"
# gol_extra = 1


# total_gols = gols_brasil + gol_extra
# print(total_gols)

# total_gols2 = gol_extra + gols_brasil
# print(total_gols2)


# =========================================================

# # O isinstance() pergunta se um valor é de um tipo específico.
# # A resposta dessa verificação é True ou False.

# gols = 3

# if isinstance(gols, int):
#     print("A variável gols é um número inteiro.")
# else:
#     print("A variável gols não é um número inteiro.")
# =========================================================
# 10) TYPE HINT NÃO FORÇA O TIPO
# =========================================================

# Mesmo indicando que gols deveria ser int,
# o Python ainda permite trocar o valor para uma string.
# Isso não é uma boa prática, mas mostra que Type Hint é dica, não trava.


# # Sem Type Hint
# time = "Brasil"
# gols = 3
# classificado = True

# print(time)
# print(gols)
# print(classificado)


# # Com Type Hint
# time: str = "Brasil"
# gols: int = 3
# classificado: bool = True

# print(time)
# print(gols)
# print(classificado)
# =========================================================
# conversão

# gols_texto = input("Qauntos Gols o Brasil fez?: ")
# gols = int(gols_texto)
# gols_total = gols + 1

# print(gols_total)

# ou

# gols2 = int(input("Qauntos Gols o Brasil fez?: "))
# gols_total2 = gols2 + 1
# print(f"Total de gols no jogo {gols_total2}")
# =========================================================

# total_gols: int = 0

# for jogo in range(1, 4):
#     gols: int = int(input(f"Quantos gols fez o brasil no jogo {jogo}?: "))
#     total_gols += gols

# print(f"Total de gols nos 3 jogos: {total_gols}")

# =========================================================
# /n - para incluir espaços

# total_gols: int = 0

# for jogo in range(1, 4):
#     gols: int = int(input(f"Quantos gols fez o brasil no jogo {jogo}?: "))

#     total_gols += gols

#     if gols == 0:
#         print("O Brasil não fez gols nesse jogo\n")

#     elif gols == 1:
#         print(" O Brasil fez apenas 1 gol nesse jogo.\n")
#     else:
#         print(f"O Brasil marcou {gols} nesse jogo\n")

# print(f"Total de gols do Brasil: {total_gols}\n")

# media_de_gols: float = round(total_gols / 3, 2)
# print(f"A média de gols do Brasil foi de: {media_de_gols} por jogo")

# print(f"A média de gols do Brasil foi de: {media:.2f} por jogo")
# print(f"A média de gols do Brasil foi de: {round(media,2)} por jogo")

# ========================TRY =================================

# try:
#     gols = int(input(f"Quantos gols fez o brasil no jogo? "))
#     print(gols)
#     print(type(gols))

# except:
#     print("Algo deu errado")
# ========================TRY =================================

# ========================TRY =================================

# try:
#     gols = int(input(f"Quantos gols fez o brasil no jogo? "))
#     print(gols)
#     print(type(gols))

# except ValueError:
#     print("Você precisa digitar um numero inteiro")
# ========================TRY =================================

# try:
#     gols: int = int(input(f"Quantos gols fez o brasil no jogo? "))
#     jogos: int = int(input(f"Em quantos jogos? "))

#     media: float = gols / jogos

#     print(f"A média de gols por jogos: {media}")

# except ValueError:
#     print("Você precisa digitar numeros inteiros")
# except ZeroDivisionError:
#     print("A quantidade de jogos não pode ser zero")
# ========================TRY COM WHILE=================================

# # numero_valido: bool = False


# # while numero_valido == False:
# #     try:
# #         gols: int = int(input(f"Quantos gols fez o brasil no jogo? "))
# #         jogos: int = int(input(f"Em quantos jogos? "))

# #         media: float = gols / jogos
# #         numero_valido = True
# #         print(f"A média de gols por jogos: {media}")

# #     except ValueError:
# #         print("Você precisa digitar numeros inteiros")
# #     except ZeroDivisionError:
# #         print("A quantidade de jogos não pode ser zero")
# # else:
# #     print("Formula funcionou")

# # ========================TRY COM WHILE e for[]=================================
# total_gols: int = 0

# for jogo in range(1, 4):
#     numero_valido: bool = False

#     while numero_valido == False:
#         try:
#             gols: int = int(input(f"Quantos gols o brasil fez no jogo {jogo} ?: "))
#             numero_valido = True

#         except ValueError:
#             print("Você precisa digitar numeros inteiros")
#         except ZeroDivisionError:
#             print("A quantidade de jogos não pode ser zero")
#     total_gols += gols

#     if gols == 0:
#         print("O Brasil não macou gols nesses jogo. \n")
#     elif gols == 1:
#         print("O Brasil marcou 1 gols nesse jogo.\n")
#     else:
#         print(f"O Brasil marcou {gols} gols nesse jogo. \n")


# print(f"O Total de gols do brasil foi de {total_gols}\n")

# media: float = total_gols / 3

# print(f"A média de gols do Brasil foi de: {media:.2f} por jogo")
############################################################
###############################################################
# Atividade Prática – Entendendo e Corrigindo Erros
#
# Exercício 1 – Descobrindo os tipos

# # Observe os valores abaixo:

# nome = "Brasil"
# gols = 3
# posse_bola = 58.7
# classificado = True

# # Crie um programa que mostre o tipo de cada uma dessas variáveis utilizando type().
# # Ao executar, o programa deve permitir identificar quais valores são str, int, float e bool.


# print(type(nome))
# print(type(gols))
# print(type(posse_bola))
# print(type(classificado))
########################  #######  ###############################
# Exercício 2 – Verificando os tipos
# Considere as variáveis:
# numero_camisa = 10
# jogador = "Raphinha"

# Utilize isinstance() para verificar:

# se numero_camisa é um int;
# se numero_camisa é uma str;
# se jogador é uma str.

# Mostre o resultado de cada verificação na tela.

# if isinstance(numero_camisa, int):
#     print("A variável numero_camisa é um número inteiro.")
# else:
#     print("A variável numero_camisa não é um número inteiro.")

# if isinstance(numero_camisa, str):
#     print("A variável numero_camisa é um texto.")
# else:
#     print("A variável numero_camisa não é um texto.")

# if isinstance(jogador, str):
#     print("A variável jogador é um texto.")
# else:
#     print("A variável jogador não é um texto.")
########################  #######  ###############################
# Exercício 3 – Encontre o Erro e Corrija

# O código abaixo apresenta um erro:

# gols = "2"
# novo_gol = gols + 1

# print(novo_gol)

# gols = "2"
# novo_gol = int(gols) + 1

# print(novo_gol)

# Execute o código, observe a mensagem apresentada pelo Python e responda:
# Qual erro ocorreu? TypeError: can only concatenate str (not "int") to str
# Quais são os tipos dos valores envolvidos? string e inter
# Por que esses valores não podem ser utilizados dessa forma? Não é posslve concatenar texto com numero.  O Python não entendi que
# Corrija o programa para que o resultado exibido seja 3.

########################  #######  ###############################
# Exercício 4 – Trabalhando com input()
# Crie um programa que pergunte ao usuário quantos gols uma seleção marcou em uma partida.
# Depois:

# descubra o tipo do valor recebido diretamente pelo input();
# converta esse valor para int;
# mostre novamente o tipo depois da conversão;
# calcule quantos gols a seleção teria caso marcasse mais um.

# Exemplo de entrada:

# Quantos gols a seleção marcou? 2
# Resultado esperado ao final:
# Com mais um gol, a seleção teria 3 gols.

# gols: int = input("Quantos gols uma seleção marcou em uma partida?")
# print(type(gols))
# gols_convertido = int(gols)
# print(type(gols_convertido))
# total_gols = gols_convertido + 1
# print(f"Total de gols marcados foi de : {total_gols}")

########################  #######  ###############################
# Exercício 5 – Convertendo valores decimais

# Crie um programa que peça ao usuário:

# o nome de um jogador;
# sua nota na partida.

# A nota pode possuir casas decimais, como 8.5.

# Converta a nota para o tipo adequado e exiba uma mensagem semelhante a:
# Vinicius recebeu a nota 8.5.
# Antes de finalizar, utilize type() para verificar se a nota foi realmente
# convertida para o tipo esperado.

# jogador: str = input("Qual o nome do jogador?")
# nota: float = float(input("Qual a nota do jogador na partida?"))
# print(type(nota))
# print(f"O {jogador} recebeu a nota {nota} .")
########################  #######  ###############################
# Exercício 6 – Quando precisamos de str

# Considere:
# numero = 10
# jogador = "Rodrygo"
# Crie uma mensagem que resulte em:

# O jogador Rodrygo veste a camisa 1.
# Para este exercício, faça a construção da mensagem utilizando +.
# Observe o erro que acontece ao tentar concatenar diretamente numero com os textos e depois utilize str() para corrigir o problema.
# Explique por que a conversão foi necessária.

# numero = 10
# jogador = "Rodrygo"

# # print(jogador + numero)
# # TypeError: can only concatenate str (not "int") to str
# print(jogador + str(numero))

# print(type(numero))
# print(type(jogador))

# print(f"O jogador {jogador} veste a camisa {numero}.")

# # O Phyton não sabe se deve somar ou concatenar.Não é possível concatenar variável string com inteiro
# # Tem um erro de digitação no exercio está escrito camisa 1
########################  #######  ###############################
# Exercício 7 – Deixando os valores explícitos

# Crie as seguintes variáveis utilizando Type Hint:
# Atribua um valor para cada variável.
# Depois, altere propositalmente uma delas para um valor de
# outro tipo e observe o comportamento do Python.

# Com base no que aconteceu, responda:

# O Type Hint impede que uma variável receba outro tipo de valor
# durante a execução?

# nome_da_selecao: str = "Brasil"
# quantidade_de_vitórias: int = 5
# aproveitamento: float = 9.1
# seleção_classificada: bool = True

# print(type(nome_da_selecao))
# print(type(quantidade_de_vitórias))
# print(type(aproveitamento))
# print(type(seleção_classificada))

# # # O Type Hint não impede que uma variável receba outro tipo de valor.
# # Ele só sinaliza qual tipo de variavel se espera para controle em projetos
# # grandes ou com equipes com ias de um desenvolvedor

########################  #######  ###############################
# Exercício 8 – Impedindo o programa de quebrar

# Crie um programa que pergunte a idade do usuário:
# Converta a resposta para int.

# Use try/except para impedir que o programa seja encerrado caso alguém
# digite algo como: vinte

# Se a conversão funcionar, mostre:
# Idade registrada com sucesso.
# Se ocorrer um ValueError, mostre:
# Digite a idade utilizando apenas números.

# idade_validada: bool = False

# while idade_validada == False:
#     try:
#         idade: int = int(input("Digite a idade do usuário:"))
#         print("Idade registrada com sucesso.\n")
#         idade_validada = True

#     except ValueError:
#         print("Digite a idade utilizando apenas números")

#### não precisa do else abaixo para funcionar

# else:
# print(f"ok, a idade {idade} foi digitada corretamente")
########################  #######  ###############################
# Exercício 9 – Tratando entrada e validando o valor

# Uma avaliação de jogador deve receber uma nota entre 0 e 10.

# Crie um programa que peça essa nota ao usuário.

# O programa deve:

# tentar converter a entrada para float;
# tratar um possível ValueError;
# verificar se a nota está entre 0 e 10;
# informar quando a nota estiver fora desse intervalo.

# Exemplos:

# Digite a nota: oito
# Valor inválido. Digite um número.

# Digite a nota: 15
# A nota deve estar entre 0 e 10.

# Digite a nota: 8.5
# Nota registrada: 8.5

##### ######## #######

# nota_validada: bool = False

# while nota_validada == False:
#     try:
#         nota: float = float(input("Digite a nota ao usuário: "))
#         nota_validada = True
#         if nota >= 0 and nota <= 10:
#             print(f"Nota registrada: {nota:.1f} \n")
#             nota_validada = True
#         else:
#             print("A nota deve estar entre 0 e 10.\n")
#             nota_validada = False

#     except ValueError:
#         print("Valor inválido. Digite um número")
#         nota_validada = False
########################  #######  ###############################
# Exercício 10 – Continue perguntando até receber um valor válido

# Crie um programa para registrar a quantidade de gols de uma seleção.
# O programa deve continuar perguntando:
# Quantos gols a seleção marcou?
# até que o usuário forneça um número inteiro válido e maior ou igual a zero.
# Considere situações como:

# Quantos gols a seleção marcou? três
# Entrada inválida.

# Quantos gols a seleção marcou? -2
# A quantidade de gols não pode ser negativa.

# Quantos gols a seleção marcou? 4
# Quantidade de gols registrada: 4

# Para resolver o exercício, utilize os conteúdos estudados até aqui, incluindo:

# input();
# conversão com int();
# try/except;
# ValueError;
# condição;
# while.

# O programa só deve parar de solicitar a informação quando receber um valor válido.

gols_validado = False

while gols_validado == False:
    try:
        gols: int = int(input("Quantos gols a seleção marcou? "))
        # print(f"Quantidade de gols registrada: {gols}")
        gols_validado = True
        if gols > 0:
            print(f"Quantidade de gols registrada: {gols}")
        else:
            print(" A quantidade de gols não pode ser negativa")
            gols_validado = False

    except ValueError:
        print("Entrada inválida.")
        gols_validado = False

########################  #######  ###############################
########################  #######  ###############################
########################  #######  ###############################
