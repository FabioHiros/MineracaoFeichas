"""Exercício 3 - Distância Euclidiana com três atributos.

Restrição: sem funções prontas de distância.
"""

# [nota média, frequência (%), horas de estudo por semana]
aluno_a = [8.0, 92, 10]
aluno_b = [7.8, 90, 9]
aluno_c = [5.2, 68, 3]


def distancia_euclidiana(a, b):
    """Raiz da soma dos quadrados das diferenças, para qualquer quantidade de atributos."""
    soma_dos_quadrados = 0
    for valor_a, valor_b in zip(a, b):
        soma_dos_quadrados += (valor_a - valor_b) ** 2
    return soma_dos_quadrados**0.5


def main():
    # 14. e 15. distâncias de A até B e de A até C
    distancia_ab = distancia_euclidiana(aluno_a, aluno_b)
    distancia_ac = distancia_euclidiana(aluno_a, aluno_c)

    # 16. exibir os dois resultados
    print(f"Distância entre A e B: {distancia_ab:.4f}")
    print(f"Distância entre A e C: {distancia_ac:.4f}")

    # 17. aluno mais próximo de A
    mais_proximo = "B" if distancia_ab < distancia_ac else "C"
    print(f"Aluno mais próximo de A: {mais_proximo}")

    # A mesma lógica usada com dois atributos serve para três: basta somar mais um termo ao
    # quadrado da diferença antes de tirar a raiz. A função acima aceita qualquer número de
    # atributos.


if __name__ == "__main__":
    main()
