import plotly.graph_objects as go
from variables import *
import plotly.express as px
from plotly.subplots import *
import numpy as np 

def graficos_barras_variables(nombre_variable):
    """
    Parameters:
        nombre_variable: df['nombre_variable']. Variable del dataframe que se reprentará en un barplot

    Output:
        fig. go.Figure(). Representación gráfica de la variable seleccionada en el dropdown según el límite de crédito (TENURE)
    """

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

    data = [
        go.Bar(
            x = variable_names,
            y = means.values,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred","lightblue", "purple"]
        )
    ]

    layout = go.Layout(title = "DISTRIBUCIÓN DE VARIABLES PARA EL CLUSTER {}".format(cluster), xaxis_title = "VARIABLES",
                    yaxis_title = f"Media del Cluster {cluster} para cada variable", title_x=0.5)

    fig = go.Figure(data = data, layout = layout)
    fig.update_yaxes(range=[0,10000])

    return fig 


def radar_chart_clusters_representacion(tipo_cluster):

    """
    Parameters:
        tipo_cluster: df['cluster']. Variable que contiene la informacion de a qué cluster pertenece el cliente

    Output:
        fig. go.Figure(). Representación gráfica del radar chart del cluster al que pertenece el cliente introducido en un input
    """

    categories = ['Purchases Frecuency','Balance Frecuency','Unique Pruchase Frecuency',
                'Purchases Installments Frequency', 'Cash Advance Frequency']

    fig = go.Figure()

    if tipo_cluster == 0:
        fig.add_trace(go.Scatterpolar(
            r=[0.945247, 0.977679, 0.681029, 0.728528, 0.059451], #0.945247 0.977679 0.681029 0.728528 0.059451
            theta=categories,
            fill='toself',
            name='Cluster 0'
        ))
    elif tipo_cluster == 1:
        fig.add_trace(go.Scatterpolar(
            r=[0.556312, 0.841441, 0.152768, 0.422003, 0.033380], #0.556312 0.841441 0.152768 0.422003 0.033380
            theta=categories,
            fill='toself',
            name='Cluster 1'
        ))
    elif tipo_cluster == 2:
        fig.add_trace(go.Scatterpolar(
            r=[0.170611, 0.940687, 0.084821, 0.093552, 0.332762], #0.170611 0.940687 0.084821 0.093552 0.332762
            theta=categories,
            fill='toself',
            name='Cluster 2'
        ))
    elif tipo_cluster == 3:
        fig.add_trace(go.Scatterpolar(
            r=[0.452271, 0.993695, 0.246687, 0.347853, 0.346737], #0.452271 0.993695 0.246687 0.347853 0.346737
            theta=categories,
            fill='toself',
            name='Cluster 3'
        ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 1]
        )),
    showlegend=True
    )

    fig.update_layout(width = 900, height = 600, title = "Frecuencia del Cluster del cliente introducido",
                    title_x=0.5, bargap = 0.2)

    return fig

