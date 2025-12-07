import json
import pandas as pd
import matplotlib.pyplot as plt

PATH = "resultados/experimento_completo.json"

def cargar_resultados():
    with open(PATH, "r") as f:
        data = json.load(f)
    return data

def transformar_a_dataframe(data):
    filas = []
    for instancia in data:
        A = instancia["A"]
        N = instancia["N"]
        for algoritmo, valores in instancia["resultados"].items():
            filas.append({
                "algoritmo": algoritmo,
                "A": A,
                "N": N,
                "tiempo": valores["tiempo"],
                "memoria": valores["memoria"],
                "resultado": valores["resultado"]
            })
    return pd.DataFrame(filas)

def analizar(df):
    print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
    print(df.groupby("algoritmo")[["tiempo", "memoria"]].describe())

    print("\n=== TIEMPO PROMEDIO POR ALGORITMO ===")
    print(df.groupby("algoritmo")["tiempo"].mean())

    print("\n=== MEMORIA PROMEDIO POR ALGORITMO ===")
    print(df.groupby("algoritmo")["memoria"].mean())

def graficar(df):
    df.groupby("algoritmo")["tiempo"].mean().plot(kind="bar")
    plt.ylabel("Tiempo promedio (s)")
    plt.title("Comparación de tiempos promedio por algoritmo")
    plt.show()

    df.groupby("algoritmo")["memoria"].mean().plot(kind="bar")
    plt.ylabel("Memoria pico (bytes)")
    plt.title("Comparación de uso de memoria")
    plt.show()

def main():
    data = cargar_resultados()
    df = transformar_a_dataframe(data)
    analizar(df)
    graficar(df)

if __name__ == "__main__":
    main()
