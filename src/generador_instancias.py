# src/generador_instancias.py

import random
import os

def generar_instancia(A, N, nombre="instancia"):
    """
    Genera una instancia aleatoria del problema y la guarda en /data/instancias.
    A: número total de acciones.
    N: número de oferentes.
    """
    os.makedirs("data/instancias", exist_ok=True)
    ruta = f"data/instancias/{nombre}.txt"

    with open(ruta, "w") as f:
        f.write(f"{A} {N}\n")
        for _ in range(N):
            minimo = random.randint(1, A // 2)
            maximo = random.randint(minimo, A)
            precio = random.randint(10, 200)
            f.write(f"{minimo} {maximo} {precio}\n")

    return ruta
