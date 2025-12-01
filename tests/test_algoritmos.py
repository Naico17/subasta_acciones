import pytest

# Importar implementaciones de los algoritmos 
from src.fuerza_bruta import fuerza_bruta
# from src.recursiva import subasta_recursiva
# from src.memo import subasta_memo
# from src.dinamica import subasta_dp

# Lista centralizada de algoritmos a probar
ALGORITMOS = [
    fuerza_bruta,
    # subasta_recursiva,
    # subasta_memo,
    # subasta_dp
]


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_instancia_pequena(alg):
    """
    Caso base del enunciado: 10 acciones, 3 ofertas.
    Solución óptima: 4 acciones al oferente 1 (precio 100) y 6 al oferente 2 (precio 90).
    Ganancia = 4*100 + 6*90 = 940.
    """
    A = 10
    N = 3
    l = [1, 6, 1]
    u = [5, 10, 10]
    p = [100, 90, 5]

    resultado = alg(A, N, l, u, p)
    assert resultado == 940


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_mejor_oferta_parcial(alg):
    """
    No se pueden vender las 10 acciones completas, pero sí es óptimo vender 9 al oferente 2,
    ya que su oferta [9,9] es factible (9 ≤ A=10) y da mayor ganancia que la oferta 1.
    Ganancia = 9 * 60 = 540.
    """
    A = 10
    N = 2
    l = [8, 9]
    u = [8, 9]
    p = [50, 60]

    resultado = alg(A, N, l, u, p)
    assert resultado == 540


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_sin_ofertas_factibles(alg):
    """
    Todas las ofertas tienen mínimo > A, por lo que ninguna puede ser aceptada.
    La única opción es no vender nada → ganancia = 0.
    """
    A = 5
    N = 2
    l = [6, 7]
    u = [10, 10]
    p = [100, 200]

    resultado = alg(A, N, l, u, p)
    assert resultado == 0


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_mejor_uno(alg):
    """
    Un oferente tiene un precio mucho mayor. La solución óptima es asignarle todas las acciones posibles.
    """
    A = 10
    N = 2
    l = [1, 1]
    u = [10, 10]
    p = [100, 5]

    resultado = alg(A, N, l, u, p)
    assert resultado == 10 * 100  # 1000


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_combinacion_optima(alg):
    """
    A = 9.
    Oferta 2: [4,6] a 60, Oferta 3: [5,7] a 55.
    Solución óptima: 4 acciones al oferente 2 (4*60 = 240) + 5 al oferente 3 (5*55 = 275) = 515.
    Total acciones: 4 + 5 = 9 = A.
    """
    A = 9
    N = 3
    l = [3, 4, 5]
    u = [5, 6, 7]
    p = [50, 60, 55]

    resultado = alg(A, N, l, u, p)
    assert resultado == 515


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_sin_acciones(alg):
    """
    Si no hay acciones para vender (A = 0), la ganancia debe ser 0.
    """
    A = 0
    N = 3
    l = [1, 2, 3]
    u = [4, 5, 6]
    p = [10, 20, 30]

    resultado = alg(A, N, l, u, p)
    assert resultado == 0


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_sin_oferentes(alg):
    """
    Si no hay oferentes (N = 0), no se puede realizar ninguna venta → ganancia = 0.
    """
    A = 10
    N = 0
    l = []
    u = []
    p = []

    resultado = alg(A, N, l, u, p)
    assert resultado == 0


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_mismo_precio(alg):
    """
    Múltiples oferentes con el mismo precio unitario.
    La ganancia óptima es vender todas las acciones disponibles al mismo precio.
    """
    A = 10
    N = 2
    l = [1, 1]
    u = [10, 10]
    p = [100, 100]

    resultado = alg(A, N, l, u, p)
    assert resultado == 1000  # 10 * 100


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_oferta_minimo_mayor_que_A(alg):
    """
    Una única oferta cuyo mínimo requerido (7) supera A=6 → no es factible.
    Ganancia = 0.
    """
    A = 6
    N = 1
    l = [7]
    u = [10]
    p = [100]

    resultado = alg(A, N, l, u, p)
    assert resultado == 0


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_no_greedy(alg):
    """
    El algoritmo no debe ser codicioso: aunque el oferente 1 tiene el mayor precio,
    combinarlo con el oferente 3 da mayor ganancia total.
    Solución: 1 acción a 100 + 4 acciones a 25 = 200.
    """
    A = 5
    N = 3
    l = [1, 1, 4]
    u = [1, 5, 4]
    p = [100, 20, 25]

    resultado = alg(A, N, l, u, p)
    assert resultado == 200


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_varios_oferentes_pequenos(alg):
    """
    10 oferentes, cada uno dispuesto a comprar exactamente 1 acción.
    Se asignan las 10 acciones a los 10 oferentes (todos caben), priorizando precios altos.
    Ganancia = suma de los 10 precios = 55.
    """
    A = 10
    N = 10
    l = [1] * 10
    u = [1] * 10
    p = list(range(10, 0, -1))  # [10, 9, ..., 1]

    resultado = alg(A, N, l, u, p)
    assert resultado == 55  # 10+9+...+1


# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("alg", ALGORITMOS)
def test_uso_parcial_de_intervalo(alg):
    """
    La solución óptima requiere usar una cantidad intermedia de un oferente.
    Ejemplo: 5 acciones al oferente 1 (precio 100) + 1 al oferente 2 (precio 90) = 590.
    """
    A = 6
    N = 2
    l = [1, 1]
    u = [5, 5]
    p = [100, 90]

    resultado = alg(A, N, l, u, p)
    assert resultado == 590