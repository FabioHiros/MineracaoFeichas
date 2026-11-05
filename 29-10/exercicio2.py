"""Exercício 2 - Qual cliente é mais semelhante ao cliente A?

Restrição: sem funções prontas de distância.
"""

# [idade, compras por mês]
cliente_a = [25, 2]
cliente_b = [27, 3]
cliente_c = [45, 10]
cliente_d = [52, 12]


def distancia_euclidiana(a, b):
    """Distância Euclidiana calculada manualmente: raiz da soma dos quadrados das diferenças."""
    soma_dos_quadrados = 0
    for valor_a, valor_b in zip(a, b):
        soma_dos_quadrados += (valor_a - valor_b) ** 2
    return soma_dos_quadrados**0.5


def cliente_mais_proximo(referencia, candidatos):
    """Devolve (nome, distância) do candidato com a menor distância até a referência."""
    distancias = {nome: distancia_euclidiana(referencia, dados) for nome, dados in candidatos.items()}
    nome = min(distancias, key=distancias.get)
    return nome, distancias[nome]


def main():
    candidatos = {"B": cliente_b, "C": cliente_c, "D": cliente_d}
    # 8, 9 e 10. distâncias de A até B, C e D
    distancias = {nome: distancia_euclidiana(cliente_a, dados) for nome, dados in candidatos.items()}

    # 11. comparar os três resultados
    for nome, distancia in distancias.items():
        print(f"Distância entre A e {nome}: {distancia:.4f}")

    # 12. e 13. cliente com a menor distância em relação ao cliente A
    nome, distancia = cliente_mais_proximo(cliente_a, candidatos)
    print(f"Cliente mais próximo de A: {nome} (distância {distancia:.4f})")

    # A distância Euclidiana mede o quão afastados estão dois clientes no espaço formado pelos
    # atributos (idade e compras por mês). Quanto menor a distância, mais próximos estão os
    # valores de cada atributo, ou seja, mais parecidos são os perfis. Por isso a menor
    # distância indica a maior semelhança segundo os atributos utilizados.


if __name__ == "__main__":
    main()
