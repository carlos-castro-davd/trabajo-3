# TRABAJO 3
# SONIA GARCÍA LORENZANA Y CRISTINA ACÍN

# Importamos las librerias mínimas necesarias
import numpy as np
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State

from plot_functions import *
from plots_estaticos_iniciales import *
from variables import *

# Inicializamos la aplicación
app = dash.Dash()

# Una vez la hemos inicializado, modificamos el diseño de la aplicación,
# incorporando nuestro análisis exploratorio y modelos de Clustering

# Creamos el primer layout, el cual va a incorporar todo el dashboard
app.layout = html.Div(  # Primer Div que contendrá toda la página
    children=[

        html.H1(  # Título
            children=[
                "TRABAJO 3: SEGMENTACIÓN DE CLIENTES"
            ],
            id="titulo",
            style={
                "text-align": "center",
                "backgroundColor": "lightgrey",
                "padding-top": "10px",
                "margin-bottom": "20px",
                "margin-left": "15px",
                "margin-right": "15px",
                "border-style": "outset",
                "border-color": "ligthgrey",
                "border-width": "5px",
                "height": "50px",
                "font-family": "monospace",
                "font-size": "35px"
            }
        ),

        html.P(  # Descripción general del proyecto
            children=[
                "Una empresa de tarjetas de crédito ha monitorizado los movimientos realizados por algunos de sus clientes durante los últimos 6 meses. "
                "Esta información la ha resumido y la ha agregado a un fichero de datos con el fin de encontrar patrones en dichos clientes. "
                "La empresa nos pide realizar un análisis exploratorio de los datos, además de montar un modelo de clustering para segmentar "
                "a los clientes en función de sus diferentes comportamientos. Todos los aspectos más relevantes se detallan a continuación: "
            ],
            id="primer_párrafo",
            style={
                "display": "block",
                "margin-left": "150px",
                "margin-right": "150px",
                "text-align": "center",
                "text-align": "justify",
                "font-weight": "bold",
                "line-height": "150%",
                "font-family": "monospace",
                "font-size": "14px"
            }
        ),

        #ANÁLISIS EXPLORATORIO

        html.H1(  # Título Análisis Exploratorio
            children=[
                "ANÁLISIS EXPLORATORIO"
            ],
            id="titulo_análisis exploratorio",
            style={
                "text-align": "center",
                "backgroundColor": "lightgrey",
                "padding-top": "5px",
                "padding-bottom": "2px",
                "margin-bottom": "20px",
                "margin-left": "30%",
                "margin-right": "30%",
                "margin-top": "30px",
                "border-style": "dashed solid",
                "border-color": "ligthgrey",
                "border-width": "2px",
                "height": "40px",
                "font-family": "monospace",
                "font-size": "25px"
            }
        ),

        html.Div(  # Primeros dos gráficos, distribución de la variable BALANCE. CON OUTLIERS
            children=[
                dcc.Graph(  # Histograma de la variable BALANCE
                    figure=go.Figure(
                        data=[
                            go.Histogram(
                                x=df["BALANCE"],
                                marker_color="steelblue",
                                name="Balance",
                            )
                        ],
                        layout=go.Layout(
                            title="Histograma: Variable Balance CON OUTLIERS",
                            xaxis_title="Balance (saldo en la cuenta)",
                            yaxis_title="Número de clientes",
                            width=600,
                            height=600,
                            bargap=0.2
                        )
                    ),
                    style={
                        "display": "inline-block",
                        "margin-left": "5%",
                        "margin-right": "3%"
                    }
                ),

                dcc.Graph(  # Diagrama de cajas de la variable BALANCE
                    figure=diagrama_cajas_balance_con_outliers(),
                    style={
                        "display": "inline-block"
                    }
                ),
            ],
        ),

        html.P(  # Explicación de los outliers
            children=[
                "Los dos gráficos siguientes muestran la distribución de los datos una vez ya hemos identificado el primer cluster (procedente de los outliers). "
            ],
            id="explicación_outliers",
            style=style_texto
        ),

        html.Div(  # Segundos dos gráficos, distribución de la variable BALANCE. SIN OUTLIERS
            children=[
                dcc.Graph(  # Histograma de la variable BALANCE SIN OUTLIERS
                    figure=go.Figure(
                        data=[
                            go.Histogram(
                                x=df_sin_outliers["BALANCE"],
                                marker_color="green",
                                name="Balance",
                            )
                        ],
                        layout=go.Layout(
                            title="Histograma: Variable Balance SIN OUTLIERS",
                            xaxis_title="Balance (saldo en la cuenta)",
                            yaxis_title="Número de clientes",
                            width=600,
                            height=600,
                            bargap=0.2
                        )
                    ),
                    style={
                        "display": "inline-block",
                        "margin-left": "5%",
                        "margin-right": "3%",
                        "text-align": "center"
                    }
                ),

                dcc.Graph(  # Diagrama de cajas de la variable BALANCE SIN OUTLIERS
                    figure=diagrama_cajas_sin_outliers(),
                    style={
                        "display": "inline-block",
                    }
                ),
            ],
        ),

        html.Div(
            
            children=[
                dcc.Dropdown(
                id="valores-grafico-barras-variables",
                options=[
                    {'label': 'Credit Limit', 'value': 'CREDIT_LIMIT'},
                    {'label': 'Balance', 'value': 'BALANCE'},
                    {'label': ' Purchases', 'value': 'PURCHASES'},
                    {'label': 'Advanced Cash', 'value': 'CASH_ADVANCE'},
                    {'label': 'Unique Purchases', 'value': 'ONEOFF_PURCHASES'},
                    {'label': 'Minimum Payments', 'value': 'MINIMUM_PAYMENTS'},
                    {'label': 'Payments', 'value': 'PAYMENTS'},
                ],
                value='CREDIT_LIMIT',
                style = {
                    "width": "750px"
                }
        ),
            ],
        style={
                    "margin-left": "20%",
                }

        ),

        # Tercera fila, gráfico de barras variables
        dcc.Graph(
            id="grafico-barras-variables",
            style={
                "display": "block",
                "margin-left": "150px",
                "margin-right": "150px"
            }
        ),


        # CLUSTERS (Representación y Explicación de cada uno de ellos)

        html.H1(  # Título clusters
            children=[
                "CLUSTERS"
            ],
            id="titulo_clusters",
            style={
                "text-align": "center",
                "backgroundColor": "lightgrey",
                "padding-top": "5px",
                "padding-bottom": "2px",
                "margin-bottom": "20px",
                "margin-left": "30%",
                "margin-right": "30%",
                "margin-top": "30px",
                "border-style": "dashed solid",
                "border-color": "ligthgrey",
                "border-width": "2px",
                "height": "40px",
                "font-family": "monospace",
                "font-size": "25px"
            }
        ),

        html.P(  # Descripción de los clusters
            children=[
                "Los clientes se pueden agrupar en 4 grupos/clusters según su comportamiento: "
            ],
            id="clusters_párrafo",
            style=stlyle_texto_3
        ),

        html.H2(  # Descripción de los clusters
            children=[
                "-Cluster 0: Grupo de clientes con poco saldo en la cuenta y muchas compras (gastones)."
            ],
            style=stlyle_texto_2
        ),

        html.H2(  # Descripción de los clusters
            children=[
                "-Cluster 1: Grupo de clientes que tienen poco saldo en la cuenta por tanto compran poco."
            ],
            style=stlyle_texto_2
        ),

        html.H2(  # Descripción de los clusters
            children=[
                "-Cluster 2: Grupo de clientes que tienen un balance considerado pero que compran muy poco."
            ],
            style=stlyle_texto_2
        ),

        html.H2(  # Descripción de los clusters
            children=[
                "-Cluster 3: Grupo de clientes con mucho saldo en la cuenta y pocas compras (ahorradores)."
            ],
            style=stlyle_texto_2
        ),

        # GRÁFICO CLUSTERS

        html.Div(
            children=[
                dcc.Graph(  # Gráfico barrras varaibles BALANCE y PURCHASES para explicar diferencia entre clusters
                    figure=grafico_barras_balance_purchases(),
                    style={
                        "display": "inline-block",
                        "margin-left": "5%"
                    }
                    ),

                dcc.Graph(  # Scatterplot variables BALANCE y PURCHASES para explicar diferencia entre clusters
                    figure=grafico_simbolos_balance_purchases(),
                    style={
                        "display": "inline-block"
                    }
                ),
            ]
        ),

        html.Div(
            children=[
                dcc.Graph(  # Gráfico de Radar para explicar diferencia entre clusters
                    figure=radar_chart_clusters(),
                    style={
                        "display": "block",
                        "margin-left":"20%",
                        "margin-right":"10%"
                    }
                ),

        html.P(  # Descripción de los clusters
            children=[
                "DESCRIPCIÓN DE LAS VARIABLES POR CLUSTERS"
            ],
            style=stlyle_texto_4
        ),
                

        html.Div(
            children=[
                dcc.Dropdown(  #Dropdown para elegir el cluster a representar en el gráfico de barras
                    id="valores-clusters",
                    options=[
                        {'label': 'Cluster 0', 'value': 0},
                        {'label': 'Cluster 1', 'value': 1},
                        {'label': 'Cluster 2', 'value': 2},
                        {'label': 'Cluster 3', 'value': 3},
                    ],
                    placeholder = 'Elige uno de los clusters',
                    ),
            ],
                style={
                        "display": 'block',
                        "margin-left": "20%",
                        "width": "750px"
                    }
        ),
                
                dcc.Graph(
                    id="info-clusters",
                    style = {
                        "display" : "none",
                        "margin-left": "150px",
                        "margin-right": "150px"
                    }
                ), 
            ]
        ),

        html.P(  # Identificador de un cliente
            children=[
                "RELACIÓN DE UN CLIENTE CON SU CLUSTER"
            ],
            style=stlyle_texto_5
        ),

        html.Div(
            children=[
                dcc.Input(  
                    id="id_cliente",
                    type="text",
                    placeholder = 'ID Cliente',
                ),
            ],
            style={
                "display": 'inline-block',
                "margin-left": "20%",
                "margin-bottom": "30px"
                    }
        ),

        # html.P(
        #     children=[],
        #     id="resultado_cluster",
        #     style={
        #         "display": 'inline-block',
        #         "margin-left": "50%"
        #             }
        # ),

        html.Div(
            children=[
                dcc.Graph(
                    id="radar_cliente_cluster",
                    style={
                        "display" : "none"

                    }
                ),
            ],
        ),
    ],
        style={  # Cambiamos el estilo de la ventana principal (toda la página)
            "margin-right": "50px",
            "margin-left": "50px",
            "margin-top": "50px",
            "margin-bottom" : "50px",
            "border-style": "double",
            "border-width": "5px"
    },
)

@app.callback(  #Callback para el dropdown de los histogramas
    Output('grafico-barras-variables', 'figure'),
    Input('valores-grafico-barras-variables', 'value')
)

def actualizar_grafico_barras(nombre_variable):

    fig = graficos_barras_variables(nombre_variable)

    return fig 

@app.callback(  #Callback para el dropdown de la información de cada cluster
    Output('info-clusters', 'figure'),
    Output('info-clusters','style'),
    Input('valores-clusters', 'value')
)
def actualizar_grafico_barras_clusters(numero_cluster):

    if numero_cluster not in [0,1,2,3]:
        return (go.Figure(data = [], layout = {}),{"display":"none"})

    # Dataset con solo un cluster
    cluster = df_clusters[df_clusters["cluster"] == numero_cluster].copy()
    fig = info_clusters(cluster)

    return fig, {'display':'block'}

@app.callback( 
    #Output('resultado_cluster','children'),    
    Output('radar_cliente_cluster', 'figure'),
    Output('radar_cliente_cluster','style'),
    Input('id_cliente', 'value')
)

def resultado_cluster_function(id_cliente):

    # Qué pasa si no encuentro un cliente concreto 
    if id_cliente not in df_clusters["CUST_ID"].values.tolist():
         return (go.Figure(data = [], layout = {}),{"display":"none"}) 
    

    # Primer paso coger id_cliente y mirar en los datos 
    client_info = df_clusters[df_clusters["CUST_ID"] == id_cliente].copy()

    # Paso 2: Verificar cual es su cluster y escribir su descripcion  
    tipo_cluster = client_info['cluster'].iloc[0]

    # Paso 3: Figura y estilo 
    fig = radar_chart_clusters_representacion(tipo_cluster) 

    return fig, {"display":"block", "margin-left":"20%", "margin-bottom": "30px"} 



# @app.callback( 
#     #Output('resultado_cluster','children'),    
#     Output('radar_cliente_cluster', 'figure'),
#     Output('radar_cliente_cluster','style'),
#     Input('id_cliente', 'value')
# )

# def resultado_cluster_function(id_cliente):

#     # Qué pasa si no encuentro un cliente concreto 

#     if id_cliente not in df_clusters["CUST_ID"].values.tolist():
#          return ([], go.Figure(data = [], layout = {}),{"display":"none"}) 
    

#     # Primer paso coger id_cliente y mirar en los datos 
#     client_info = df_clusters[df_clusters["CUST_ID"] == id_cliente].copy()

#     # Paso 2: Verificar cual es su cluster y escribir su descripcion  
#     tipo_cluster = client_info['cluster'].iloc[0]

#     desc_cluster = {
#         '0': "Cluster 0: Grupo de clientes con poco saldo en la cuenta y muchas compras (gastones)",
#         '1': "Cluster 1: Grupo de clientes que tienen poco saldo en la cuenta por tanto compran poco" ,
#         '2': "Cluster 2: Grupo de clientes que tienen un balance considerado pero que compran muy poco" ,
#         '3': "Cluster 3: Grupo de clientes con mucho saldo en la cuenta y pocas compras (ahorradores)" 
#     }

#     parrafo = desc_cluster[tipo_cluster]

#     # Paso 3: Figura y estilo 
#     fig = radar_chart_clusters_por_usuario(tipo_cluster) 

#     return parrafo,fig, {"display":"block"} 


if __name__ == '__main__':
    app.run_server(debug = True)
