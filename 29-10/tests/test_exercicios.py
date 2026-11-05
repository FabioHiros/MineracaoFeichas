import ast
import math
from pathlib import Path

import pandas as pd
import pytest

import exercicio1
import exercicio2
import exercicio3
import exercicio4
import exercicio5
import exercicio6

RAIZ = Path(__file__).resolve().parent.parent
MODULOS_SEM_FUNCOES_PRONTAS = ["exercicio1.py", "exercicio2.py", "exercicio3.py"]
NOMES_PROIBIDOS = {"dist", "pdist", "cdist", "norm", "euclidean", "hypot"}
MODULOS_PROIBIDOS = {"math", "scipy", "sklearn"}


# Restrição da Parte A: nada de funções prontas de distância


@pytest.mark.parametrize("arquivo", MODULOS_SEM_FUNCOES_PRONTAS)
def test_parte_a_nao_usa_funcoes_prontas_de_distancia(arquivo):
    arvore = ast.parse((RAIZ / arquivo).read_text(encoding="utf-8"))

    for no in ast.walk(arvore):
        if isinstance(no, ast.Import):
            assert not {a.name.split(".")[0] for a in no.names} & MODULOS_PROIBIDOS
        if isinstance(no, ast.ImportFrom):
            assert no.module.split(".")[0] not in MODULOS_PROIBIDOS
        if isinstance(no, ast.Attribute):
            assert no.attr not in NOMES_PROIBIDOS
        if isinstance(no, ast.Name):
            assert no.id not in NOMES_PROIBIDOS


# Exercício 1


def test_exercicio1_distancia_entre_a_e_b_e_5():
    passos = exercicio1.distancia_euclidiana_passo_a_passo(exercicio1.cliente_a, exercicio1.cliente_b)

    assert passos["distancia"] == 5.0


def test_exercicio1_etapas_do_calculo():
    passos = exercicio1.distancia_euclidiana_passo_a_passo([25, 2], [28, 6])

    assert passos["diferenca_idade"] == -3
    assert passos["diferenca_compras"] == -4
    assert passos["quadrado_idade"] == 9
    assert passos["quadrado_compras"] == 16
    assert passos["soma"] == 25


def test_exercicio1_saida(capsys):
    exercicio1.main()

    assert "Distância Euclidiana entre A e B: 5.0000" in capsys.readouterr().out


# Exercício 2


@pytest.mark.parametrize(
    "outro, esperado",
    [
        (exercicio2.cliente_b, math.sqrt(5)),
        (exercicio2.cliente_c, math.sqrt(464)),
        (exercicio2.cliente_d, math.sqrt(829)),
    ],
)
def test_exercicio2_distancias_a_partir_do_cliente_a(outro, esperado):
    assert exercicio2.distancia_euclidiana(exercicio2.cliente_a, outro) == pytest.approx(esperado)


def test_exercicio2_distancia_para_si_mesmo_e_zero():
    assert exercicio2.distancia_euclidiana([25, 2], [25, 2]) == 0


def test_exercicio2_cliente_mais_proximo_e_o_b():
    candidatos = {"B": exercicio2.cliente_b, "C": exercicio2.cliente_c, "D": exercicio2.cliente_d}

    nome, distancia = exercicio2.cliente_mais_proximo(exercicio2.cliente_a, candidatos)

    assert nome == "B"
    assert distancia == pytest.approx(math.sqrt(5))


def test_exercicio2_saida(capsys):
    exercicio2.main()
    saida = capsys.readouterr().out

    assert "Distância entre A e B: 2.2361" in saida
    assert "Distância entre A e C: 21.5407" in saida
    assert "Distância entre A e D: 28.7924" in saida
    assert "Cliente mais próximo de A: B" in saida


# Exercício 3


def test_exercicio3_distancias_com_tres_atributos():
    assert exercicio3.distancia_euclidiana(exercicio3.aluno_a, exercicio3.aluno_b) == pytest.approx(
        math.sqrt(5.04)
    )
    assert exercicio3.distancia_euclidiana(exercicio3.aluno_a, exercicio3.aluno_c) == pytest.approx(
        math.sqrt(632.84)
    )


def test_exercicio3_confere_com_math_dist():
    for outro in (exercicio3.aluno_b, exercicio3.aluno_c):
        assert exercicio3.distancia_euclidiana(exercicio3.aluno_a, outro) == pytest.approx(
            math.dist(exercicio3.aluno_a, outro)
        )


def test_exercicio3_saida(capsys):
    exercicio3.main()
    saida = capsys.readouterr().out

    assert "Distância entre A e B: 2.2450" in saida
    assert "Distância entre A e C: 25.1563" in saida
    assert "Aluno mais próximo de A: B" in saida


# Exercício 4


def test_exercicio4_distancias_a_partir_de_a():
    distancias = exercicio4.distancias_ate_a(exercicio4.clientes)

    assert list(distancias) == ["B", "C", "D", "E"]
    assert distancias["B"] == pytest.approx(math.sqrt(5))
    assert distancias["C"] == pytest.approx(math.sqrt(34))
    assert distancias["D"] == pytest.approx(math.sqrt(464))
    assert distancias["E"] == pytest.approx(math.sqrt(829))


def test_exercicio4_saida(capsys):
    exercicio4.main()
    saida = capsys.readouterr().out

    assert "Distância entre A e E: 28.7924" in saida
    assert "O cliente B possui o perfil mais próximo de A" in saida


# Exercício 5


def test_exercicio5_dataframe():
    df = exercicio5.criar_dataframe()

    assert list(df.index) == ["A", "B", "C", "D", "E"]
    assert list(df.columns) == ["Idade", "Renda"]
    assert df.loc["C"].tolist() == [40, 6000]


def test_exercicio5_distancia_com_valores_originais_e_dominada_pela_renda():
    df = exercicio5.criar_dataframe()

    distancia = exercicio5.distancia_entre(df, "A", "B")

    assert distancia == pytest.approx(math.sqrt(25 + 1_000_000))
    assert distancia == pytest.approx(1000, abs=0.1)


def test_exercicio5_normalizacao_leva_as_colunas_para_0_e_1():
    normalizado = exercicio5.normalizar(exercicio5.criar_dataframe())

    assert normalizado.min().tolist() == [0.0, 0.0]
    assert normalizado.max().tolist() == [1.0, 1.0]
    assert normalizado.loc["B"].tolist() == pytest.approx([0.1, 0.1])
    assert normalizado.loc["C"].tolist() == pytest.approx([0.4, 0.4])


def test_exercicio5_distancia_normalizada_pesa_idade_e_renda_igualmente():
    normalizado = exercicio5.normalizar(exercicio5.criar_dataframe())

    assert exercicio5.distancia_entre(normalizado, "A", "B") == pytest.approx(math.sqrt(0.02))


def test_exercicio5_normalizar_nao_altera_o_dataframe_original():
    df = exercicio5.criar_dataframe()

    exercicio5.normalizar(df)

    assert df.loc["E"].tolist() == [70, 12000]


def test_exercicio5_saida(capsys):
    exercicio5.main()
    saida = capsys.readouterr().out

    assert "Distância A-B com valores originais: 1000.0125" in saida
    assert "Distância A-B com valores normalizados: 0.1414" in saida


# Exercício 6


@pytest.fixture
def matriz():
    return exercicio6.matriz_de_distancias(exercicio6.registros)


def test_exercicio6_matriz_tem_um_registro_por_linha_e_coluna(matriz):
    assert isinstance(matriz, pd.DataFrame)
    assert list(matriz.index) == ["A", "B", "C", "D"]
    assert list(matriz.columns) == ["A", "B", "C", "D"]


def test_exercicio6_valores_da_matriz(matriz):
    assert matriz.loc["A", "B"] == pytest.approx(5.0)
    assert matriz.loc["A", "C"] == pytest.approx(math.sqrt(2))
    assert matriz.loc["A", "D"] == pytest.approx(5.0)
    assert matriz.loc["B", "C"] == pytest.approx(math.sqrt(13))
    assert matriz.loc["B", "D"] == pytest.approx(math.sqrt(2))
    assert matriz.loc["C", "D"] == pytest.approx(math.sqrt(13))


def test_exercicio6_menor_distancia_diferente_de_zero(matriz):
    assert exercicio6.menor_distancia_diferente_de_zero(matriz) == pytest.approx(math.sqrt(2))


def test_exercicio6_ha_empate_entre_dois_pares_mais_proximos(matriz):
    assert exercicio6.pares_mais_proximos(matriz) == [("A", "C"), ("B", "D")]


def test_exercicio6_diagonal_so_tem_zeros(matriz):
    assert exercicio6.diagonal_e_zero(matriz)


def test_exercicio6_matriz_e_simetrica(matriz):
    assert exercicio6.e_simetrica(matriz)


def test_exercicio6_detecta_matriz_que_nao_e_simetrica_nem_tem_diagonal_zero():
    invalida = pd.DataFrame([[1.0, 2.0], [3.0, 0.0]], index=["A", "B"], columns=["A", "B"])

    assert not exercicio6.diagonal_e_zero(invalida)
    assert not exercicio6.e_simetrica(invalida)


def test_exercicio6_saida(capsys):
    exercicio6.main()
    saida = capsys.readouterr().out

    assert "Par(es) de registros mais próximo(s): A-C, B-D" in saida
    assert "Diagonal principal só com zeros: True" in saida
    assert "Matriz simétrica: True" in saida
