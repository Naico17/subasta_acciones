# src/generador_instancias.py

import random
import os


def generate_instance(A, N, name="instancia", price_min=10, price_max=200):
    """
    Genera una instancia aleatoria del problema y la guarda en data/instancias.

    Parámetros
    ----------
    A : int
        Número total de acciones.
    N : int
        Número de oferentes.
    name : str
        Nombre base del archivo de salida (sin extensión).
    price_min : int
        Precio mínimo posible por acción.
    price_max : int
        Precio máximo posible por acción.

    Retorna
    -------
    str
        Ruta del archivo de instancia generado.
    """
    if A <= 0 or N <= 0:
        raise ValueError("A y N deben ser enteros positivos.")

    if price_min > price_max:
        raise ValueError("price_min no puede ser mayor que price_max.")

    os.makedirs("data/instancias", exist_ok=True)
    path = f"data/instancias/{name}.txt"

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{A} {N}\n")
        for _ in range(N):
            # mínimo entre 1 y A//2 (ajustado para que A=1 no falle)
            minimum = random.randint(1, max(1, A // 2))
            maximum = random.randint(minimum, A)
            price = random.randint(price_min, price_max)
            f.write(f"{minimum} {maximum} {price}\n")

    return path
