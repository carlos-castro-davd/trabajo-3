import plotly.graph_objects as go
from variables import *
import plotly.express as px
from plotly.subplots import *
import numpy as np 

def graficos_barras_variables(nombre_variable):

    fig = go.Figure(px.bar(df.groupby('TENURE').mean()[nombre_variable]))

    return fig

def info_clusters(df):
    """
    Parameters:
        df: pd.DataFrame(). Dataframe que contiene la informacion de los clusters

    Output:
        fig. go.Figure(). Representación gráfica de las medias por el cluster seleccionado
    """

    cluster = df["cluster"].iloc[0]
    columnas = ['CREDIT_LIMIT','BALANCE','PURCHASES','CASH_ADVANCE','MINIMUM_PAYMENTS','PAYMENTS']
    means = df[columnas].mean()

    variable_names= ['Credit Limit', 'Balance', 'Purchases', 'Cash Advance', 'Minimum Payments', 'Payments']

    # valores_primer_cluster = np.array([7284.607938, 1483.370003, 4070.525973, 416.412323, 781.144880, 4083.630226])
    # valores_segundo_cluster = np.array([3272.034108, 587.491306, 599.382552, 136.452908, 445.604001, 879.249391])
    # valores_tercer_cluster = np.array([4131.819553, 2100.521034, 243.428715, 2225.840189, 1063.410985, 1934.865207])
    # valores_cuarto_cluster = np.array([10309.629630, 7232.476288, 1903.598919, 3840.969261, 3266.247218, 4100.758674]) 

    data = [
        go.Bar(
            x = variable_names,
            y = means.values,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred","lightblue", "purple"]#,,"lightblue","indigo",'black'],
        )
    ]

    layout = go.Layout(title = "DISTRIBUCIÓN DE VARIABLES PARA EL CLUSTER {}".format(cluster), xaxis_title = "VARIABLES",
                    yaxis_title = f"CLUSTER {cluster}", title_x=0.5)

    fig = go.Figure(data = data, layout = layout)
    fig.update_yaxes(range=[0,10000])

    return fig 



