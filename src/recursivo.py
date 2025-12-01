def ganancia_maxima(i, a, l, u, p):
    """
    Versión recursiva pura.

    i : cantidad de oferentes considerados (1..N)
    a : acciones disponibles para repartir (0..A)
    """
    # Caso base: no hay oferentes o no hay acciones
    if i == 0 or a == 0:
        return 0

    # Opción 1: no asignar acciones al oferente i
    mejor = ganancia_maxima(i - 1, a, l, u, p)

    # Opción 2: asignar x acciones al oferente i-1
    li = l[i - 1]
    ui = u[i - 1]

    if a >= li:
        limite_superior = min(ui, a)
        for x in range(li, limite_superior + 1):
            valor = p[i - 1] * x + ganancia_maxima(i - 1, a - x, l, u, p)
            if valor > mejor:
                mejor = valor

    return mejor


def SubastaAccionesRecursiva(A, N, l, u, p):
    """
    Función de envoltura para llamar a la versión recursiva pura.
    """
    return ganancia_maxima(N, A, l, u, p)
