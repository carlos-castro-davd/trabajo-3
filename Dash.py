# TRABAJO 3
# SONIA GARCÍA LORENZANA Y CRISTINA ACÍN

# Importamos las librerias mínimas necesarias
import numpy as np
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
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
                            title="Histograma: Variable Balance",
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

        dcc.Dropdown(
            id="valores-grafico-barras-variables",
            options=[
                {'label': 'Credit Limit', 'value': 'CREDIT_LIMIT'},
                {'label': 'Balance', 'value': 'BALANCE'},
                {'label': ' Purchases', 'value': 'PURCHASES'},
                {'label': 'Advanced Cash', 'value': 'CASH_ADVANCE'},
                {'label': 'Unique Purchases', 'value': 'ONEOFF_PURCHASES'},
            ],
            value='CREDIT_LIMIT'
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


    ],

    style={  # Cambiamos el estilo de la ventana principal (toda la página)
        "margin-right": "50px",
        "margin-left": "50px",
        "margin-top": "50px",
        "border-style": "double",
        "border-width": "5px"
    }
)


@app.callback(
    Output('grafico-barras-variables', 'figure'),
    Input('valores-grafico-barras-variables', 'value')
)
def actualizar_grafico_barras(nombre_variable):

    print(nombre_variable)
    fig = graficos_barras_variables(nombre_variable)

    return fig


if __name__ == '__main__':
    app.run_server()
