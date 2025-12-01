from src.utils import read_data
from src.generador_instancias import generate_instance
from src.brute_force import brute_force

# Generar una instancia de prueba automática
path = generate_instance(10, 3, name="ejemplo_prueba")

# Leer los datos generados
A, N, l, u, p = read_data(path)

print("Capacidad total (A):", A)
print("Número de oferentes (N):", N)
print("Mínimos l:", l)
print("Máximos u:", u)
print("Precios p:", p)

# Ejecutar el algoritmo de fuerza bruta
result = brute_force(A, N, l, u, p)

print("\nGanancia máxima (fuerza bruta):", result)
