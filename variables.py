# Librería para leer los ficheros
import pandas as pd

# Seleccionamos nuestro fichero de datos completo
df = pd.read_csv("trabajo3.csv")

# Fichero de todos los clientes, menos los outliers
df_sin_outliers = df[df["BALANCE"] < 5000]

# Fichero con la asignacion de cluster a cada cliente
df_clusters = pd.read_csv('../../Trabajo 3 Info/df_clusters.csv')

# Fichero para representar el radar chart
df_radar_chart = pd.read_csv('../../Trabajo 3 Info/df_radar_chart.csv')

# Estilo del primer texto (Explicación de los outliers)
style_texto = {
    "display": "block",
    "margin-left": "150px",
    "margin-right": "150px",
    "text-align": "center",
    "text-align": "justify",
    "line-height": "150%",
    "font-family": "monospace",
    "font-weight": "bold",
    "font-size": "14px"
}

# Estilo del segundo texto (Descripción de cada clusters) 
stlyle_texto_2 = {
    "display": "block",
    "margin-left": "300px",
    "margin-right": "150px",
    "text-align": "center",
    "text-align": "justify",
    "font-weight": "bold",
    "line-height": "150%",
    "font-family": "monospace",
    "font-size": "14px"
}

# Estilo del tercer texto (Descripción larga de los clusters) 
stlyle_texto_3 = {
    "display": "block",
    "margin-left": "250px",
    "margin-right": "150px",
    "text-align": "center",
    "text-align": "justify",
    "font-weight": "bold",
    "line-height": "150%",
    "font-family": "monospace",
    "font-size": "14px"
}

# Estilo del cuarto texto (Descripción de variables por clusters) 
stlyle_texto_4 = {
    "display": "block",
    "margin-left": "400px",
    "margin-right": "150px",
    "text-align": "center",
    "text-align": "justify",
    "font-weight": "bold",
    "line-height": "150%",
    "font-family": "monospace",
    "font-size": "30px"
}

# Estilo del quinto texto (Relacion de un cliente con su cluster) 
stlyle_texto_5 = {
    "display": "block",
    "margin-left": "450px",
    "margin-right": "150px",
    "text-align": "center",
    "text-align": "justify",
    "font-weight": "bold",
    "line-height": "150%",
    "font-family": "monospace",
    "font-size": "30px"
}