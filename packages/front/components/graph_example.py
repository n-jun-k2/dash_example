import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Output
from dash_extensions.enrich import DashBlueprint, Input, ServersideOutput
import plotly.express as px
import pandas as pd

class GraphExample(object):

    GRAPH_EXAMPLE_GRAPH_ID = "graph_example_graph_id"
    GRAPH_EXAMPLE_BTN_ID = "graph_example_btn_id"
    GRAPH_EXAMPLE_GRAPH_COL_ID = "graph_example_graph_col_id"
    CACHE_ID = "cache_id"

    def __init__(self, app):
        self.bp = DashBlueprint()
        self.bp.layout = dbc.Row([
            dcc.Store(id=self.CACHE_ID),
            dbc.Col(
                dbc.Button(
                    id=self.GRAPH_EXAMPLE_BTN_ID,
                    children="Generate Graph",
                    color="primary", className="ms=2"
                ),
                width="auto"
            ),
            dbc.Col(
                id=self.GRAPH_EXAMPLE_GRAPH_COL_ID,
                children=dcc.Graph(id=self.GRAPH_EXAMPLE_GRAPH_ID),
                width="auto",
                style={'display': 'none'}
            )
        ])
        app.callback(
            output=ServersideOutput(self.CACHE_ID, "data"),
            inputs=Input(self.GRAPH_EXAMPLE_BTN_ID, "n_clicks"),
            prevent_initial_call=True
        )(self.__create_data_callbacks)
        self.bp.callback(
            output=[
                Output(self.GRAPH_EXAMPLE_GRAPH_ID, "figure"),
                Output(self.GRAPH_EXAMPLE_GRAPH_COL_ID, "style")
            ],
            inputs=Input(self.CACHE_ID, "data"),
            prevent_initial_call=True
        )(self.__callbacks)

    def __create_data_callbacks(self, __):
        print("__create_data_callbacks")
        df = pd.DataFrame(
            {
                "sepal_width": [2, 3, 4, 5],
                "sepal_length": [1, 2, 3, 4]
            }
        )
        return df

    def __callbacks(self, df):
        print("__callbacks")
        
        fig = px.scatter(
            df, x="sepal_width", y="sepal_length",
            color_discrete_sequence=px.colors.sequential.Viridis,
        )
        return fig, {'display': 'inline'}

    @property
    def BP(self):
        return self.bp