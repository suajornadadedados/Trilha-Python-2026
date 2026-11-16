
# Estrutura de Repetiçõa


# grito = "GOL"

# for caracter in grito:
#     print (caracter)
# print ("A torcida terminou de gritar")

# RANGE

##. Resumo para memorizar
# Código	Resultado
# range(5)	         0, 1, 2, 3, 4   # SE COLOCAR SOMENTE UM NUMERO ELE COMEÇA DO 0
# range(1, 5)	     1, 2, 3, 4      # NÃO IMPRIME O ULTIMO
# range(0, 10, 2)	 0, 2, 4, 6, 8   # PODEMOS PULAR EM STP DE DOIS EM DOIS OU OUTRO NUMERO
# range(5, 0, -1)	 5, 4, 3, 2, 1   # PODE SER INVERSO

# for cobranca in range(1,6):
#     print (f"Cobrança {cobranca}: o jogador ajeita a bola...")


# # OPÇÃO DE VARIAVEL DENTRO DO TEXTO
# for rodada in range(1,5):
#     print ("Rodada" ,rodada, "da copa do mundo")


# print(list(range(5, 0, -3)))

# for numero in range(5, 0, -3):
#     print (numero)

# for rodada in range(1,6):
#     print (f"Rodada {rodada} da copa do mundo")

#     if rodada == 3:
#         print ("Última rodada! Jogo decisivo")

# gols_brasil = 0

# for lance in range(1,4):
#     print (f"Lance perigoso, número {lance}")

#     resultado =input("Foi gol do Brasil? Digite sim ou não: ")

#     if resultado == "sim":
#         gols_brasil+=1
#         print("GOOOOOOOOOOL")
#     else:
#         print ("Não foi gol ...")
# print ("Fim do jogo!")
# print(f"Total de gols do Brasil:{gols_brasil}")

# EXEMPLO WHILE

# cobranca = 1
# while cobranca <=5:
#     print (f"Cobrança {cobranca}: o jogador ajeita a bola...")
#     cobranca+=1 # variavel de controle

# resultado = input("Acertou o pênalti: Digite sim ou não: ")
                  
# while resultado !="sim":
#     print("Errou....tente de novo!")
#     resultado = input("Acertou o pênalti agora: Digite sim ou não: ")
# print ("Boa! O Jogador acertou pênalti")

gols =0
rodada=1

# while gols <3:
#     print(f"Rodada treino {rodada}")

#     for cobranca in range (1,4):
#         print(f"Cobrança -  {cobranca}")
#         resultado =input ("Foi gol? Digite sim ou não: ")

#         if resultado =="sim":
#             gols +=1
#             print ("GOOOOOOOOOOOL")
#         else:
#             print ("Errou...")
#     print(f"Total de gols até agora {cobranca}")
#     rodada += 1
# print ("\nTreino finalizado")
# print(f"Número de rodadas: {rodada}")

print (gols+rodada)
resultado = gols + rodada
print (resultado )

pontos = 7
vitorias = 2
saldo_gols = 4


print (pontos > 5)
print (vitorias== 3)
print (pontos > 5 and saldo_gols>0)


