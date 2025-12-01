def max_profit_recursive(i, shares, l, u, p):
    """
    Versión recursiva pura.

    i : cantidad de oferentes considerados (1..N)
    shares : acciones disponibles para repartir (0..A)
    """
    # Caso base: no hay oferentes o no hay acciones
    if i == 0 or shares == 0:
        return 0

    # Opción 1: no asignar acciones al oferente i
    best = max_profit_recursive(i - 1, shares, l, u, p)

    # Opción 2: asignar x acciones al oferente i-1
    min_i = l[i - 1]
    max_i = u[i - 1]

    if shares >= min_i:
        upper_limit = min(max_i, shares)
        for x in range(min_i, upper_limit + 1):
            value = p[i - 1] * x + max_profit_recursive(i - 1, shares - x, l, u, p)
            if value > best:
                best = value

    return best


def recursive(A, N, l, u, p):
    """
    Función de envoltura para llamar a la versión recursiva pura.
    """
    return max_profit_recursive(N, A, l, u, p)
