

from src.utils import leer_datos
from src.generador_instancias import generar_instancia
from src.fuerza_bruta import fuerza_bruta

# Generar una instancia de prueba automática
ruta = generar_instancia(10, 3, nombre="ejemplo_prueba")

# Leer los datos generados
A, N, l, u, p = leer_datos(ruta)

print("Capacidad total (A):", A)
print("Número de oferentes (N):", N)
print("Mínimos l:", l)
print("Máximos u:", u)
print("Precios p:", p)

# Ejecutar el algoritmo de fuerza bruta
resultado = fuerza_bruta(A, N, l, u, p)

print("\nGanancia máxima (fuerza bruta):", resultado)
