"""Exercício 5 - Influência da escala e normalização."""

import math

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

COLUNAS = ["Idade", "Renda"]


def criar_dataframe():
    """22. DataFrame com a base de clientes."""
    return pd.DataFrame(
        {
            "Idade": [20, 25, 40, 55, 70],
            "Renda": [2000, 3000, 6000, 9000, 12000],
        },
        index=["A", "B", "C", "D", "E"],
    )


def normalizar(df):
    """24. Normaliza Idade e Renda para [0, 1] com MinMaxScaler."""
    escalador = MinMaxScaler()
    return pd.DataFrame(escalador.fit_transform(df[COLUNAS]), columns=COLUNAS, index=df.index)


def distancia_entre(df, nome_1, nome_2):
    return math.dist(df.loc[nome_1, COLUNAS], df.loc[nome_2, COLUNAS])


def main():
    df = criar_dataframe()
    print("Base original:")
    print(df, end="\n\n")

    # 23. distância entre A e B com os valores originais
    distancia_original = distancia_entre(df, "A", "B")
    print(f"Distância A-B com valores originais: {distancia_original:.4f}")

    # 25. DataFrame com os valores normalizados
    df_normalizado = normalizar(df)
    print("\nBase normalizada (MinMaxScaler):")
    print(df_normalizado, end="\n\n")

    # 26. distância entre A e B com os valores normalizados
    distancia_normalizada = distancia_entre(df_normalizado, "A", "B")
    print(f"Distância A-B com valores normalizados: {distancia_normalizada:.4f}")

    # 27. comparar os dois resultados
    print(f"\nA distância original é {distancia_original / distancia_normalizada:.0f} vezes maior.")

    # A renda tem influência muito maior na distância com os valores originais porque está em
    # uma escala muito maior que a idade. Entre A e B, a diferença de idade é 5 anos e a de
    # renda é R$ 1.000. Ao elevar ao quadrado, a renda contribui com 1.000.000 e a idade com
    # apenas 25, então a distância (cerca de 1000,01) praticamente só reflete a renda e a idade
    # quase não pesa. Depois da normalização as duas variáveis ficam entre 0 e 1, e cada uma
    # contribui de forma proporcional à sua variação: a diferença passa a ser 0,1 em ambas,
    # e a distância cai para cerca de 0,1414.


if __name__ == "__main__":
    main()
