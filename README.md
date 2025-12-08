# SUBASTA_ACCIONES

Análisis experimental de algoritmos exactos para el problema de **subasta de acciones**.

## Autores

- *Nicolas Vasquez Rengifo* –  
- *Juan Camilo Miño* –  



---

## Descripción del problema

Dado un número total de acciones \(A\) y un conjunto de \(N\) oferentes, cada uno con:

- un mínimo de acciones `l[i]`,
- un máximo de acciones `u[i]`,
- y un precio por acción `p[i]`,

se desea **asignar acciones a los oferentes** de forma que:

- no se exceda el total de acciones disponibles \(A\),
- se respeten los mínimos y máximos de cada oferente,
- y la **ganancia total** sea máxima.

Este repositorio implementa y compara varios algoritmos exactos para resolver este problema usando únicamente Python.

---

## Estructura del repositorio

    SUBASTA_ACCIONES/
    │
    ├─ data/                # Instancias de entrada
    ├─ resultados/          # Resultados de experimentos en formato JSON
    │
    ├─ src/
    │  ├─ fuerza_bruta.py           # función brute_force
    │  ├─ programacion_dinamica.py  # función dynamic_programming
    │  ├─ recursivo.py              # versión recursiva pura (recursive)
    │  ├─ recursivaMemorización.py  # versión recursiva con memoización
    │  ├─ generador_instancias.py   # generate_instance
    │  ├─ utils.py                  # read_data, save_result
    │  └─ utils_tiempo.py           # utilidades para medir tiempos
    │
    ├─ tests/               # Pruebas automáticas (pytest)
    ├─ main.py              # Ejemplo simple de uso
    └─ experimento.py       # Script principal de experimentos y medición de tiempos

---

## Algoritmos implementados

- **brute_force**  
  Búsqueda exhaustiva (backtracking) sobre todas las combinaciones posibles.

- **recursive**  
  Versión recursiva pura (top-down) sin memoización.

- **recursive_memoization**  
  Versión recursiva con memoización (top-down con caché).

- **dynamic_programming**  
  Versión iterativa de programación dinámica (bottom-up).

---

## Requisitos

- Python:  
- Bibliotecas externas: *(solo librería estándar; si se agrega algo más, escribirlo aquí)*  
- IDE recomendado:  

*(Completar versiones concretas más adelante.)*

---

## Cómo ejecutar

1. Clonar el repositorio:

       git clone <url-del-repo>
       cd SUBASTA_ACCIONES

2. (Opcional) Crear y activar un entorno virtual:

       python -m venv .venv
       # Windows
       .venv\Scripts\activate
       # Linux / macOS
       source .venv/bin/activate

3. Ejecutar un ejemplo sencillo:

       python main.py

   Este script:
   - genera una instancia de prueba,
   - la lee desde disco,
   - ejecuta el algoritmo de fuerza bruta,
   - y muestra la ganancia máxima.

4. Ejecutar el script de experimentos (comparación de algoritmos y tiempos):

       python experimento.py

   Los resultados se guardan en la carpeta `resultados/` en formato JSON.

---

## Ejecución de pruebas

Si se utilizan tests con `pytest`, desde la raíz del proyecto:

    pytest

---

## Especificaciones del dispositivo (para el informe)

**Hardware**

- Nombre del dispositivo:  
- Procesador:  
- RAM instalada:  
- Tipo de sistema:  

**Software**

- Sistema operativo:  
- Versión:  
- Herramientas utilizadas (IDE, etc.):  

*(Completar estos datos según el equipo donde se corrieron los experimentos.)*
