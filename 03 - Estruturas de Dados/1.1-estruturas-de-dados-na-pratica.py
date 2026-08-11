'''
PARTIDA

Brasil x México

Titulares:
Alisson
Marquinhos
Gabriel Magalhães
Bruno Guimarães
Raphinha
Rodrygo
Vini Jr.

Gols:
Vini Jr.
Rodrygo
Vini Jr.

México marcou 1 gol.
'''

jogadores = [
    "Alisson",
    "Marquinhos",
    "Gabriel Magalhães",
    "Bruno Guimarães",
    "Raphinha",
    "Rodrygo",
    "Vini Jr.",
]

# print(jogadores)
# print(jogadores[0])
# print(jogadores[1])
# print(jogadores[2])
# print(jogadores[3])
# print(jogadores[-1])

jogadores.append("Endrick")
# print(jogadores)
# print(jogadores[-1])

jogadores[3] = "Neymar"
# print(jogadores)

# print("Jogadores do Brasil")
# for i, jogador in enumerate(jogadores):
#     print(f" - {jogador} | Posição: {i}")


partida = (
    "Brasil",
    "México",
    "Estádio Central",
    "20:00"
)

print(partida)
print(partida[0])
print(partida[3])
print(partida[-1])

# Desempacotamento
selecao = partida[0]
adversario = partida[1]
estadio = partida[2]
horario = partida[3]

print(selecao, adversario, estadio, horario)

print(selecao)
print(partida[0])

print(f"{selecao} x {adversario}")
print(f"Estádio: {estadio}")
print(f"Horário: {horario}")

autores_gols = [
    "Vini Jr.",
    "Rodrygo",
    "Vini Jr.",
]

quantidade_gols = len(autores_gols)
print(quantidade_gols)

jogadores_que_marcaram_gols = set(autores_gols)
print(jogadores_que_marcaram_gols)
quantidade_de_jogadores_que_marcaram_gols = len(jogadores_que_marcaram_gols)
print(quantidade_de_jogadores_que_marcaram_gols)
# Vini Jr. -> 2
# Rodrygo -> 1

# Contagem de Gols
gols_por_jogador = {}
# Adicionar a chave que vai ser o nome do jogador e adicionar a quantidade de gols que ele fez no valor
# for (iterar sobre nossa lista), if (condições), dicionário (armazenar os dados)

for jogador in autores_gols:
    
    if jogador in gols_por_jogador:
        gols_por_jogador[jogador] += 1
    else:
        gols_por_jogador[jogador] = 1
        
print(gols_por_jogador)

# .items(), .keys(), .values()

for jogador in gols_por_jogador.items():
    print(jogador)
    
print(gols_por_jogador.items())
print(gols_por_jogador.keys())
print(gols_por_jogador.values())
    
for jogador, gols in gols_por_jogador.items():
    print(f"{jogador}: {gols} gol(s)")
    
    
# Recuperando input(), while e validação


# Recuperando try/except
# Descobrindo o resultado da partida
# Gerando os dados finais