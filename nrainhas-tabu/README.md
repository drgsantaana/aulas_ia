# N-Rainhas - Busca com Memória Tabu

## Sobre o Projeto

Este projeto implementa uma solução para o problema das N-Rainhas utilizando a técnica de busca com memória tabu. A abordagem visa minimizar ou maximizar conflitos, dependendo do script executado, com a ajuda de uma lista tabu para evitar ciclos e melhorar a eficiência da busca.

## Estrutura do Código

-   **nrainhas-minimizar.py**: Código que executa a busca tabu para resolver o problema das N-Rainhas minimizando conflitos.
-   **nrainhas-maximizar.py**: Código que executa a busca tabu para tentar encontrar a pior solução possível, maximizando os conflitos entre as rainhas.

## Como Executar

1. Certifique-se de que o Python está instalado.

    ```sh
    sudo apt update
    sudo apt install python3 python3-pip
    ```

2. Clonando o Repositório.

    ```sh
    git clone https://github.com/drgsantaana/aulas-ia
    ```

3. Navegue até o diretório `nrainhas-tabu`.

    ```sh
    cd aulas-ia/nrainhas-tabu
    ```

4. Instale as bibliotecas necessárias.

    ```sh
        pip install -r requirements.txt
    ```

5. Execute o script desejado com o comando:

    ```sh
    # Para encontrar a solução minimizando conflitos
    python nrainhas-minimizar.py

    # Para encontrar a solução maximizando conflitos
    python nrainhas-maximizar.py
    ```

## Configuração de Parâmetros

No início de cada script, há variáveis que permitem configurar o número de rainhas, o limite de execuções e o tamanho da lista tabu. Edite esses valores conforme necessário para ajustar a busca:

```python
# ==============================
# Inicialização de parâmetros EXEMPLO
# ==============================
numero_rainhas = 50          # Número de rainhas
total_execucoes = 5000       # Total de execuções (0 para infinito)
tamanho_lista_tabu = 30      # Tamanho da lista tabu para evitar ciclos
```

## Requisitos

Python 3.x
Bibliotecas: random, numpy, json, collections, uuid
Para instalar as bibliotecas necessárias:

```sh
    pip install -r requirements.txt
```
