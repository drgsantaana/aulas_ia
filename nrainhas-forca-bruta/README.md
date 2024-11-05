# N-Rainhas - Força Bruta

## Sobre o Projeto

Este projeto implementa uma solução para o problema das N-Rainhas utilizando a abordagem de força bruta. O objetivo é posicionar `N` rainhas em um tabuleiro `N x N` de forma que nenhuma rainha ataque outra. Este código está configurado para encontrar a solução minimizando os conflitos entre as rainhas.

## Estrutura do Código

-   **nrainhas-minimizar.py**: Código principal que executa o algoritmo de força bruta para resolver o problema das N-Rainhas.

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
    cd aulas-ia/nrainhas-forca-bruta
    ```

4. Instale as bibliotecas necessárias.

    ```sh
        pip install -r requirements.txt
    ```

5. Execute o script desejado com o comando:

    ```sh
    python nrainhas-minimizar.py
    ```

## Configuração de Parâmetros

Para configurar o número de rainhas, o número de execuções, e outros parâmetros, edite as variáveis no código conforme necessário:

```python
# ==============================
# Inicialização de parâmetros EXEMPLO
# ==============================
n = 50          # Número de rainhas
execucoes = 5000       # Total de execuções (0 para infinito)
```
