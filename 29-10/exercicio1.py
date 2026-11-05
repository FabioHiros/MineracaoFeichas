"""Exercício 1 - Distância Euclidiana entre dois clientes.

Restrição: sem math.dist() nem qualquer função pronta de distância.
"""

# 1. Armazenar os dados dos clientes em listas: [idade, compras por mês]
cliente_a = [25, 2]
cliente_b = [28, 6]


def distancia_euclidiana_passo_a_passo(a, b):
    """Devolve cada etapa do cálculo da distância Euclidiana entre dois clientes."""
    diferenca_idade = a[0] - b[0]  # 2. diferença entre as idades
    diferenca_compras = a[1] - b[1]  # 3. diferença entre as quantidades de compras
    quadrado_idade = diferenca_idade**2  # 4. cada diferença ao quadrado
    quadrado_compras = diferenca_compras**2
    soma = quadrado_idade + quadrado_compras  # 5. soma dos quadrados
    distancia = soma**0.5  # 6. raiz quadrada da soma
    return {
        "diferenca_idade": diferenca_idade,
        "diferenca_compras": diferenca_compras,
        "quadrado_idade": quadrado_idade,
        "quadrado_compras": quadrado_compras,
        "soma": soma,
        "distancia": distancia,
    }


def main():
    passos = distancia_euclidiana_passo_a_passo(cliente_a, cliente_b)
    print(f"Diferença entre as idades: {passos['diferenca_idade']}")
    print(f"Diferença entre as compras: {passos['diferenca_compras']}")
    print(f"Quadrados: {passos['quadrado_idade']} e {passos['quadrado_compras']}")
    print(f"Soma dos quadrados: {passos['soma']}")
    # 7. exibir a distância Euclidiana entre os dois clientes
    print(f"Distância Euclidiana entre A e B: {passos['distancia']:.4f}")


if __name__ == "__main__":
    main()
