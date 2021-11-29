import plotly.graph_objects as go
from variables import *
import plotly.express as px
from plotly.subplots import *


def diagrama_cajas_sin_outliers():

    """
    Output:
        fig. go.Figure(). Representación gráfica del diagrama de cajas de los clientes que no pertenecen al cluster de los outliers
    """

    fig = go.Figure(
        data=[
            go.Box(
                x=df_sin_outliers["BALANCE"],
                marker_color="green",
                boxpoints="all"
            ),
        ],
        layout=go.Layout(
            title="Diagrama de cajas: Variable Balance SIN OUTLIERS",
            xaxis_title="Balance (saldo en la cuenta)",
            width=600,
            height=600,
        )
    )

    return fig


def diagrama_cajas_balance_con_outliers():

    """
    Output:
        fig. go.Figure(). Representación gráfica del diagrama de cajas de los clientes que pertenecen al cluster de los outliers
    """

    fig = go.Figure(
        data=[
            go.Box(
                x=df["BALANCE"],
                marker_color="steelblue",
                boxpoints="all"
            ),
        ],
        layout=go.Layout(
            title="Diagrama de cajas: Variable Balance CON OUTLIERS",
            xaxis_title="Balance (saldo en la cuenta)",
            width=600,
            height=600,
        )
    )
    return fig


def grafico_barras_balance_purchases():

    """
    Output:
        fig. go.Figure(). Representación gráfica de un barplot que ilustra los valores de BALANCE y PURCHASES para cada cluster
    """

    means_credit_limit = df_clusters.groupby('cluster').mean()['CREDIT_LIMIT'].values
    means_balance_limit = df_clusters.groupby('cluster').mean()['BALANCE'].values
    means_purchases_limit = df_clusters.groupby('cluster').mean()['PURCHASES'].values
    means_cash_advance_limit = df_clusters.groupby('cluster').mean()['CASH_ADVANCE'].values
    means_minimum_payments_limit = df_clusters.groupby('cluster').mean()['MINIMUM_PAYMENTS'].values
    means_purchases_frecuency_limit = df_clusters.groupby('cluster').mean()['PURCHASES_FREQUENCY'].values

    cluster_names = ["0","1","2","3"]

    df_clusters_list = pd.DataFrame({'cluster': cluster_names,'cluster_means': means_credit_limit})

    data1 = go.Bar(x = cluster_names, y = means_purchases_limit, name = "PURCHASES")
    data2 = go.Bar(x = cluster_names, y = means_balance_limit, name = "BALANCE")

    data= [data1, data2]

    layout = go.Layout(title = "Purchases VS. Balance por Cluster (Gráfico de barras)", xaxis_title = "CLUSTERS", yaxis_title = "COUNT", title_x=0.45)

    fig = go.Figure(data = data, layout = layout)

    return fig


def grafico_simbolos_balance_purchases():
    
    """
    Output:
        fig. go.Figure(). Representación gráfica de un scatterplot que ilustra la distribución de los clusters según el BALANCE (eje x) y PURCHASES (eje y) 
    """

    color_cluster = {
        0 : 'blue',
        1 : 'purple',
        2 : 'orange',
        3 : 'green'    
    }

    fig = go.Figure()

    for i in color_cluster.keys():

        fig.add_trace(
            go.Scatter(
                x = df_clusters[df_clusters["cluster"] == i]["BALANCE"],
                y = df_clusters[df_clusters["cluster"] == i]["PURCHASES"],
                mode = "markers",
                name = 'Cluster ' + str(i),
                marker_color = color_cluster[i],
            )
        )

    fig.update_traces(marker=dict(size=12,
                                line=dict(width=2,
                                            color='DarkSlateGrey')),
                    selector=dict(mode='markers'))

    fig.update_layout(title = "Purchases VS. Balance por Cluster (Gráfico de puntos)", xaxis_title = "BALANCE", yaxis_title = "PURCHASES", title_x=0.5)
    return fig


def radar_chart_clusters():

    """
    Output:
        fig. go.Figure(). Representación gráfica de un radar chart que ilustra para cada cluster los medias de las variables de frecuencia
    """

    medias = pd.DataFrame(df_clusters.groupby("cluster")[['PURCHASES_FREQUENCY',
                                                            'BALANCE_FREQUENCY',
                                                            'ONEOFF_PURCHASES_FREQUENCY',
                                                            'PURCHASES_INSTALLMENTS_FREQUENCY',
                                                            'CASH_ADVANCE_FREQUENCY']].mean()).reset_index()

    fig = go.Figure()

    categories = ['Purchases Frequency', 'Balance Frequency','Unique Purchase Frequency',
                'Purchases Installments Frequency', 'Cash Advance Frequency']

    for i in medias["cluster"].unique().tolist():

        radios = medias[medias["cluster"] == i][['PURCHASES_FREQUENCY',
                                                 'BALANCE_FREQUENCY',
                                                 'ONEOFF_PURCHASES_FREQUENCY',
                                                 'PURCHASES_INSTALLMENTS_FREQUENCY',
                                                 'CASH_ADVANCE_FREQUENCY']].values

        fig.add_trace(go.Scatterpolar(
                r = radios[0], #0.945247 0.977679 0.681029 0.728528 0.059451
                theta=categories,
                fill='toself',
                name='Cluster {}'.format(i)
            ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 1]
        )),
    showlegend=True
    )

    fig.update_layout(width = 900, height = 600, title = "Frecuencias por Cluster",
                    title_x=0.5, bargap = 0.2)

    return fig

