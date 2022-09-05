import dash
from dash.dependencies import Output
from dash_extensions.enrich import Input
import plotly.express as px
import pandas as pd
from front.components import GRAPH_EXAMPLE_GRAPH_ID, GRAPH_EXAMPLE_BTN_ID, GRAPH_EXAMPLE_GRAPH_COL_ID

@dash.callback(
    output=[
        Output(GRAPH_EXAMPLE_GRAPH_ID, "figure"),
        Output(GRAPH_EXAMPLE_GRAPH_COL_ID, "style")
    ],
    inputs=Input(GRAPH_EXAMPLE_BTN_ID, "n_clicks"),
    prevent_initial_call=True
)
def get_graph(n_clicks):
    print("generate graph")
    df = pd.DataFrame(
        {
            "sepal_width": [2, 3, 4, 5],
            "sepal_length": [1, 2, 3, 4]
        }
    )

    fig = px.scatter(
        df, x="sepal_width", y="sepal_length",
        color_discrete_sequence=px.colors.sequential.Viridis,
    )
    return fig, {'display': 'inline'}