# ==============================
# Nome do Projeto: N Rainhas com Busca Tabu
# Descrição: Implementação do problema N-Rainhas utilizando busca tabu
# Autor: Daniel Reis Goncalves Sant'ana
# ==============================

# ==============================
# Importações
# Aqui são importados os módulos e bibliotecas necessários para o funcionamento do projeto
import random  # Para gerar números aleatórios, utilizados na inicialização das posições das rainhas.
import time    # Para medir o tempo de execução do algoritmo.
import numpy as np  # Para manipulação de arrays e operações matemáticas.
import json    # Para manipulação de dados em formato JSON, usado para salvar o vetor final.
import uuid  # Para gerar identificadores únicos

# ==============================

# ==============================
# Parâmetros iniciais
# Aqui é configurado os parâmetros iniciais e comportamento do código
n = 100  # Número de linhas/rainhas
execucoes = 10000  # Total de execuções, 0 para infinito
# ==============================

# ==============================
# Iniciando vetores e variáveis
#* Vetor inicial aleatório de posições das rainhas
vetS = random.sample(range(n), n)  # Gera uma lista aleatória de posições para as rainhas.

#* Vetor inicial com posições predefinidas
# vetS = (1,2,3,4,5)  # Exemplo de vetor predefinido (comentar/alterar conforme necessidade).

#* Vetor inicial com um vetor salvo anteriormente em arquivo
# with open(f"vetor_final_{n}_rainhas.json", "r") as arquivo:
#     vetS = json.load(arquivo)  # Carrega um vetor previamente salvo a partir de um arquivo JSON.

print(f"Vetor inicial: {vetS}")  # Exibe o vetor inicial gerado.

# ==============================

# ==============================
# Timer vai contabilizar todo o código dentro deste bloco
inicio = time.time()  # Marca o início da contagem do tempo

# Gera diagonal positiva e negativa
dp = np.zeros((n, n), dtype=np.int64)  # Cria uma matriz para as diagonais positivas.
dn = np.zeros((n, n), dtype=np.int64)  # Cria uma matriz para as diagonais negativas.

# Preenche as matrizes de diagonais
for i in range(n):
    for j in range(n):
        dp[i][j] = i + j  # Preenche a matriz de diagonais positivas.
        dn[i][j] = i - j  # Preenche a matriz de diagonais negativas.
# Fim gera diagonal positiva e negativa

# Função para verificar conflitos no vetor de posições das rainhas
def verificaFit(vet):
    conflitos = 0  # Contador de conflitos
    diagonal_positiva = {}  # Dicionário para rastrear diagonais positivas
    diagonal_negativa = {}  # Dicionário para rastrear diagonais negativas

    # Verifica conflitos entre as rainhas
    for i in range(n):
        j = vet[i]  # Posição da rainha na linha i
        
        # Calcular soma e diferença para identificar diagonais
        soma = i + j  # Soma para diagonais positivas
        diferenca = i - j  # Diferença para diagonais negativas

        # Verifica conflito na diagonal positiva
        if soma in diagonal_positiva:
            conflitos += 1  # Incrementa conflitos se já houver uma rainha nesta diagonal
        diagonal_positiva[soma] = True  # Marca a diagonal como ocupada

        # Verifica conflito na diagonal negativa
        if diferenca in diagonal_negativa:
            conflitos += 1  # Incrementa conflitos se já houver uma rainha nesta diagonal
        diagonal_negativa[diferenca] = True  # Marca a diagonal como ocupada
    
    print(f"Número total de conflitos: {conflitos}")  # Exibe o número de conflitos encontrados
    return conflitos  # Retorna o total de conflitos

# Verifica a fitness do vetor inicial
total_conflitos = verificaFit(vetS)  # Avalia o vetor inicial para determinar o número de conflitos.

r = 0  # Execução inicial
# Loop principal que continua enquanto houver conflitos
while total_conflitos != 0 and (execucoes == 0 or r < execucoes):
    # Gera duas posições aleatórias diferentes
    posicao1 = random.randint(0, n - 1)  # Seleciona a primeira posição aleatória
    posicao2 = random.randint(0, n - 1)  # Seleciona a segunda posição aleatória
    while posicao2 == posicao1:  # Garante que as posições sejam diferentes
        posicao2 = random.randint(0, n - 1)

    # Faz uma cópia do vetor para modificar
    geraVetor = vetS[:]  # Cópia do vetor atual
    
    # Troca as posições das rainhas nas duas posições escolhidas
    geraVetor[posicao1], geraVetor[posicao2] = geraVetor[posicao2], geraVetor[posicao1]

    # Verifica se a nova configuração é melhor (com menos conflitos)
    if verificaFit(geraVetor) < total_conflitos:
        vetS = geraVetor  # Atualiza o vetor se a nova configuração for melhor
        total_conflitos = verificaFit(vetS)  # Atualiza o total de conflitos
    
    r += 1  # Incrementa o contador de execuções

# Fim da contabilização de tempo
fim = time.time()  # Marca o fim da contagem do tempo
# ============================== 

# Exibe resultados finais
print(f"Tempo de execução: {fim - inicio:.6f} segundos")  # Mostra o tempo total de execução
print(f"Vetor final: {vetS}")  # Exibe o vetor final das posições das rainhas.

# Gera um identificador único para esta execução
identificador = str(uuid.uuid4())

# Estrutura de dados para armazenar a execução
dados_execucao = {
    "id": identificador,
    "numero_rainhas": n,
    "numero_conflitos": total_conflitos,
    "numero_execucoes": r,
    "vetor_posicoes": vetS
}

# Salva ou adiciona os dados em um arquivo JSON
file_path = f"vetor_final_{n}_rainhas_BRUTE.json"

# Carrega dados existentes, se houver
try:
    with open(file_path, "r") as arquivo:
        dados_existentes = json.load(arquivo)
except FileNotFoundError:
    dados_existentes = []

# Adiciona a nova execução
dados_existentes.append(dados_execucao)

# Salva os dados atualizados de volta no arquivo
with open(file_path, "w") as arquivo:
    json.dump(dados_existentes, arquivo, indent=4)

print(f"Vetor salvo com sucesso em '{file_path}'")  # Confirmação de salvamento

# ============================== 
# # Imprime o tabuleiro final (opcional)
# for i in range(n):
#     for j in range(n):
#         if j == vetS[i]:
#             print("1", end=" ")  # Imprime 1 (representa a presença de uma rainha)
#         else:
#             print("0", end=" ")  # Imprime 0 (representa um espaço vazio)
#     print()  # Nova linha para cada linha do tabuleiro
# # ============================== 
