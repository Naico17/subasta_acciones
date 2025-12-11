from functools import lru_cache


def recursive_memoization(A, N, l, u, p):
    """
    Versión recursiva con memoización (top-down) para la subasta de acciones.
    Usa un caché interno para guardar los subproblemas (i, a).
    """
    # Subproblema:
    # ¿Cuál es la ganancia máxima que puedo obtener usando los primeros i oferentes
    # y teniendo shares acciones disponibles?



    @lru_cache(maxsize=None)
    def memo_helper(i, shares):
        # Caso base: no hay oferentes o no hay acciones
        if i == 0 or shares == 0:
            return 0                #ganancia 0

        # Opción 1: no asignar acciones al oferente i, se ignora el oferente i-1 y se resuelve el problema para i-1 oferentes
        best = memo_helper(i - 1, shares)

        # Opción 2: asignar x acciones al oferente i-1
        min_i = l[i - 1]
        max_i = u[i - 1]

        if shares >= min_i:
            upper_limit = min(max_i, shares)
            for x in range(min_i, upper_limit + 1):
                value = p[i - 1] * x + memo_helper(i - 1, shares - x)
                if value > best:
                    best = value

        return best

    # Llamada inicial: considerar N oferentes y A acciones
    return memo_helper(N, A)
