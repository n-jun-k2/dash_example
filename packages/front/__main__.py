import dash_bootstrap_components as dbc
from dash_extensions.enrich import DashProxy, MultiplexerTransform, NoOutputTransform, ServersideOutputTransform
from front.components import BtnSample, GraphExample

app = DashProxy(
    __name__,
    update_title="Loading...",
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://codepen.io/chriddyp/pen/bWLwgP.css"
    ],
    suppress_callback_exceptions=True, # 他のファイルでcallbackを定義する場合
    transforms=[
        MultiplexerTransform(), # 複数のコールバックでアウトプットを多重で定義できるオプション
        NoOutputTransform(), # コールバックで出力指定をしなくても良いオプション
        ServersideOutputTransform()
    ],
    # blueprint=GraphExample().BP
)

ge = GraphExample(app)

app.titlte = "TEST PROJECT TITLE"
app.layout = ge.BP.layout
ge.BP.register_callbacks(app)
server = app.server

app.run_server(debug=True, host="0.0.0.0", port="8080", threaded=True)
