import dash_bootstrap_components as dbc
from dash_extensions.enrich import DashProxy, MultiplexerTransform, NoOutputTransform
from front.layout import setup_main_layout
import front.callbacks

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
        NoOutputTransform() # コールバックで出力指定をしなくても良いオプション
    ]
)

app.titlte = "TEST PROJECT TITLE"
app = setup_main_layout(app)
server = app.server

app.run_server(debug=True, host="0.0.0.0", port="8080", threaded=True)
