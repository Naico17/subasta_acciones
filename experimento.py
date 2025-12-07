from src.generador_instancias import generate_instance
from src.utils import read_data, save_result
from src.utils_tiempo import medir_algoritmo
from src.fuerza_bruta import brute_force
from src.recursivo import recursive
from src.recursivaMemorización import recursive_memoization
from src.programacion_dinamica import dynamic_programming
import json

ALGORITMOS = {
    "brute_force": brute_force,
    "recursive": recursive,
    "memo": recursive_memoization,
    "dp": dynamic_programming
}

def ejecutar_experimento(num_instancias=10, A=50, N=10):
    resultados = []

    for i in range(num_instancias):
        path = generate_instance(A, N, name=f"inst{i}")
        A_, N_, l, u, p = read_data(path)

        print(f"Instancia {i+1}/{num_instancias}")

        datos_instancia = {
            "path": path,
            "A": A_,
            "N": N_,
            "resultados": {}
        }

        for nombre, algoritmo in ALGORITMOS.items():
            print(f"  Ejecutando {nombre}...")
            m = medir_algoritmo(algoritmo, A_, N_, l, u, p)
            datos_instancia["resultados"][nombre] = m

        resultados.append(datos_instancia)

    save_result("experimento_completo", resultados)
    print("\nExperimento completo guardado en resultados/")

if __name__ == "__main__":
    ejecutar_experimento()
