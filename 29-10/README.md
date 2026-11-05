# Lista de Exercícios: Similaridade e Distância

Resolução em Python da `Lista_Exercicios_Similaridade_Distancia.pdf`.

| Arquivo | Exercício | Resumo |
| --- | --- | --- |
| `exercicio1.py` | 1 | Distância Euclidiana entre dois clientes, passo a passo (sem funções prontas) |
| `exercicio2.py` | 2 | Cliente mais próximo de A, com a distância calculada à mão |
| `exercicio3.py` | 3 | Distância Euclidiana com três atributos |
| `exercicio4.py` | 4 | Vários clientes com `math.dist()` |
| `exercicio5.py` | 5 | Influência da escala, com pandas e `MinMaxScaler` |
| `exercicio6.py` | 6 | Matriz de distâncias com `math.dist()` e pandas |

Os exercícios 1 a 3 (Parte A) não usam funções prontas de distância. Há um teste que confere isso lendo o código.

## Como rodar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python exercicio1.py     # e assim por diante, até exercicio6.py
pytest                   # roda os testes
```

## Observação sobre o exercício 6

Há um empate: A-C e B-D têm a mesma distância mínima, raiz de 2 (cerca de 1,4142). O programa mostra os dois pares.
