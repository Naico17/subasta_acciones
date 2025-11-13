# main.py

from src.utils import leer_datos
from src.generador_instancias import generar_instancia

# Generar una instancia de prueba
ruta = generar_instancia(10, 3, nombre="ejemplo_prueba")

# Leer los datos
A, N, l, u, p = leer_datos(ruta)

print("Acciones:", A)
print("Oferentes:", N)
print("Mínimos:", l)
print("Máximos:", u)
print("Precios:", p)
