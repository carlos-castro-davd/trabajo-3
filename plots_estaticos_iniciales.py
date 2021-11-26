import plotly.graph_objects as go
from variables import *
import plotly.express as px
from plotly.subplots import *


def diagrama_cajas_sin_outliers():

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

    layout = go.Layout(title = "Purchases VS. Balance por Cluster (Gráfico de barras)", xaxis_title = "CLUSTERS", title_x=0.45)

    fig = go.Figure(data = data, layout = layout)

    return fig


def grafico_simbolos_balance_purchases():
    #fig = px.scatter(df_clusters, x="BALANCE", y="PURCHASES", color="cluster")

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

    fig.update_layout(title = "Purchases VS. Balance por Cluster (Gráfico de puntos)", title_x=0.5)
    return fig


def radar_chart_clusters():

    means_purchases_frecuency_limit = df_clusters.groupby('cluster').mean()['PURCHASES_FREQUENCY'].values
    means_balance_frecuency_limit = df_clusters.groupby('cluster').mean()['BALANCE_FREQUENCY'].values
    means_pruchases_frecuency_limit = df_clusters.groupby('cluster').mean()['PURCHASES_FREQUENCY'].values
    means_purchases_installments_limit = df_clusters.groupby('cluster').mean()['PURCHASES_INSTALLMENTS_FREQUENCY'].values
    means_cash_adv_limit = df_clusters.groupby('cluster').mean()['CASH_ADVANCE_FREQUENCY'].values
    means_unique_pruchase_frecuency_limit = df_clusters.groupby('cluster').mean()['ONEOFF_PURCHASES_FREQUENCY'].values

    cluster_names = ["0","1","2","3"]

    df_radar_chart = pd.DataFrame(
                        {'cluster': cluster_names,
                        'purchases_frecuency': means_purchases_frecuency_limit,
                        'balance_frecuency': means_balance_frecuency_limit,
                        'unique_pruchase': means_unique_pruchase_frecuency_limit,
                        'purchases_installments_freq': means_purchases_installments_limit,
                        'cash_adv_freq': means_cash_adv_limit
                        })


    categories = ['Purchases Frecuency','Balance Frecuency','Unique Pruchase Frecuency',
                'Purchases Installments Frequency', 'Cash Advance Frequency']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[0.945247, 0.977679, 0.681029, 0.728528, 0.059451], #0.945247 0.977679 0.681029 0.728528 0.059451
        theta=categories,
        fill='toself',
        name='Cluster 0'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[0.556312, 0.841441, 0.152768, 0.422003, 0.033380], #0.556312 0.841441 0.152768 0.422003 0.033380
        theta=categories,
        fill='toself',
        name='Cluster 1'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[0.170611, 0.940687, 0.084821, 0.093552, 0.332762], #0.170611 0.940687 0.084821 0.093552 0.332762
        theta=categories,
        fill='toself',
        name='Cluster 2'
    ))
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

    fig.update_layout(width = 900, height = 600, title = "Frecuencias por Cluster",
                    title_x=0.5, bargap = 0.2)

    return fig


def subplot_clusters():

    means_minimum_payments_limit = df_clusters.groupby('cluster').mean()['MINIMUM_PAYMENTS'].values
    means_cash_advance_limit = df_clusters.groupby('cluster').mean()['CASH_ADVANCE'].values
    means_balance_frecuency_limit = df_clusters.groupby('cluster').mean()['BALANCE_FREQUENCY'].values
    means_credit_limit = df_clusters.groupby('cluster').mean()['CREDIT_LIMIT'].values
    means_purchases_limit = df_clusters.groupby('cluster').mean()['PURCHASES'].values
    means_balance_limit = df_clusters.groupby('cluster').mean()['BALANCE'].values
    means_unique_pruchase_frecuency_limit = df_clusters.groupby('cluster').mean()['ONEOFF_PURCHASES_FREQUENCY'].values
    means_purchases_frecuency_limit = df_clusters.groupby('cluster').mean()['PURCHASES_FREQUENCY'].values
    means_cash_adv_limit = df_clusters.groupby('cluster').mean()['CASH_ADVANCE_FREQUENCY'].values

    cluster_names = ["0","1","2","3"]

    fig = make_subplots(rows = 3,
                        cols = 2,
                        #subplot_titles=("Distribución de las notas", "Impacto del test previo",
                                        #"Media según la formación de los padres",
                                        #"Media por formación y grupo étnico")
                    )

    fig.add_trace(
        go.Bar(
            x = cluster_names,
            y = means_credit_limit,
            name = "Parental level",
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred"]
        ),
        row = 1,
        col = 1
    )


    # Segundo gráfico
    fig.add_trace(
        go.Bar(
            x = cluster_names,
            y = means_balance_limit,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred"]
        ),
        row = 1,
        col = 2
    )

    # Tercer gráfico
    fig.add_trace(
        go.Bar(
            x = cluster_names,
            y = means_purchases_limit,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred"]
        ),
        row = 2,
        col = 1
    )

    # Cuarto gráfico
    fig.add_trace(
        go.Bar(
            x = cluster_names,
            y = means_cash_advance_limit,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred"]
        ),
        row = 2,
        col = 2
    )

    # Quinto gráfico
    fig.add_trace(
        go.Bar(
            x = cluster_names,
            y = means_minimum_payments_limit,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred"]
        ),
        row = 3,
        col = 1
    )

    # Sexto gráfico
    fig.add_trace(
        go.Bar(
            x = cluster_names,
            y = means_purchases_frecuency_limit,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred"]
        ),
        row = 3,
        col = 2
    )

    # Modifico las dimensiones totales y el titulo global
    fig.update_layout(width = 1000, height = 900, title = "Información de los Clusters",
                    title_x=0.5, bargap = 0.2, showlegend=False)

    fig.update_xaxes(title_text = "Clusters", row = 1, col = 1)
    fig.update_yaxes(title_text = "Credit Limit", row = 1, col = 1)

    fig.update_xaxes(title_text = "Clusters", row = 1, col = 2)
    fig.update_yaxes(title_text = "Balance", row = 1, col = 2)

    fig.update_xaxes(title_text = "Clusters", row = 2, col = 1)
    fig.update_yaxes(title_text = "Purchases", row = 2, col = 1)

    fig.update_xaxes(title_text = "Clusters", row = 2, col = 2)
    fig.update_yaxes(title_text = "Cash Advance", row = 2, col = 2)

    fig.update_xaxes(title_text = "Clusters", row = 3, col = 1)
    fig.update_yaxes(title_text = "Minimum Payments", row = 3, col = 1)

    fig.update_xaxes(title_text = "Clusters", row = 3, col = 2)
    fig.update_yaxes(title_text = "Purchases Frecuency", row = 3, col = 2)

    return fig


