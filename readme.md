# Modelo de análisis de inversión extranjera directa y riesgo financiero
**Estructuras objeto-relacionales en Oracle SQL + visualización en Power BI**

## Descripción
Este proyecto utiliza el poder de las bases de datos objeto-relacionales de Oracle combinadas con análisis exploratorio en Python y visualización interactiva en Power BI para examinar la evolución de la inversión extranjera directa (FDI) en economías clave entre 2000 y 2023.

## Objetivos del proyecto
- Analizar el comportamiento de la FDI como % del PIB por país y año
- Identificar países con mayores y menores niveles de atracción de capital
- Desarrollar un modelo base de riesgo financiero y dispersión
- Visualizar los datos de forma dinámica para facilitar su interpretación

## Resumen económico del análisis
Irlanda presenta un comportamiento notable en la serie histórica de FDI (% del PIB), alcanzando un valor cercano al 74,75 %, lo cual la posiciona como el país con el mayor FDI registrado en el periodo. En contraste, Estados Unidos marca el mínimo positivo con un valor del 0,64 %. Esta dispersión sugiere diferencias estructurales significativas en los modelos económicos y fiscales. Una primera hipótesis indica que el modelo de baja tributación de Irlanda podría haber incentivado flujos de capital más volátiles. Se prevé complementar este análisis con variables adicionales en el futuro para obtener una visión más rigurosa del riesgo país.

## Herramientas utilizadas
- **Oracle SQL Developer** – Modelado objeto-relacional y consultas avanzadas
- **Python (Pandas, Matplotlib)** – Exploración, limpieza y validación de datos
- **Power BI + DAX** – Dashboard visual e indicadores clave
- **DAX Studio** – Evaluación de rendimiento de las medidas en Power BI

## Datos
Fuente: [Banco Mundial](https://data.worldbank.org/indicator/BX.KLT.DINV.WD.GD.ZS)  
Métrica: FDI como % del PIB

