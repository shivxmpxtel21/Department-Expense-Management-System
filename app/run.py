from dash import Dash
import dash_bootstrap_components as dbc
from app.layout import layout
from app.callbacks import register_callbacks

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Department Expense Management System"

app.layout = layout
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
