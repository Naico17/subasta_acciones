# src/utils.py

import json
import os


def read_data(path):
    """Lee el archivo de entrada y devuelve los datos de la subasta."""
    with open(path, "r") as f:
        A, N = map(int, f.readline().split())
        l, u, p = [], [], []
        for _ in range(N):
            li, ui, pi = map(int, f.readline().split())
            l.append(li)
            u.append(ui)
            p.append(pi)
    return A, N, l, u, p


def save_result(filename, result):
    """Guarda un resultado en formato JSON dentro de la carpeta resultados."""
    os.makedirs("resultados", exist_ok=True)
    path = os.path.join("resultados", f"{filename}.json")
    with open(path, "w") as f:
        json.dump(result, f, indent=4)
