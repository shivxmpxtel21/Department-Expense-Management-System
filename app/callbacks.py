from dash import Input, Output
import plotly.express as px
from app.utils import load_dataframe

def register_callbacks(app):
    df = load_dataframe()

    @app.callback(
        [Output('total-spend', 'children'),
         Output('transaction-count', 'children'),
         Output('avg-spend', 'children'),
         Output('monthly-trend-chart', 'figure'),
         Output('category-breakdown-chart', 'figure'),
         Output('department-comparison-chart', 'figure'),
         Output('top-vendors-chart', 'figure'),
         Output('vendor-department-breakdown-chart', 'figure')],
        [Input('date-range-filter', 'start_date'),
         Input('date-range-filter', 'end_date'),
         Input('vendor-filter', 'value'),
         Input('department-filter', 'value')]
    )
    def update_dashboard(start_date, end_date, selected_vendor, selected_departments):
        dff = df.copy()
        dff = dff[(dff['expense_date'] >= start_date) & (dff['expense_date'] <= end_date)]

        if selected_vendor:
            dff = dff[dff['vendor'] == selected_vendor]
        if selected_departments:
            dff = dff[dff['department'].isin(selected_departments)]

        total_spend = f"${dff['amount'].sum():,.2f}"
        transaction_count = f"{len(dff):,}"
        avg_transaction = f"${dff['amount'].mean():,.2f}" if not dff.empty else "$0.00"

        dff['Month'] = dff['expense_date'].dt.to_period('M').astype(str)
        monthly_fig = px.line(dff.groupby('Month')['amount'].sum().reset_index(), x='Month', y='amount')
        category_fig = px.pie(dff, names='category', values='amount')
        dept_fig = px.bar(dff.groupby('department')['amount'].sum().reset_index(), x='department', y='amount')
        vendor_fig = px.bar(dff.groupby('vendor')['amount'].sum().nlargest(10).reset_index(), x='vendor', y='amount')
        pivot = dff.groupby(['vendor', 'department'])['amount'].sum().reset_index()
        vendor_dept_fig = px.bar(pivot, x='department', y='amount', color='vendor', barmode='group')

        return total_spend, transaction_count, avg_transaction, monthly_fig, category_fig, dept_fig, vendor_fig, vendor_dept_fig
