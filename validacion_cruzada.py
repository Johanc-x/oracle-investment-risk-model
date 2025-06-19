from fdi_utils import limpiar_datos_fdi, procesar_pais
from conexion_Oracle import conectar_oracle
import pandas as pd

df = pd.read_csv("data/fdi_inflows.csv", skiprows=4)
df_limpio = limpiar_datos_fdi(df)
df_esp_python = procesar_pais(df_limpio, "Spain")

def obtener_datos_oracle(conexion, nombre_pais):
    cursor = conexion.cursor()
    query = """
        SELECT f.anio, f.fdi_porcentaje
        FROM fdi_pais_objeto p,
             TABLE(p.fdi_anual) f
        WHERE p.nombre_pais = :nombre_pais
        ORDER BY f.anio
    """
    cursor.execute(query, {"nombre_pais": nombre_pais})
    resultados = cursor.fetchall()
    cursor.close()
    return pd.DataFrame(resultados, columns=["Año", "FDI"])

conexion = conectar_oracle("Usuario", "Contraseña")
df_esp_oracle = obtener_datos_oracle(conexion, "España")
conexion.close()

comparacion = df_esp_python.merge(df_esp_oracle, on="Año", suffixes=('_Python', '_Oracle'))
comparacion["Diferencia"] = abs(comparacion["FDI_Python"] - comparacion["FDI_Oracle"])
print(comparacion)
