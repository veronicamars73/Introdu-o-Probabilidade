import numpy as np

# Definiremos nosso espaço amostral como uma lista de todos os valores de um dado
espaco_amostral = [1,2,3,4,5,6]

# Definiremos nossos casos favoráveis como uma lista valores pares de um dado
favoraveis = [2,4,6]

# Definiremos nosso contador de lançamentos com resultados pares
resultados_pares = 0

# Agora escreveremos nosso iterador com nossos lançamentos
for i in range (10000):
	# np.random.choice escolhe um dos valores no espaço amostral, ou seja, algum valor entre (1,2,3,4,5,6)
    x = np.random.choice(espaco_amostral)
    """O comando x in favoráveis checa se o valor escolhido
    está na nossa lista de favoráveis, ou seja, se é 2, 4 ou 6
    """
    if(x in favoraveis):
        resultados_pares += 1

