from dash import html
import dash_bootstrap_components as dbc

search_bar_row = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms=2"
            ),
            width="auto"
        )
    ],
    align="center"
)