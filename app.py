from dash import Dash
import dash_mantine_components as dmc

from index import lyt
from callbacks import callbacks_baby

app = Dash(__name__, external_stylesheets=[dmc.styles.DATES])

app.layout=lyt

callbacks_baby(app)

if __name__=="__main__":
    app.run_server(debug=True, port="8040")
