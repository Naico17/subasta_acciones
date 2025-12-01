def dynamic_programming(A, N, l, u, p):
    """
    Programación dinámica iterativa para el problema de subasta de acciones.

    Parámetros
    ----------
    A : int
        Número total de acciones a subastar.
    N : int
        Número de oferentes.
    l, u, p : list[int]
        Listas de longitud N con el mínimo, máximo y precio por acción
        de cada oferente, respectivamente.

    Retorna
    -------
    int
        Ganancia máxima posible.
    """
    # Inicializar la tabla dp con ceros (dimensiones: (N+1) x (A+1))
    dp = [[0 for _ in range(A + 1)] for _ in range(N + 1)]

    # Caso base: i = 0 --> ganancia nula (ya está con ceros)
    for shares in range(A + 1):
        dp[0][shares] = 0

    # Llenar la tabla fila por fila
    for i in range(1, N + 1):
        for shares in range(A + 1):
            # Opción 1: no asignar acciones al oferente i
            best = dp[i - 1][shares]

            # Opción 2: asignar x acciones al oferente i
            if shares >= l[i - 1]:
                limit = min(u[i - 1], shares)
                for x in range(l[i - 1], limit + 1):
                    profit = p[i - 1] * x + dp[i - 1][shares - x]
                    if profit > best:
                        best = profit

            dp[i][shares] = best

    # La ganancia máxima se encuentra en dp[N][A]
    return dp[N][A]
