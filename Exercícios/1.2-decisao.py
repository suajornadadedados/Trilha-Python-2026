# Estrutura de Decisão

# distancia_do_gol =20
# if distancia_do_gol <18:
#     print ("Entrou na área do gol. Perigode gol")

# Exemplo de IF ELSE
# fora_do_chute = 87
# reflexo_goleiro = 60

# if fora_do_chute < reflexo_goleiro:
#     print("Gol")
# else:
#     print("Goleiro defendeu")

# Qual cartão o juiz deu?

# gravidade_da_falta = "grave"

# if gravidade_da_falta == "Leve":
#     print("Advetência")
# elif gravidade_da_falta =="moderada":
#     print("Cartão amarelo")
# else:
#     print("Cartão vermelho")

    # Cenários Multiplo elif


# saldo = 1 # diferença de gols ( negativo = perdendo)

# if saldo>= 3:
#     print ("vitoria tranquila")
# elif saldo == 2 :
#     print ("Jogo controlado")
# elif saldo ==1:
#     print ("Vitória apertada")
# elif saldo ==0:
#     print ("Jogo empatado")
# elif saldo ==-1:
#     print ("Time perdendo")
# else:
#     print ("Está ruim")
        

# # If Aninhado => Operadores Lóicos( AND, OR,NOT)
# # Cenário decisão de VAR
# print ("__Cenário decisão de VAR__")

# teve_gol =True
# revisao_do_var = "mao" # legal, impedido, mão e falta

# if teve_gol:
#     print ("Gol marcado.")

#     if revisao_do_var == "legal":
#         print ("Gol confirmado")
#     else:
#         print ("Gol anulado")   
# else:
#     print ("Não teve gol")

# print ("__Cenário decisão de VAR_opcao2_")

# if teve_gol and revisao_do_var == "legal":
#     print ("Gol confirmado")
# else:
#     print ("Gol não confirmado")

#  # IF / ELIF / ELSE COM OPERADORES LÓGICOS E DE COMPARAÇÃO( AND, OR,NOT)
# Cenário: Chance de liderar o grupo

print ("__Chance de liderar o grupo__")

pontos = 6
saldo_gols = 4
jogo_direto_contra_lider = True
gols_marcados=7

if pontos >=7 and saldo_gols > 3:
    print ("Já está na liderança")
elif pontos == 6 and jogo_direto_contra_lider and saldo_gols > 3:
    print ("Depende só da vitória")
elif pontos == 6 and (saldo_gols <3 or gols_marcados < 3):
    print ("Precisa ganhar e torcer")
elif pontos < 4 or saldo_gols <-2 :
    print ("Risco de eliminacao")
else:
    print ("Classificação indefinida")

nome_do_jogador = "Cristiano Ronaldo"

if nome_do_jogador == "cristiano ronaldo":
    print ("O jogador é o Cristiano Ronaldo com letras minusculas")
elif nome_do_jogador == "Cristiano Ronaldo":
    print ("O jogador é o Cristiano Ronaldo com letras maiusculas")
else:
    print("Nome não encontrato")

# Match case


#No Python, tanto match/case quanto if/elif/else servem para tomar decisões no código. 
# A diferença principal é o tipo de situação em que cada um é mais útil.
  # 1.Quando usar if / elif / else
#Use quando precisar verificar condições, comparações e operadores lógicos, como >, <, ==, and, or e not.

  #2. Quando usar match / case
#Use quando quiser comparar um valor com diferentes opções específicas, como menus, comandos, categorias ou códigos.
#Exemplo: um menu de opções.


print ("__Match case__")

revisao_do_var_novo  = "impedido"


match revisao_do_var_novo:
        case "legal":
            print ("Gol confirmado")
        case "impedido":
            print ("Gol anulado por impedimento")
        case "mao":
            print ("Gol anulado por toque de mão")
        case "falta":
            print ("Gol anulado por falta")
        case _:
            print ("Lance em revisão")

# O MESMO CASO COM O ELIF

print ("__Exemplo ELIF__")


if revisao_do_var_novo == "legal":
    print ("Gol confirmado")
elif revisao_do_var_novo == "impedido":
    print ("Gol anulado por impedimento")
elif revisao_do_var_novo == "mao":
    print ("Gol anulado por toque de mão")
elif revisao_do_var_novo == "falta":
     print ("Gol anulado por falta")
else:
    print ("Lance em revisão")


# OUTRO EXEMPLO MATCH CASE
print ("__Exemplo Match Case__")

posicao= "goleiro"

match posicao:
    case "goleiro":
        print ("Defende o gol")
    case "zagueiro":
        print ("Marca os atacantes.")
    case "atcantes":
        print ("Tenta fazer o gol.")
    case _:
        print ("Posicão não reconhecida")