from dash import html
from dash_extensions.enrich import DashBlueprint
import dash_bootstrap_components as dbc
from dash.dependencies import Output
from dash_extensions.enrich import Input

class BtnSample(object):

    def __init__(self):
        self.bp = DashBlueprint()
        self.bp.layout = dbc.Row([
            dbc.Col(
                dbc.Label(id="btn_output_label_id", children=["Button not clicked"]),
                width=3,
                ),
            dbc.Col(
                dbc.Button(id="btn_output_btn_id", color="primary", className="me-1", children="Run Job!"),
                width=4,
                ),
            ],
            justify="start"
        )
        self.bp.callback(
            output=Output("btn_output_label_id", "children"),
            inputs=Input("btn_output_btn_id", "n_clicks"),
            prevent_initial_call=True
        )(self.__callback_btn)

    def __callback_btn(self, n_clicks):
        print(f"Clicked {n_clicks} times")
        return [f"Clicked {n_clicks} times"]

    @property
    def BP(self):
        return self.bp