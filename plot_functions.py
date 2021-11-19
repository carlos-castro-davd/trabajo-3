import plotly.graph_objects as go
from variables import *
import plotly.express as px


def graficos_barras_variables(nombre_variable):

    fig = go.Figure(px.bar(df.groupby('TENURE').mean()[nombre_variable]))

    return fig
