from fdi_utils import (limpiar_datos_fdi, analizar_fdi, procesar_pais,
                       graficar_comparativo, generar_resumen,)

import pandas as pd
import matplotlib.pyplot as plt

#Cargar archivo
df = pd.read_csv("data/fdi_inflows.csv", skiprows=4)

# Limpieza de datos.

df_limpio= limpiar_datos_fdi(df)

# df individuales por país.

df_s = procesar_pais(df_limpio, "Spain")
print(df_s)
# Análisis  de datos

# espana = analizar_fdi(df_limpio, "Spain", "España", "img/fdi_espana.png") 
# irlanda = analizar_fdi(df_limpio, "Ireland", "Irlanda", "img/fdi_ireland.png") 
# ue = analizar_fdi(df_limpio, "European Union", "Unión Europea", "img/fdi_ue.png") 
# usa = analizar_fdi(df_limpio, "United States", "Estados Unidos de América", "img/fdi_usa.png") 

# # Diccionario para el gráfico comparativo
# paises_data = {
#     "España": espana,
#     "Irlanda": irlanda,
#     "Unión Europea": ue,
#     "Estados Unidos de América": usa
# }

# # Gráfico comparativo
# graficar_comparativo(paises_data, "img/fdi_comparativo.png")

# # Crear resumen
# generar_resumen(paises_data)


