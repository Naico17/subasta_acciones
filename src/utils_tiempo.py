import time
import tracemalloc


def medir_algoritmo(func, A, N, l, u, p):
    """
    Ejecuta un algoritmo midiendo:
    - tiempo
    - memoria usada
    - resultado
    """
    tracemalloc.start()
    t0 = time.perf_counter()

    resultado = func(A, N, l, u, p)

    t1 = time.perf_counter()
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "resultado": resultado,
        "tiempo": t1 - t0,
        "memoria": memoria_pico
    }

