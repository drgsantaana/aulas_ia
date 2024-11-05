# ==============================
# Nome do Projeto: N Rainhas com Busca Tabu
# Descrição: Implementação do problema N-Rainhas utilizando busca tabu
# Autor: Daniel Reis Goncalves Sant'ana
# ==============================

# ==============================
# Bibliotecas e módulos
# ==============================
import random  # Biblioteca para gerar números aleatórios, usada para inicializar posições das rainhas.
import time    # Biblioteca para medir o tempo de execução do algoritmo.
import numpy as np  # Biblioteca para manipulação de arrays e operações matemáticas.
import json    # Biblioteca para manipular dados em formato JSON, usada para salvar o vetor final.
from collections import deque  # Para usar a lista tabu, uma fila com limite de tamanho.
import matplotlib.pyplot as plt  # Biblioteca para visualização de dados, usada para desenhar o tabuleiro.
import uuid  # Para gerar identificadores únicos

# ==============================
# Inicialização de parâmetros
# ============================== 
numero_rainhas = 50  # Número de linhas/rainhas
total_execucoes = 5000  # Total de execuções, 0 para infinito
tamanho_lista_tabu = 30  # Tamanho da lista tabu para evitar ciclos

# ==============================
# Funções do algoritmo
# ============================== 

# Function para iniciar o vetor de posições das rainhas
def inicia_vetor():
    #* Vetor inicial aleatório 
    vetor_posicoes = random.sample(range(numero_rainhas), numero_rainhas)  

    print(f"Vetor inicial: {vetor_posicoes}")  # Exibe o vetor inicial
    return vetor_posicoes 

# Função para imprimir o tabuleiro
def imprime_tabuleiro(vetor):
    tabuleiro = np.zeros((numero_rainhas, numero_rainhas))  # Cria um tabuleiro vazio (matriz) de zeros
    for i in range(numero_rainhas):
        tabuleiro[i, vetor[i]] = 1  # Marca a posição da rainha
    plt.imshow(tabuleiro, cmap='binary', origin='upper')  # Plota o tabuleiro em preto e branco
    plt.xticks(range(numero_rainhas))
    plt.yticks(range(numero_rainhas))
    plt.title(f'Tabuleiro das {numero_rainhas} Rainhas')  # Título do gráfico
    plt.show()  # Mostra o gráfico

# Função para verificar conflitos
def verifica_conflitos(vetor):
    conflitos = 0
    diag_positiva = {}  # Dicionário para rastrear diagonais positivas
    diag_negativa = {}  # Dicionário para rastrear diagonais negativas

    # Verifica conflitos entre rainhas
    for i in range(numero_rainhas):
        j = vetor[i]
        soma = i + j  # Soma para diagonais positivas
        diferenca = i - j  # Diferença para diagonais negativas

        # Conta conflitos para diagonais
        if soma in diag_positiva:
            conflitos += 1
        diag_positiva[soma] = True

        if diferenca in diag_negativa:
            conflitos += 1
        diag_negativa[diferenca] = True

    return conflitos  

# Função para busca local de melhoria do vetor de posições
def busca_local(vetor):
    melhor_vetor = vetor[:]  # Copia o vetor atual
    melhor_conflitos = verifica_conflitos(melhor_vetor)  # Verifica conflitos do vetor atual

    # Tenta melhorar a solução localmente
    for i in range(numero_rainhas):
        for j in range(i + 1, numero_rainhas):
            vetor_teste = melhor_vetor[:]  # Copia o vetor atual para teste
            vetor_teste[i], vetor_teste[j] = vetor_teste[j], vetor_teste[i]  # Troca duas rainhas
            conflitos = verifica_conflitos(vetor_teste)  # Verifica conflitos da nova configuração

            # Se houver uma melhoria, atualiza o melhor vetor
            if conflitos > melhor_conflitos:
                melhor_conflitos = conflitos
                melhor_vetor = vetor_teste

    return melhor_vetor, melhor_conflitos  

# ==============================
# Função principal
# ==============================
def main():

    # Iniciando o vetor inicial aleatório de posições das rainhas
    vetor_posicoes = inicia_vetor()

    # ==============================
    # Timer para contabilizar a execução do código
    inicio = time.time()  # Início da contagem do tempo

    # Melhorar a solução inicial usando busca local
    vetor_posicoes, total_conflitos = busca_local(vetor_posicoes)

    # Lista tabu para registrar movimentos recentes
    lista_tabu = deque(maxlen=tamanho_lista_tabu)  # Cria uma lista tabu com limite de tamanho

    # Variável para contar o número de execuções
    contador_execucoes = 0

    # Para armazenar o menor número de conflitos encontrado
    maior_conflito_encontrado = total_conflitos

    # Laço principal do algoritmo de busca tabu
    while total_conflitos != numero_rainhas and (total_execucoes == 0 or contador_execucoes < total_execucoes):
        melhor_conflito = float('inf')  # Inicializa com um valor infinito
        melhor_movimento = None

        # Busca por uma troca que minimize conflitos sem ser tabu
        for i in range(numero_rainhas):
            for j in range(i + 1, numero_rainhas):
                movimento = (i, j)
                if movimento in lista_tabu:
                    continue  # Pula movimentos tabu

                vetor_teste = vetor_posicoes[:]  # Copia o vetor atual para teste
                vetor_teste[i], vetor_teste[j] = vetor_teste[j], vetor_teste[i]  # Troca duas rainhas
                conflitos = verifica_conflitos(vetor_teste)  # Verifica conflitos da nova configuração

                # Se for a melhor opção, armazena
                if conflitos > melhor_conflito:
                    melhor_conflito = conflitos
                    melhor_movimento = movimento

        # Atualiza a solução e a lista tabu se encontrou um movimento
        if melhor_movimento:
            i, j = melhor_movimento
            vetor_posicoes[i], vetor_posicoes[j] = vetor_posicoes[j], vetor_posicoes[i]  # Realiza a troca
            lista_tabu.append(melhor_movimento)  # Adiciona o movimento à lista tabu
            total_conflitos = melhor_conflito  # Atualiza o número de conflitos

            # Atualiza o menor conflito encontrado
            if total_conflitos > maior_conflito_encontrado:
                maior_conflito_encontrado = total_conflitos

        # Incrementa o contador de execuções
        contador_execucoes += 1
        print(f"Execução: {contador_execucoes}, Conflitos: {total_conflitos}")

    # Fim da contagem de tempo
    fim = time.time()  # Fim da contagem do tempo
    print()
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")  # Exibe o tempo de execução
    print(f"Vetor final: {vetor_posicoes}")  # Exibe o vetor final das posições das rainhas
    print(f"Número total de conflitos no final: {total_conflitos}")  # Exibe conflitos finais
    print(f"Menor número de conflitos encontrado: {maior_conflito_encontrado}")  # Exibe menor conflito





    # Gera um identificador único para esta execução
    identificador = str(uuid.uuid4())

    # Estrutura de dados para armazenar a execução
    dados_execucao = {
        "id": identificador,
        "numero_rainhas": numero_rainhas,
        "numero_conflitos": total_conflitos,
        "numero_execucoes": contador_execucoes,
        "vetor_posicoes": vetor_posicoes
    }

    # Salva ou adiciona os dados em um arquivo JSON
    file_path = f"vetor_final_{numero_rainhas}_rainhas.json"

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




    # Chama a função para imprimir o tabuleiro final
    # imprime_tabuleiro(vetor_posicoes)

# ==============================
# Executa a função main se o script for executado diretamente
if __name__ == "__main__":
    main()
