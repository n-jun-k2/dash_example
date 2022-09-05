import dash_bootstrap_components as dbc
from dash import dcc


GRAPH_EXAMPLE_GRAPH_ID = "graph_example_graph_id"
GRAPH_EXAMPLE_BTN_ID = "graph_example_btn_id"
GRAPH_EXAMPLE_GRAPH_COL_ID = "graph_example_graph_col_id"

graph_example_bar_row = dbc.Row([
    dbc.Col(
        dbc.Button(
            id=GRAPH_EXAMPLE_BTN_ID,
            children="Generate Graph",
            color="primary", className="ms=2"
        ),
        width="auto"
    ),
    dbc.Col(
        id=GRAPH_EXAMPLE_GRAPH_COL_ID,
        children=dcc.Graph(id=GRAPH_EXAMPLE_GRAPH_ID),
        width="auto",
        style={'display': 'none'}
    )
])