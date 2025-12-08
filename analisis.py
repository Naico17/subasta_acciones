"""
analisis.py
Lee resultados del experimento (resultados/experimento.json o .csv) y genera:
- estadísticas descriptivas impresas
- resumen CSV
- gráficas (tiempo vs A, tiempo vs N, boxplots tiempo por algoritmo, memoria)
"""

import os
import json
import pandas as pd
import matplotlib.pyplot as plt

JSON_PATH = "resultados/experimento.json"
CSV_PATH = "resultados/experimento_flat.csv"
OUT_DIR = "resultados/figs"
os.makedirs(OUT_DIR, exist_ok=True)

# Cargar datos preferentemente desde CSV si existe (más fácil)
if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
elif os.path.exists(JSON_PATH):
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    # convertir a DataFrame plano
    rows = []
    for inst in data:
        base = {"instance_path": inst.get("path"), "A": inst.get("A"), "N": inst.get("N"), "seed": inst.get("seed")}
        for alg, res in inst.get("resultados", {}).items():
            row = base.copy()
            row["algorithm"] = alg
            if isinstance(res, dict):
                row["resultado"] = res.get("resultado")
                row["tiempo"] = res.get("tiempo")
                row["memoria"] = res.get("memoria")
            else:
                row["resultado"] = res
                row["tiempo"] = None
                row["memoria"] = None
            rows.append(row)
    df = pd.DataFrame(rows)
    df.to_csv(CSV_PATH, index=False)
else:
    raise FileNotFoundError("No encontré resultados. Ejecuta experimento.py primero.")

# limpieza: convertir tipos
df["A"] = df["A"].astype(int)
df["N"] = df["N"].astype(int)
df["tiempo"] = pd.to_numeric(df["tiempo"], errors="coerce")
df["memoria"] = pd.to_numeric(df["memoria"], errors="coerce")

# Estadística descriptiva por algoritmo
group = df.groupby("algorithm")
desc = group[["tiempo","memoria"]].describe().transpose()
print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(desc)

# Tablas de resumen (tiempo promedio y memoria promedio)
time_mean = group["tiempo"].mean().sort_values()
mem_mean = group["memoria"].mean().sort_values()
print("\n=== TIEMPO PROMEDIO POR ALGORITMO ===")
print(time_mean)
print("\n=== MEMORIA PROMEDIO POR ALGORITMO ===")
print(mem_mean)

# Guardar resumen simple
summary_df = pd.DataFrame({
    "time_mean": time_mean,
    "time_std": group["tiempo"].std(),
    "mem_mean": mem_mean,
    "mem_std": group["memoria"].std()
})
summary_df.to_csv("resultados/summary_by_algorithm.csv")

# ----------------- GRAFICAS -----------------

# 1) Tiempo (mediana) vs A (una línea por algoritmo)
plt.figure(figsize=(8,5))
for alg, g in df.groupby("algorithm"):
    medians = g.groupby("A")["tiempo"].median().sort_index()
    plt.plot(medians.index, medians.values, marker='o', label=alg)
plt.xlabel("A (acciones)")
plt.ylabel("Tiempo mediano (s)")
plt.title("Tiempo mediano vs A por algoritmo")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "time_vs_A_median.png"))
plt.close()

# 2) Tiempo (mediana) vs N
plt.figure(figsize=(8,5))
for alg, g in df.groupby("algorithm"):
    medians = g.groupby("N")["tiempo"].median().sort_index()
    plt.plot(medians.index, medians.values, marker='o', label=alg)
plt.xlabel("N (oferentes)")
plt.ylabel("Tiempo mediano (s)")
plt.title("Tiempo mediano vs N por algoritmo")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "time_vs_N_median.png"))
plt.close()

# 3) Boxplot de tiempos por algoritmo (comparación de distribuciones)
plt.figure(figsize=(8,5))
df_box = df[["algorithm","tiempo"]].dropna()
df_box.boxplot(by="algorithm", column=["tiempo"], rot=45)
plt.suptitle("")
plt.title("Distribución de tiempos por algoritmo")
plt.xlabel("Algoritmo")
plt.ylabel("Tiempo (s)")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "boxplot_tiempos_por_algoritmo.png"))
plt.close()

# 4) Barra de memoria promedio por algoritmo
plt.figure(figsize=(8,5))
mem_mean.plot(kind="bar")
plt.ylabel("Memoria promedio (bytes)")
plt.title("Memoria promedio por algoritmo")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "memoria_promedio_por_algoritmo.png"))
plt.close()

# 5) Scatter tiempo vs resultado (si quieres ver trade-offs)
plt.figure(figsize=(8,5))
for alg, g in df.groupby("algorithm"):
    plt.scatter(g["tiempo"], g["resultado"], label=alg, alpha=0.8)
plt.xlabel("Tiempo (s)")
plt.ylabel("Resultado (ganancia)")
plt.title("Tiempo vs Resultado por algoritmo")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "tiempo_vs_resultado_scatter.png"))
plt.close()

# Guardar DataFrame procesado
df.to_csv("resultados/experimento_processed.csv", index=False)

print("\nGráficas y CSVs guardados en 'resultados/' y 'resultados/figs/'.")
print("Archivos generados:")
print(" - resultados/summary_by_algorithm.csv")
print(" - resultados/experimento_processed.csv")
print(" - resultados/figs/*.png")
