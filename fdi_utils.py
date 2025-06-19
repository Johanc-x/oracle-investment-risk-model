import pandas as pd
import matplotlib.pyplot as plt 

# =====================================
# Funciones de limpieza de datos
# =====================================

def limpiar_datos_fdi(df):
    """
    Limpia el DataFrame original del CSV:
    - Elimina columnas completamente vacías.
    - Convierte los valores FDI a float.
    - Elimina filas con todos los valores FDI nulos.
    - Mantiene solo los años entre 2000 y 2022 (si están presentes).
    """

    print(f"📥 Shape original: {df.shape}")

    # 1. Eliminar columnas completamente vacías
    df = df.dropna(axis=1, how='all')

    # 2. Verificar qué columnas de año realmente están presentes
    columnas_esperadas = [str(año) for año in range(2000, 2023)]
    columnas_presentes = [col for col in columnas_esperadas if col in df.columns]

    # 3. Seleccionar solo columnas válidas
    columnas_validas = ["Country Name", "Country Code"] + columnas_presentes
    df = df[columnas_validas]

    # 4. Convertir columnas de año a float
    for col in columnas_presentes:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 5. Eliminar filas que tengan todos los FDI como NaN
    df = df.dropna(subset=columnas_presentes, how='all')

    print(f"✅ Shape después de limpieza: {df.shape}")
    print(f"🧪 ¿Hay nulos? {df.isnull().values.any()}")

    return df


# =====================================
# Funcion para la creacion de df por país.
# =====================================

def procesar_pais(df, nombre_pais):
    """
    Filtra el DataFrame por país y transforma los datos para análisis.

    Args:
        df (pd.DataFrame): DataFrame original cargado desde el CSV.
        nombre_pais (str): Nombre del país a procesar (ej. "Spain").

    Returns:
        pd.DataFrame: DataFrame con columnas 'Año' y 'FDI'.
    """

    cols = ["Country Name", "Country Code"] + [str(a) for a in range(2000, 2023)]
    df_filtrado = df[cols]
    pais = df_filtrado[df_filtrado["Country Name"] == nombre_pais]
    pais = pais.drop(columns=["Country Name", "Country Code"])
    pais = pais.T
    pais = pais.reset_index()
    pais.columns = ['Año','FDI']
    pais["Año"] = pais["Año"].astype(int)
    return pais

# =====================================
# Funcion para el calculo estadístico por país.
# =====================================

def resumen_estadistico(df_pais, nombre_pais):
    """
    Imprime estadísticas descriptivas del FDI de un país.

    Args:
        df_pais (pd.DataFrame): DataFrame con columnas 'Año' y 'FDI'.
        nombre_pais (str): Nombre del país (para mostrar en los mensajes).
    """
    print(f"\n📊 Análisis estadístico de {nombre_pais}")
    print(f"➡️ Promedio: {df_pais['FDI'].mean():.2f}% del PIB")
    print(f"➡️ Mediana: {df_pais['FDI'].median():.2f}% del PIB")
    print(f"➡️ Rango: {df_pais['FDI'].max() - df_pais['FDI'].min():.2f}%")
    print(f"➡️ Desviación estándar: {df_pais['FDI'].std():.2f}%")

# =====================================
# Funcion para la creación de gráfica por país.
# =====================================


def graficar_fdi(df_pais, nombre_pais, ruta_salida):
    """
    Genera un gráfico de líneas con la evolución del FDI.

    Args:
        df_pais (pd.DataFrame): DataFrame con columnas 'Año' y 'FDI'.
        nombre_pais (str): Nombre del país (para título).
        ruta_salida (str): Ruta donde guardar la imagen .png.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df_pais["Año"], df_pais["FDI"], marker='o', label=nombre_pais)
    plt.axhline(df_pais["FDI"].mean(), color='red', linestyle='--', label='Promedio')
    plt.title(f"Flujo de Inversión Extranjera Directa (% PIB) - {nombre_pais}")
    plt.xlabel("Año")
    plt.ylabel("FDI (% PIB)")
    plt.legend()
    plt.grid(True)
    print(f"📁 Guardando gráfica en: {ruta_salida}")
    plt.savefig(ruta_salida)
    plt.close()

# =====================================
# Funcion que agrupa las 3 funciones anteriores en una sóla.
# Para una sola llamada a función.
# =====================================

def analizar_fdi(df, nombre_filtro, nombre_visible, ruta_salida):
    df_pais = procesar_pais(df, nombre_filtro)
    resumen_estadistico(df_pais, nombre_visible)
    graficar_fdi(df_pais, nombre_visible, ruta_salida)
    return df_pais
# =====================================
# Funcion para generar un gráfico comparativo entre países.
# =====================================


def graficar_comparativo(paises_data, ruta_salida):
    """
    Genera un gráfico comparativo de FDI para múltiples países.

    Args:
        paises_data (dict): Diccionario con clave el nombre visible del país y valor su DataFrame.
        ruta_salida (str): Ruta para guardar la imagen comparativa.
    """
    plt.figure(figsize=(12, 6))
    
    for nombre_pais, df in paises_data.items():
        plt.plot(df["Año"], df["FDI"], marker='o', label=nombre_pais)

    plt.title("Comparación FDI (% del PIB) - 2000 a 2022")
    plt.xlabel("Año")
    plt.ylabel("FDI (% PIB)")
    plt.legend()
    plt.grid(True)
    print(f"📊 Guardando gráfico comparativo en: {ruta_salida}")
    plt.savefig(ruta_salida)
    plt.close()

# =====================================
# Función que genera un archivo nuevo con el resumen estadístico por país.
# =====================================

def generar_resumen(paises_data, ruta_archivo="docs/resumen_fdi.txt"):
    """
    Genera un archivo de texto con el resumen estadístico de cada país.

    Args:
        paises_data (dict): Diccionario con claves como nombres visibles y valores como DataFrames con 'FDI' y 'Año'.
        ruta_archivo (str): Ruta del archivo de salida.
    """
    with open(ruta_archivo,"w", encoding="utf-8") as f:
        f.write("📘RESUMEN ESTADÍSTICO FDI(% del PIB)\n")
        f.write("="* 45 + "\n\n")

        for nombre_pais, df_pais in paises_data.items():
            promedio = df_pais["FDI"].mean()
            mediana = df_pais["FDI"].median()
            desviacion = df_pais["FDI"].std()
            rango = df_pais["FDI"].max() - df_pais['FDI'].min()

            f.write(f" 🌍 {nombre_pais}\n")
            f.write(f" ➡️ Promedio: {promedio:.2f}%\n")
            f.write(f" ➡️ Mediana: {mediana:.2f}%\n")
            f.write(f" ➡️ Rango: {rango:.2f}%\n")
            f.write(f" ➡️ Desviación estándar: {desviacion:.2f}%\n")
            f.write("-" * 40 + "\n")


