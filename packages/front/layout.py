from dash import Dash, html
import dash_bootstrap_components as dbc
from front.components import btn_output_row, search_bar_row, graph_example_bar_row

def setup_main_layout(app: Dash):
    """Dashフレームワークのレイアウト構築フロー
        Args:
            - app (Dash): dashフレームワーク
        Returns:
            (Dash): dashフレームワーク
    """
    app.layout = html.Div([
        btn_output_row,
        search_bar_row,
        graph_example_bar_row
    ])
    return app
