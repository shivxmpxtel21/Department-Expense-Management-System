from dash import html, dcc
import dash_bootstrap_components as dbc
from app.utils import load_dataframe

df = load_dataframe()

layout = dbc.Container([
    html.H1("Department Expense Management System", className="text-center my-4"),

    dbc.Row([
        dbc.Col([
            html.Label("Select Date Range:"),
            dcc.DatePickerRange(
                id='date-range-filter',
                start_date=df['expense_date'].min(),
                end_date=df['expense_date'].max(),
                display_format='YYYY-MM-DD'
            )
        ], width=4),
        dbc.Col([
            html.Label("Select Vendor:"),
            dcc.Dropdown(
                id='vendor-filter',
                options=[{"label": v, "value": v} for v in sorted(df['vendor'].unique())],
                placeholder="All Vendors",
                clearable=True
            )
        ], width=4),
        dbc.Col([
            html.Label("Select Department(s):"),
            dcc.Dropdown(
                id='department-filter',
                options=[{"label": d, "value": d} for d in sorted(df['department'].unique())],
                multi=True,
                placeholder="All Departments",
                clearable=True
            )
        ], width=4),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dbc.Card([html.H5(id='total-spend'), html.P("Total Spend")], body=True), width=4),
        dbc.Col(dbc.Card([html.H5(id='transaction-count'), html.P("# of Transactions")], body=True), width=4),
        dbc.Col(dbc.Card([html.H5(id='avg-spend'), html.P("Avg Transaction")], body=True), width=4),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id='monthly-trend-chart'), width=6),
        dbc.Col(dcc.Graph(id='category-breakdown-chart'), width=6),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id='department-comparison-chart'), width=6),
        dbc.Col(dcc.Graph(id='top-vendors-chart'), width=6),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id='vendor-department-breakdown-chart'), width=12),
    ])
], fluid=True)
