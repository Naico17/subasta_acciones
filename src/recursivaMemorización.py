from functools import lru_cache

def SubastaAccionesRecursivaMemo(A, N, l, u, p):
    """
    Versión recursiva con memoización (top-down) para la subasta de acciones.
    Usa un caché interno para guardar los subproblemas (i, a).
    """

    @lru_cache(maxsize=None)
    def aux(i, a):
        # Caso base: no hay oferentes o no hay acciones
        if i == 0 or a == 0:
            return 0

        # Opción 1: no asignar acciones al oferente i
        mejor = aux(i - 1, a)

        # Opción 2: asignar x acciones al oferente i-1
        li = l[i - 1]
        ui = u[i - 1]

        if a >= li:
            limite_superior = min(ui, a)
            for x in range(li, limite_superior + 1):
                valor = p[i - 1] * x + aux(i - 1, a - x)
                if valor > mejor:
                    mejor = valor

        return mejor

    # Llamada inicial: considerar N oferentes y A acciones
    return aux(N, A)
