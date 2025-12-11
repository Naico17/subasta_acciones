# src/brute_force.py

def brute_force(A, N, l, u, p):
    """
    Búsqueda exhaustiva (backtracking).
    
    """
    best_profit = 0

    def backtrack(i, remaining_shares, current_profit):
        nonlocal best_profit

        # Caso base: ya procesamos todos los oferentes
        if i == N:
            best_profit = max(best_profit, current_profit)
            return

        # Opción 1: no vender a este oferente
        backtrack(i + 1, remaining_shares, current_profit)

        # Opción 2: venderle entre el mínimo y el máximo posible
        for x in range(l[i], u[i] + 1):
            if x <= remaining_shares:
                backtrack(
                    i + 1,
                    remaining_shares - x,
                    current_profit + x * p[i],
                )

    # Llamada inicial
    backtrack(0, A, 0)
    return best_profit
