import plotly.graph_objects as go
from variables import *
import plotly.express as px
from plotly.subplots import *
import numpy as np 

def graficos_barras_variables(nombre_variable):

    fig = go.Figure(px.bar(df.groupby('TENURE').mean()[nombre_variable]))

    return fig

"""def info_clusters(numero_cluster):

    means_credit_limit = df_clusters.groupby('cluster').mean()['CREDIT_LIMIT'].values
    means_balance_limit = df_clusters.groupby('cluster').mean()['BALANCE'].values
    means_purchases_limit = df_clusters.groupby('cluster').mean()['PURCHASES'].values
    means_cash_advance_limit = df_clusters.groupby('cluster').mean()['CASH_ADVANCE'].values
    means_minimum_payments_limit = df_clusters.groupby('cluster').mean()['MINIMUM_PAYMENTS'].values
    means_payments_limit = df_clusters.groupby('cluster').mean()['PAYMENTS'].values

    cluster_names = ["0","1","2","3"]

    df_variables = pd.DataFrame(
                        {'cluster': cluster_names,
                        'credit_limit': means_credit_limit,
                        'balance': means_balance_limit,
                        'pruchases': means_purchases_limit,
                        'cash_advance': means_cash_advance_limit,
                        'minimum_payments': means_minimum_payments_limit,
                        'payments': means_payments_limit,
                        })

    variable_names= ['Credit Limit', 'Balance', 'Purchases', 'Cash Advance', 'Minimum Payments', 'Payments']

    valores_primer_cluster = np.array([7284.607938, 1483.370003, 4070.525973, 416.412323, 781.144880, 4083.630226])
    valores_segundo_cluster = np.array([3272.034108, 587.491306, 599.382552, 136.452908, 445.604001, 879.249391])
    valores_tercer_cluster = np.array([4131.819553, 2100.521034, 243.428715, 2225.840189, 1063.410985, 1934.865207])
    valores_cuarto_cluster = np.array([10309.629630, 7232.476288, 1903.598919, 3840.969261, 3266.247218, 4100.758674]) 




    data = [
        go.Bar(
            x = variable_names,
            y = valores_primer_cluster,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred","lightblue", "purple"]#,,"lightblue","indigo",'black'],
        )
    ]

    layout = go.Layout(title = "DISTRIBUCIÓN DE VARIABLES PARA EL PRIMER CLUSTER", xaxis_title = "VARIABLES",
                    yaxis_title = "CLUSTER 0", title_x=0.5)

    fig = go.Figure(data = data, layout = layout)
    fig.update_yaxes(range=[0,10000])






    data = [
        go.Bar(
            x = variable_names,
            y = valores_segundo_cluster,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred","lightblue", "purple"]#,,"lightblue","indigo",'black'],
        )
    ]

    layout = go.Layout(title = "DISTRIBUCIÓN DE VARIABLES PARA EL SEGUNDO CLUSTER", xaxis_title = "VARIABLES",
                    yaxis_title = "CLUSTER 1", title_x=0.5)

    fig = go.Figure(data = data, layout = layout)
    fig.update_yaxes(range=[0,10000])








    data = [
        go.Bar(
            x = variable_names,
            y = valores_tercer_cluster,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred","lightblue", "purple"]#,,"lightblue","indigo",'black'],
        )
    ]

    layout = go.Layout(title = "DISTRIBUCIÓN DE VARIABLES PARA EL TERCER CLUSTER", xaxis_title = "VARIABLES",
                    yaxis_title = "CLUSTER 2", title_x=0.5)

    fig = go.Figure(data = data, layout = layout)
    fig.update_yaxes(range=[0,10000])






    data = [
        go.Bar(
            x = variable_names,
            y = valores_cuarto_cluster,
            marker_color = ["cornflowerblue","sandybrown","mediumseagreen", "indianred","lightblue", "purple"]#,,"lightblue","indigo",'black'],
        )
    ]

    layout = go.Layout(title = "DISTRIBUCIÓN DE VARIABLES PARA EL CUARTO CLUSTER", xaxis_title = "VARIABLES",
                    yaxis_title = "CLUSTER 3", title_x=0.5)

    fig = go.Figure(data = data, layout = layout)
    fig.update_yaxes(range=[0,10000])




    return fig """



