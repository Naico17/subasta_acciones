# src/fuerza_bruta.py

def fuerza_bruta(A, N, l, u, p):
    """
    Búsqueda exhaustiva (backtracking) para el problema de la subasta de acciones.

    Parámetros
    ----------
    A : int
        Número total de acciones disponibles.
    N : int
        Número de oferentes.
    l, u, p : list[int]
        Listas de longitud N con el mínimo, máximo y precio por acción
        de cada oferente, respectivamente.

    Retorna
    -------
    int
        Ganancia máxima posible al repartir como mucho A acciones entre
        los N oferentes.
    """
    mejor_ganancia = 0

    def backtrack(i, acciones_restantes, ganancia_actual):
        nonlocal mejor_ganancia

        # Caso base: ya procesamos todos los oferentes
        if i == N:
            mejor_ganancia = max(mejor_ganancia, ganancia_actual)
            return

        # Opción 1: no vender a este oferente
        backtrack(i + 1, acciones_restantes, ganancia_actual)

        # Opción 2: venderle entre el mínimo y el máximo posible
        for x in range(l[i], u[i] + 1):
            if x <= acciones_restantes:
                backtrack(
                    i + 1,
                    acciones_restantes - x,
                    ganancia_actual + x * p[i],
                )

    # Llamada inicial
    backtrack(0, A, 0)
    return mejor_ganancia

