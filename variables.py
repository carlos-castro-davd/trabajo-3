import pandas as pd

# Seleccionamos nuestro fichero de datos
df = pd.read_csv("trabajo3.csv")

df_sin_outliers = df[df["BALANCE"] < 5000]


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
