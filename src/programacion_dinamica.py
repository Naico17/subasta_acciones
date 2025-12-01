def SubastaAccionesDP(A, N, l, u, p):
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
    for a in range(A + 1):
        dp[0][a] = 0

    # Llenar la tabla fila por fila
    for i in range(1, N + 1):
        for a in range(A + 1):
            # Opción 1: no asignar acciones al oferente i
            mejor = dp[i - 1][a]

            # Opción 2: asignar x acciones al oferente i
            if a >= l[i - 1]:
                limite = min(u[i - 1], a)
                for x in range(l[i - 1], limite + 1):
                    ganancia = p[i - 1] * x + dp[i - 1][a - x]
                    if ganancia > mejor:
                        mejor = ganancia

            dp[i][a] = mejor

    # La ganancia máxima se encuentra en dp[N][A]
    return dp[N][A]

