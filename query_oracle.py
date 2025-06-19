import cx_Oracle


def consultar_fdi_por_pais(conexion, nombre_pais):
    cursor = conexion.cursor()

    query = """
        SELECT p.nombre_pais, f.anio, f.fdi_porcentaje
        FROM fdi_pais_objeto p,
             TABLE(p.fdi_anual) f
        WHERE p.nombre_pais = :nombre_pais
        ORDER BY f.anio
    """

    cursor.execute(query, {"nombre_pais": nombre_pais})
    resultados = cursor.fetchall()

    print(f"\n📊 Datos FDI de {nombre_pais}:")
    for fila in resultados:
        print(f"Año: {fila[1]}, FDI: {fila[2]}%")

    cursor.close()

# ===========================
# Generador de INSERT SQL
# ===========================

def generar_insert_oracle(nombre_pais, codigo_pais, df_pais):
    """
    Genera una sentencia SQL INSERT para Oracle con tipos anidados.

    Args:
        nombre_pais (str): Nombre del país (ej. "España").
        codigo_pais (str): Código del país (ej. "ESP").
        df_pais (pd.DataFrame): DataFrame con columnas 'Año' y 'FDI'.

    Returns:
        str: Sentencia SQL INSERT lista para pegar en Oracle SQL Developer.
    """
    valores = []
    for _, fila in df_pais.iterrows():
        valores.append(f"fdi_anual_tipo({fila['Año']}, {round(fila['FDI'], 2)})")

    valores_str = ",\n        ".join(valores)
    
    insert = f"""
INSERT INTO fdi_pais_objeto VALUES (
    '{nombre_pais}',
    '{codigo_pais}',
    fdi_lista_tipo(
        {valores_str}
    )
);
"""
    return insert

if __name__ == "__main__":
    from fdi_utils import procesar_pais, limpiar_datos_fdi
    from conexion_Oracle import conectar_oracle
    import pandas as pd

    # ========================
    # 1. Limpieza y procesamiento
    # ========================

    # df = pd.read_csv("data/fdi_inflows.csv", skiprows=4)
    # df_limpio = limpiar_datos_fdi(df)
    # df_ue = procesar_pais(df_limpio, "United States")

    # # ========================
    # # 2. Generador SQL para INSERT en Oracle
    # # ========================

    # sql_insert = generar_insert_oracle("Estados Unidos de América", "USA", df_ue)
    # print(sql_insert)

    #  # ========================
    # # 3. Consulta cruzada desde Oracle
    # # ========================

    conexion = conectar_oracle("system", "Success_0425")
    if conexion:
        consultar_fdi_por_pais(conexion, "España")
        conexion.close()
