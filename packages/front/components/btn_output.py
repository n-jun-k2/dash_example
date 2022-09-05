from dash import html
import dash_bootstrap_components as dbc


btn_output_row = dbc.Row([
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