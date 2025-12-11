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

- Python:  3.12.6
- Bibliotecas externas: pandas, matplotlib
- IDE recomendado:  Visual Studio Code (VS Code)


---

## Cómo ejecutar

1. Clonar el repositorio:

       git clone https://github.com/Naico17/subasta_acciones.git
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
   
5. Ejecutar el análisis de resultados(gráficas y resultados):

       python analisis.py

   Lee los resultados guardados en resultados/experimento.json (o el archivo CSV plano),
Calcula estadísticas por algoritmo (media, desviación estándar, mediana),
Genera gráficas de tiempo vs. tamaño de entrada, boxplots y uso de memoria,
Guarda las figuras en resultados/figs/ y los resúmenes en archivos CSV.
Las gráficas y tablas producidas son las utilizadas en la presentación y el informe final.

---

## Ejecución de pruebas

Si se utilizan tests con `pytest`, desde la raíz del proyecto:

    pytest

---

## Especificaciones del dispositivo

**Hardware**

- Nombre del dispositivo	NITRO
- Procesador	11th Gen Intel(R) Core(TM) i5-11400H @ 2.70GHz (2.69 GHz)
- RAM instalada	12,0 GB (11,8 GB utilizable)
- Id. del dispositivo	ECD153B9-36AC-4E57-B5A4-E5CAA2E51DF6
- Id. del producto	00342-42319-46889-AAOEM
- Tipo de sistema	Sistema operativo de 64 bits, procesador x64
- Lápiz y entrada táctil	Compatibilidad con entrada manuscrita

**Software**

- Edición	Windows 11 Home Single Language
- Versión	24H2
- Se instaló el	‎16/‎02/‎2025
- Compilación del SO	26100.7171
- Experiencia	Paquete de experiencia de características de Windows 1000.26100.265.0

