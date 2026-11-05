"""Exercício 4 - Comparando vários clientes com math.dist()."""

import math  # 18. importar o módulo math

# [idade, compras por mês]
clientes = {
    "A": [25, 2],
    "B": [27, 3],
    "C": [30, 5],
    "D": [45, 10],
    "E": [52, 12],
}


def distancias_ate_a(clientes):
    """19. Distância de A para cada um dos outros clientes, com math.dist()."""
    referencia = clientes["A"]
    return {nome: math.dist(referencia, dados) for nome, dados in clientes.items() if nome != "A"}


def main():
    distancias = distancias_ate_a(clientes)

    # 20. exibir cada distância calculada
    for nome, distancia in distancias.items():
        print(f"Distância entre A e {nome}: {distancia:.4f}")

    # 21. identificar automaticamente o cliente mais próximo de A
    mais_proximo = min(distancias, key=distancias.get)
    print(
        f"O cliente {mais_proximo} possui o perfil mais próximo de A considerando idade "
        f"e compras por mês (distância {distancias[mais_proximo]:.4f})."
    )


if __name__ == "__main__":
    main()
