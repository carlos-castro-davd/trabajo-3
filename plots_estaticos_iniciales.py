import plotly.graph_objects as go
from variables import *
import plotly.express as px


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
            title="Diagrama de cajas: Variable Balance",
            xaxis_title="Balance (saldo en la cuenta)",
            width=600,
            height=600,
        )
    )
    return fig
