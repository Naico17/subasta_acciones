"""
experimento_v2.py
Runner experimental mejorado:
- genera instancias con A y N variados (no todas del mismo tamaño)
- ejecuta todos los algoritmos disponibles
- mide tiempo y memoria (usa src/utils_tiempo.py -> medir_algoritmo)
- guarda resultados en resultados/experimento.json y resultados/experimento_flat.csv
"""

import os
import random
import csv
from datetime import datetime

# imports del proyecto (ajusta si tus módulos tienen otros nombres)
from src.generador_instancias import generate_instance
from src.utils import read_data, save_result
# medir_algoritmo fue definido en src/utils_tiempo.py
from src.utils_tiempo import medir_algoritmo

# intentamos importar los algoritmos con los nombres que tienes en src
# si alguno falta, se ignora y se informa.
ALGORITMOS = {}
try:
    from src.fuerza_bruta import brute_force
    ALGORITMOS["brute_force"] = brute_force
except Exception:
    try:
        from src.fuerza_bruta import brute_force
        ALGORITMOS["brute_force"] = brute_force
    except Exception:
        print("Aviso: no se pudo importar brute_force")

try:
    from src.recursivo import recursive
    ALGORITMOS["recursive"] = recursive
except Exception:
    print("Aviso: no se pudo importar recursivo")

# nombre con acento si existe en tu repo
try:
    from src.recursivaMemorización import recursive_memoization
    ALGORITMOS["memo"] = recursive_memoization
except Exception:
    try:
        from src.recursivaMemorización import recursive_memoization
        ALGORITMOS["memo"] = recursive_memoization
    except Exception:
        print("Aviso: no se pudo importar recursive_memoization")

try:
    from src.programacion_dinamica import dynamic_programming
    ALGORITMOS["dp"] = dynamic_programming
except Exception:
    try:
        from src.programacion_dinamica import dynamic_programming
        ALGORITMOS["dp"] = dynamic_programming
    except Exception:
        print("Aviso: no se pudo importar dynamic_programming")

if not ALGORITMOS:
    raise RuntimeError("No se importó ningún algoritmo. Revisa nombres de módulos en src/")

# Parámetros del experimento (ajustables)
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# quieres rangos variados: lista de A y N
LIST_A = [10, 25, 50]            # tamaños de capacidad A (puedes ajustar)
LIST_N = [5, 10, 15]             # números de oferentes (puedes ajustar)
INSTANCIAS_POR_COMBINACION = 4   # cuántas instancias por par (A,N)
REPETICIONES_POR_EJECUCION = 1   # medir cada algoritmo REPETICIONES veces dentro de medir_algoritmo si lo deseas

# directorios de salida
os.makedirs("resultados", exist_ok=True)
FNAME_JSON = "resultados/experimento.json"
FNAME_CSV = "resultados/experimento_flat.csv"

def generar_nombre_instancia(A, N, idx):
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"inst_A{A}_N{N}_{idx}_{ts}"

def ejecutar():
    resultados = []
    filas_csv = []

    total = len(LIST_A) * len(LIST_N) * INSTANCIAS_POR_COMBINACION
    contador = 0

    for A in LIST_A:
        for N in LIST_N:
            for idx in range(INSTANCIAS_POR_COMBINACION):
                contador += 1
                inst_name = generar_nombre_instancia(A, N, idx)
                # fijar semilla por instancia para reproducibilidad
                seed = RANDOM_SEED + contador
                random.seed(seed)

                path = generate_instance(A, N, name=inst_name)
                A_, N_, l, u, p = read_data(path)

                print(f"Instancia {contador}/{total}: {path}  (A={A_}, N={N_}, seed={seed})")

                datos_inst = {
                    "path": path,
                    "A": A_,
                    "N": N_,
                    "seed": seed,
                    "resultados": {}
                }

                for nombre, func in ALGORITMOS.items():
                    print(f"  Ejecutando {nombre} ...")
                    try:
                        medicion = medir_algoritmo(func, A_, N_, l, u, p)
                    except Exception as e:
                        medicion = {"error": str(e)}
                        print(f"    Error al ejecutar {nombre}: {e}")

                    # normalizar resultado si es dict o int
                    resultado_val = medicion.get("resultado") if isinstance(medicion, dict) else medicion

                    datos_inst["resultados"][nombre] = medicion

                    # fila plana para CSV
                    fila = {
                        "instance_path": path,
                        "instance_name": inst_name,
                        "A": A_,
                        "N": N_,
                        "seed": seed,
                        "algorithm": nombre,
                        "resultado": resultado_val,
                        "tiempo": medicion.get("tiempo"),
                        "memoria": medicion.get("memoria")
                    }
                    filas_csv.append(fila)

                resultados.append(datos_inst)

    # Guardar JSON completo de la corrida
    save_result("experimento", resultados)
    # Guardar CSV plano
    with open(FNAME_CSV, "w", newline="", encoding="utf-8") as f:
        campos = ["instance_path","instance_name","A","N","seed","algorithm","resultado","tiempo","memoria"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for r in filas_csv:
            writer.writerow(r)

    print(f"\nExperimento terminado. JSON -> {FNAME_JSON} (usado save_result)\nCSV plano -> {FNAME_CSV}")

if __name__ == "__main__":
    ejecutar()
