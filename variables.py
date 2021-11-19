import pandas as pd

# Seleccionamos nuestro fichero de datos
df = pd.read_csv("trabajo3.csv")

df_sin_outliers = df[df["BALANCE"] < 5000]
df_clusters = pd.read_csv('../../Trabajo 3 Info/df_clusters.csv')
df_radar_chart = pd.read_csv('../../Trabajo 3 Info/df_radar_chart.csv')

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
