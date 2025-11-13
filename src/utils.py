# src/utils.py

import json
import os

def leer_datos(ruta):
    """Lee el archivo de entrada y devuelve los datos de la subasta."""
    with open(ruta, "r") as f:
        A, N = map(int, f.readline().split())
        l, u, p = [], [], []
        for _ in range(N):
            li, ui, pi = map(int, f.readline().split())
            l.append(li)
            u.append(ui)
            p.append(pi)
    return A, N, l, u, p


def guardar_resultado(nombre_archivo, resultado):
    """Guarda un resultado en formato JSON dentro de la carpeta resultados."""
    os.makedirs("resultados", exist_ok=True)
    ruta = os.path.join("resultados", f"{nombre_archivo}.json")
    with open(ruta, "w") as f:
        json.dump(resultado, f, indent=4)
