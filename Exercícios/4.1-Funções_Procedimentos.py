##########

# S padrão que funciona na maioria dos casos é este:


# def nome_da_funcao(param1, param2=None):
# """
# Descrição do que a função faz.
# """
#
# # processamento
# resultado = param1
#
# return resultado

#######
# Exemplos práticos:

# Exemplo: 1
# def somar(a, b):
# resultado = a + b
# return resultado

# Exemplo: 2
# def calcular_imc(peso, altura):
# imc = peso / (altura ** 2)
# return imc

# Exemplo: 3
# def exibir_mensagem(nome):
# print(f"Olá, {nome}!")


# Uma boa "receita mental" para criar qualquer função é:


# def nome_da_funcao(entradas):
# # lógica
# return resultado


# ########  ###########  ######################

# Exercício 1 – Exibindo uma mensagem

# Crie uma função chamada exibir_boas_vindas() que exiba a mensagem:
# Bem-vindo ao sistema!

# Depois, chame a função para executar a mensagem.

# Requisitos:

# Utilize def.
# A função não deve receber parâmetros.
# A função não precisa retornar nenhum valor.


def mensagem_boasvindas():
    print("Bem-vindo ao sistema!")


mensagem_boasvindas()

##################  ###########  ######################

# Exercício 2 – Identificando um produto

# Crie uma função chamada exibir_produto() que receba:

# o nome de um produto;
# o preço do produto.

# A função deve exibir uma mensagem no seguinte formato:
# Produto: Teclado | Preço: R$ 150.00

# Depois, chame a função passando um produto e um preço como
# argumentos.

# Requisitos:
# Utilize parâmetros.
# Adicione type hints nos parâmetros.
# A função deve retornar None.


def exibir_produto(nome_produto: str, preco_produto: float) -> None:
    """
    Exibe informação do produto

    Args:
        nome_produto: Nome do produto
        preco_produto: Preço unitário do produto
    """
    print(f"Produto: {nome_produto} | Preço: R$ {preco_produto:.2f}")


nome_produto = "Teclado"
preco_produto = 150.00

exibir_produto(nome_produto, preco_produto)

##################  ###########  ######################
##################  ###########  ######################

# Exercício 3 – Calculando o valor de uma compra

# Crie uma função chamada calcular_total() que receba:


# o preço de um produto;
# a quantidade comprada.

# A função deve calcular e retornar o valor total da compra.

# Exemplo:

# total = calcular_total(50.0, 3)
# print(total)

# Resultado esperado: 150.0

# Requisitos:
# preco deve possuir type hint float.
# quantidade deve possuir type hint int.
# A função deve indicar que retorna um float.
# Utilize return para devolver o resultado.


def calcular_total(preco: float, quantidade: int) -> float:
    """
    A função calcula o valor total de uma compra

    Args:
        preco: Preço unitário do produto
        quantidade: Quantidade comprada do produto, número inteiro positivo

    Returns:
        Valor total da compra.
    """
    total = preco * quantidade
    return total


total = calcular_total(50.0, 3)
print(total)

##################  ###########  ######################

# Exercício 4 – Calculando a média de avaliações
# Uma plataforma armazena três avaliações dadas por usuários para um produto.
# Crie uma função chamada calcular_media_avaliacoes() que receba três notas e
# retorne a média entre elas.

# Depois, utilize o resultado retornado pela função para exibir a média das avaliações

# Requisitos:

# Utilize parâmetros e argumentos.
# Adicione type hints.
# Utilize return.
# Adicione uma docstring explicando o que a função recebe e o que retorna.
# Guarde o resultado da função em uma variável antes de exibi-lo.


def calcular_media_avaliacoes(nota1: float, nota2: float, nota3: float) -> float:
    """
    Calcula a média de três avaliações dadas por usuários para um produto.

    Args:
        nota1: primeira nota dada pelo usuário
        nota2: segunda nota dada pelo usuário
        nota3: terceira nota dada pelo usuário

    Returns:
        Média das três notas.
    """
    media_avaliacoes = (nota1 + nota2 + nota3) / 3
    return media_avaliacoes


media_avaliacoes = calcular_media_avaliacoes(10, 10, 8)
print(f"A média das avaliações é {media_avaliacoes:.2f}")

##################  ###########  ######################

# Exercício 5 – Processando um pedido

# Você precisa criar duas funções para representar uma pequena parte de um sistema
# de pedidos.

# A primeira função deve se chamar: calcular_valor_final()

# Ela deve receber:

# preço unitário;
# quantidade;
# desconto em formato decimal.
# Por exemplo, 0.10 representa 10% de desconto.

# A função deve calcular e retornar o valor final do pedido após o desconto.

# Depois, crie uma segunda função chamada: exibir_resumo_pedido()

# Ela deve receber:
# número do pedido;
# valor final.

# E exibir uma mensagem como: Pedido #1025 finalizado. Total: R$ 270.00

# Requisitos:
# As duas funções devem possuir type hints.
# calcular_valor_final() deve retornar um float.
# exibir_resumo_pedido() deve retornar None.
# As duas funções devem possuir docstrings.
# O valor retornado por calcular_valor_final() deve ser passado como argumento para
# exibir_resumo_pedido().
# Não faça o cálculo diretamente fora da função.


def calcular_valor_final(preco: float, quantidade: int, desconto: float) -> float:
    """
    A função calcula o valor total de uma compra

    Args:
        preco: Preço unitário do produto
        quantidade: Quantidade comprada do produto, número inteiro positivo
        desconto:desconto em formato decimal.

    Returns:
        Valor final da compra após o desconto
    """
    subtotal: float = preco * quantidade
    desconto_aplicado: float = subtotal * desconto
    valor_final: float = subtotal - desconto_aplicado
    return valor_final


def exibir_resumo_pedido(numero_pedido: int, valor_final: float) -> None:
    """
    Exibe informação do número do pedido e o valor do pedido

    Args:
        numero_pedido: Número do pedido
        valor_final: Valor final do pedido finalizado

    """
    print(f"Pedido #{numero_pedido} finalizado. Total: R$ {valor_final:.2f}")


valor_final = calcular_valor_final(100.0, 3, 0.10)
numero_pedido = 1025
exibir_resumo_pedido(numero_pedido, valor_final)

##################  ###########  ######################

# Exercício 6 – Convertendo temperatura

# Crie uma função chamada converter_celsius_para_fahrenheit().
# A função deve receber uma temperatura em Celsius e retornar o valor convertido
# para Fahrenheit.

# Use a fórmula: fahrenheit = (celsius * 9 / 5) + 32
# Depois, armazene o resultado em uma variável e imprima a temperatura convertida.

# Requisitos:

# Receba a temperatura por parâmetro.
# Utilize type hint float.
# A função deve retornar um float.
# Utilize return.
# Adicione uma docstring explicando a função.


def converter_celsius_para_fahrenheit(temperatura_celsius: float) -> float:
    """
    A função converte a temperatura de Celsius para Fahrenheit

    Args:
        temperatura_celsius: número da temperatura em celsius
    Returns:

        Temperatura em Fahrenheit

    """
    temperatura_fahrenheit: float = (temperatura_celsius * 9 / 5) + 32
    return temperatura_fahrenheit


temperatura_celsius = 30.0
temperatura_convertida = converter_celsius_para_fahrenheit(temperatura_celsius)
print(
    f" A temperatura está em {temperatura_celsius:.1f} °C, que equivalem a {temperatura_convertida:.1f} °F."
)

##################  ###########  ######################

# Exercício 7 – Calculando consumo médio

# Um veículo percorreu determinada distância utilizando uma quantidade de combustível.

# Crie uma função chamada calcular_consumo_medio() que receba:

# distância percorrida em quilômetros;
# quantidade de litros utilizados.

# A função deve retornar quantos quilômetros o veículo percorreu por litro.

# Exemplo: consumo = calcular_consumo_medio(420.0, 35.0)
# Resultado: 12.0

# Depois, crie uma segunda função chamada exibir_consumo() que receba o resultado e exiba: Consumo médio: {resultado} km/l

# Requisitos:
# As duas funções devem possuir type hints.
# calcular_consumo_medio() deve retornar float.
# exibir_consumo() deve retornar None.
# As duas funções devem possuir docstrings.
# O resultado da primeira função deve ser passado como argumento para a segunda.


def calcular_consumo_medio(distancia: float, quantidade_combustivel: float) -> float:
    """
    A função deve retornar quantos quilômetros o veículo percorreu por litro.

    Args:
        distancia:distância percorrida em quilômetros
        quantidade_combustivel: quantidade de litros utilizados.

    Returns:
        Quantidade de quilometros percorrido por litro de combustível
    """
    consumo: float = distancia / quantidade_combustivel

    return consumo


def exibir_consumo(consumo: float) -> None:
    """
    Exibir consumo médio

    Args:
        consumo:consumo médio da viagem
    """


dados_viagem = calcular_consumo_medio(420.0, 35.0)
print(f"Consumo médio: {dados_viagem } km/l")

##################  ###########  ######################

# Exercício 8 – Verificando uma meta de vendas

# Crie uma função chamada calcular_percentual_meta() que receba:
# valor da meta;
# valor vendido.

# A função deve calcular e retornar o percentual da meta que foi atingido.

# Exemplo: percentual = calcular_percentual_meta(10000.0, 7500.0)
# Resultado: 75.0

# Depois, crie uma função chamada exibir_status_meta() que receba esse percentual.

# Ela deve exibir: Meta atingida!
# caso o percentual seja maior ou igual a 100.

# Caso contrário, deve exibir: Meta ainda não atingida.

# Requisitos:
# Utilize type hints.
# calcular_percentual_meta() deve retornar float.
# exibir_status_meta() deve retornar None.
# Utilize o valor retornado por uma função como argumento da outra.
# Adicione docstrings nas duas funções.
# Não repita o cálculo do percentual fora da função.


####
def calcular_percentual_meta(valor_meta: float, valor_vendido: float) -> float:
    """
    Calcula o percentual da meta

    Args:
        valor_meta: valor da meta de vendas
        valor_vendido: valor efetivamente vendido

    Returns:
        Percentual da meta atingido.
    """
    percentual = valor_vendido / valor_meta * 100
    return percentual


def exibir_status_meta(percentual: float) -> None:
    """
    Exibe se a meta foi atingida ou não.

    Args:
        percentual: percentual da meta atingido

    """
    if percentual >= 100:
        print("Meta atingida!")
    else:
        print("Meta ainda não atingida.")


percentual = calcular_percentual_meta(10000.0, 7500.0)
exibir_status_meta(percentual)


##################  ###########  ######################

# Exercício 9 – Analisando uma entrega

# Você está desenvolvendo uma pequena parte de um sistema de entregas.

# Crie uma função chamada calcular_tempo_estimado() que receba:

# distância da entrega em quilômetros;
# velocidade média do veículo em km/h.

# A função deve calcular e retornar o tempo estimado da entrega em horas.

# Use: tempo = distancia / velocidade

# Depois, crie uma função chamada classificar_entrega() que receba o tempo calculado e retorne:

# "Entrega rápida" se o tempo for menor ou igual a 1;
# "Entrega normal" se o tempo for maior que 1 e menor ou igual a 3;
# "Entrega demorada" se o tempo for maior que 3.

# Por fim, crie uma terceira função chamada exibir_resumo_entrega() que receba:
# o tempo estimado;
# a classificação.

# Ela deve exibir algo como:
# Tempo estimado: 2.5 horas
# Classificação: Entrega normal


# Requisitos:
# As três funções devem possuir type hints.
# calcular_tempo_estimado() deve retornar float.
# classificar_entrega() deve retornar str.
# exibir_resumo_entrega() deve retornar None.
# Todas devem possuir docstrings.
# O resultado de calcular_tempo_estimado() deve ser utilizado por classificar_entrega().
# Os resultados das duas primeiras funções devem ser utilizados por exibir_resumo_entrega().
# Cada função deve possuir apenas uma responsabilidade.


####


def calcular_tempo_estimado(distancia: float, velocidade: float) -> float:
    """
        Calcular o tempo estimado da entrega em h    oras
    Args:
        distancia:distância da entrega em quilômetros
        velocidade:velocidade média do veículo em km/h.
    Returns:
        Tempo estimado da entrega em  horas.
    """
    tempo_estimado = distancia / velocidade
    return tempo_estimado


def classificar_entrega(tempo_estimado: float) -> str:
    """
    Classifica o tempo de entrega seguindo alguns critérios
    Args:
        tempo_estimado: tempo estimado da entrega calculado na função 'calcular_tempo_estimado'
    Returns:
        Classiicação do tempo estimado da entrega em horas.
    """
    if tempo_estimado <= 1:
        classificacao = "Entrega rápida"
    elif tempo_estimado <= 3:
        classificacao = "Entrega normal"
    else:
        classificacao = "Entrega demorada"
    return classificacao


def exibir_resumo_entrega(tempo_estimado: float, classificacao: str) -> None:
    """
        Exibe o resumo da entrega com o tempo e a classificação
    Args:
        tempo_estimado: tempo estimado da entrega calculado na função 'calcular_tempo_estimado'
        classificacao : Clssificação do tempo de entrega obtido na função classificação 'classificar_entrega'
    """
    print(f"Tempo estimado: {tempo_estimado:.1f} horas\nClassificação: {classificacao}")


distancia = 100
velocidade = 40
tempo_estimado = calcular_tempo_estimado(distancia, velocidade)
classificacao = classificar_entrega(tempo_estimado)
exibir_resumo_entrega(tempo_estimado, classificacao)


##################  ###########  ######################


# Exercício 10 – Sistema de Aprovação de Empréstimo

# Você está desenvolvendo uma parte de um sistema bancário responsável por analisar solicitações de empréstimo.

# O programa deverá utilizar várias funções, e cada uma terá uma responsabilidade específica.


# 1. Calcular comprometimento da renda
# Crie uma função chamada calcular_comprometimento_renda() que receba:

# renda mensal;
# valor da parcela do empréstimo.
# Ela deve calcular qual percentual da renda mensal seria comprometido pela parcela.

# Use:

# percentual = (parcela / renda) * 100

# A função deve retornar esse percentual.


# 2. Analisar o empréstimo
# Crie uma segunda função chamada analisar_emprestimo() que receba:

# renda mensal;
# valor solicitado;
# percentual de comprometimento da renda.
# A função deve retornar uma das seguintes classificações:

# "Aprovado"
# "Análise manual"
# "Recusado"


# Utilize estas regras:

# Se o comprometimento da renda for maior que 40%, retorne "Recusado".
# Se o comprometimento for menor ou igual a 40%, mas o valor solicitado for maior que 5 vezes a renda mensal, retorne "Análise manual".
# Caso contrário, retorne "Aprovado".


# 3. Calcular o total do pagamento
# Crie uma terceira função chamada calcular_total_pagamento() que receba:

# valor da parcela;
# quantidade de parcelas.
# Ela deve retornar o valor total que será pago ao final do empréstimo.

# Exemplo:

# Parcela: R$ 850.00
# Quantidade: 24

# Total pago: R$ 20400.00


# 4. Exibir o resultado final
# Por fim, crie uma função chamada exibir_resultado() que receba:

# valor solicitado;
# percentual de comprometimento;
# total que será pago;
# resultado da análise.
# Ela deve apenas exibir um resumo como:

# --- Análise do empréstimo ---

# Valor solicitado: R$ 15000.00
# Comprometimento da renda: 28.3%
# Total a pagar: R$ 20400.00

# Resultado: Aprovado

# Essa função não deve retornar nenhuma informação.


# Requisitos
# Todas as funções devem possuir type hints.
# Todas devem possuir docstrings.
# calcular_comprometimento_renda() deve retornar float.
# analisar_emprestimo() deve retornar str.
# calcular_total_pagamento() deve retornar float.
# exibir_resultado() deve retornar None.
# Os cálculos devem acontecer dentro das funções responsáveis por eles.
# Não repita cálculos fora das funções.
# Os valores retornados pelas funções devem ser armazenados em variáveis e reutilizados nas próximas etapas.
# A função exibir_resultado() deve apenas receber os resultados já calculados e exibi-los.
# Não utilize *args, **kwargs, parâmetros com valores padrão ou outros recursos ainda não vistos nesta aula.

# Fluxo esperado

# dados do empréstimo
# ↓
# calcular comprometimento da renda
# ↓
# analisar empréstimo
# ↓
# calcular total do pagamento
# ↓
# exibir resultado final


# O objetivo é organizar um problema maior em funções menores, fazendo com que o retorno de uma etapa seja utilizado pelas próximas.


##########################################################


# 1
def calcular_comprometimento_renda(
    renda_mensal: float, parcela_emprestimo: float
) -> float:
    """
    Calcula o percentual da renda mensal comprometida pela parcela do empréstimo
    Args:
        renda_mensal:renda mensal do solicitante
        parcela_empréstimo: valor da parcela do empréstimo.
    Returns:
        Cálculo do percentual de comprometimento da renda
    """

    percentual = (parcela_emprestimo / renda_mensal) * 100
    return percentual


# 2
def analisar_emprestimo(
    renda_mensal: float, valor_emprestimo: float, percentual: float
) -> str:
    """
    Analisa e classifica o empréstimo solicitado.

    Args:
        renda_mensal: renda mensal do solicitante
        valor_emprestimo: valor do empréstimo solicitado
        percentual: percentual da renda comprometido pela parcela

    Returns:
        Classificação do empréstimo: "Aprovado", "Análise manual" ou "Recusado".
    """

    if percentual > 40.00:
        classificacao = "Recusado"
    elif percentual <= 40.00 and valor_emprestimo > renda_mensal * 5:
        classificacao = "Análise manual"
    else:
        classificacao = "Aprovado"

    return classificacao


# 3
def calcular_total_pagamento(
    parcela_emprestimo: float, quantidade_parcelas: int
) -> float:
    """
    Calcula o valor total pago ao final do empréstimo.

    Args:
        parcela_emprestimo: valor de cada parcela
        quantidade_parcelas: quantidade de parcelas do empréstimo

    Returns:
        Valor total a ser pago.
    """
    total_pago = parcela_emprestimo * quantidade_parcelas
    return total_pago


# 4
def exibir_resultado(
    valor_emprestimo: float, percentual: float, total_pago: float, classificacao: str
) -> None:
    """
    Exibe o resumo da análise do empréstimo.

    Args:

        valor_emprestimo: o valor do empréstimo solicitado
        percentual : percentual de comprometimento de renda, obtido na função 'calcular_comprometimento_renda'
        total_pago: : total pago ao final do empréstimo,obitida na função 'analisar_emprestimo'
        classificacao: classificação do empréstimo, obitida na função 'calcular_total_pagamento'
    """
    print("\n--- Análise do empréstimo ---\n")
    print(f"Valor solicitado: R$ {valor_emprestimo:.2f}")
    print(f"Comprometimento da renda: {percentual:.1f}%")
    print(f"Total a pagar: R$ {total_pago:.2f}")
    print(f"\nResultado: {classificacao}")


# Dados do empréstimo

renda_mensal = 3003.00
parcela_emprestimo = 850.00
valor_emprestimo = 15000.00
quantidade_parcelas = 24

# Fluxo: cada resultado guardado e usado na próxima etapa

percentual = calcular_comprometimento_renda(renda_mensal, parcela_emprestimo)
classificacao = analisar_emprestimo(renda_mensal, valor_emprestimo, percentual)
total_pago = calcular_total_pagamento(parcela_emprestimo, quantidade_parcelas)
exibir_resultado(valor_emprestimo, percentual, total_pago, classificacao)


##################  ###########  ######################

# correções:

# Parte final: as chamadas das funções
# python
# calcular_comprometimento_renda(renda_mensal, parcela_empréstimo)
# analisar_emprestimo(renda_mensal, valor_emprestimo, percentual)
# calcular_total_pagamento(parcela_empréstimo, quantidade_parcelas)
# exibir_resultado(percentual,total_pago,classificacao)

# A ordem está certa, seguindo o fluxo do enunciado. O problema é que os resultados não estão sendo guardados. É o mesmo erro do exercício 9.

# Erro 1: o return é chamado, mas o valor se perde

# Quando você escreve só:

# python
# calcular_comprometimento_renda(renda_mensal, parcela_empréstimo)

# a função roda, calcula 28.3 e devolve esse valor... mas ninguém está “segurando” ele. O valor some.

# Talvez você tenha pensado: “mas dentro da função existe uma variável chamada percentual”. Existe, mas ela só vive lá dentro. Quando a função termina, as variáveis de dentro desaparecem. Pense na função como uma cozinha fechada: ela entrega o prato pela janela (o return), e se ninguém pegar, o prato cai no chão. Fora dela, ninguém enxerga o que estava lá dentro.

# Por isso, na linha seguinte, percentual não existe e o Python dá:

# NameError: name 'percentual' is not defined

# A correção é guardar cada retorno em uma variável, que é exatamente o que o enunciado pede (“os valores retornados devem ser armazenados em variáveis e reutilizados”):

# python
# percentual = calcular_comprometimento_renda(renda_mensal, parcela_emprestimo)

# Agora sim existe uma variável percentual fora da função, que pode ser passada para a próxima.

# Erro 2: faltou um argumento na exibir_resultado()

# python
# exibir_resultado(percentual, total_pago, classificacao)

# A função foi criada com 4 parâmetros (valor_emprestimo, percentual,
# total_pago, classificacao), mas está sendo chamada com 3. Faltou o valor_emprestimo, e o Python daria TypeError: missing 1 required positional argument.

# Lembre que os valores entram na ordem dos parâmetros: o primeiro vai para o primeiro, e assim por diante.

# A parte final corrigida:


# Repare que as três primeiras linhas têm variável =
# função(...), porque essas funções devolvem algo. A última não tem, porque a exibir_resultado() só mostra e retorna None, então não há o que guardar.

# Com tudo junto, a saída fica:

# Sugestão: junte as correções no seu arquivo, rode, e me manda o código final para eu conferir. Se quiser testar os outros resultados, troque a parcela para 1500 (dá “Recusado”) ou o valor solicitado para 20000 (dá “Análise manual”).


##################  ###########  ######################


##################  ###########  ######################
