import dash
from dash.dependencies import Output
from dash_extensions.enrich import Input


@dash.callback(
    output=Output("btn_output_label_id", "children"),
    inputs=Input("btn_output_btn_id", "n_clicks"),
    prevent_initial_call=True
)
def callback(n_clicks):
    print(f"Clicked {n_clicks} times")
    return [f"Clicked {n_clicks} times"]