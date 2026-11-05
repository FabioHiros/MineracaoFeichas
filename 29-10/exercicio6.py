"""Exercício 6 - Matriz de distâncias entre registros."""

import math
from itertools import combinations

import numpy as np
import pandas as pd

registros = {
    "A": [1, 1],
    "B": [4, 5],
    "C": [2, 2],
    "D": [5, 4],
}


def matriz_de_distancias(registros):
    """28. e 29. Distância Euclidiana (math.dist) entre todos os pares, em um DataFrame."""
    nomes = list(registros)
    linhas = [[math.dist(registros[a], registros[b]) for b in nomes] for a in nomes]
    return pd.DataFrame(linhas, index=nomes, columns=nomes)


def menor_distancia_diferente_de_zero(matriz):
    """30. Menor valor diferente de zero da matriz."""
    valores = matriz.to_numpy()
    return valores[valores > 0].min()


def pares_mais_proximos(matriz):
    """31. Pares com a menor distância (mais de um par, se houver empate)."""
    menor = menor_distancia_diferente_de_zero(matriz)
    return [
        (a, b)
        for a, b in combinations(matriz.index, 2)
        if math.isclose(matriz.loc[a, b], menor)
    ]


def diagonal_e_zero(matriz):
    """32. A diagonal principal possui apenas zeros."""
    return bool((np.diag(matriz.to_numpy()) == 0).all())


def e_simetrica(matriz):
    """33. A matriz é simétrica: d(i, j) == d(j, i)."""
    return bool(np.allclose(matriz.to_numpy(), matriz.to_numpy().T))


def main():
    matriz = matriz_de_distancias(registros)
    print("Matriz de distâncias:")
    print(matriz.round(4), end="\n\n")

    print(f"Menor valor diferente de zero: {menor_distancia_diferente_de_zero(matriz):.4f}")
    pares = ", ".join(f"{a}-{b}" for a, b in pares_mais_proximos(matriz))
    print(f"Par(es) de registros mais próximo(s): {pares}")

    # A diagonal é zero porque d(A, A) é a distância de um registro até ele mesmo: todas as
    # diferenças são 0, então a soma dos quadrados e a raiz também são 0.
    print(f"Diagonal principal só com zeros: {diagonal_e_zero(matriz)}")

    # d(A, B) = d(B, A) porque a diferença é elevada ao quadrado: (a - b)² = (b - a)².
    # A ordem dos registros não muda o resultado, então a matriz é simétrica.
    print(f"Matriz simétrica: {e_simetrica(matriz)}")


if __name__ == "__main__":
    main()
