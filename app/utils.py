import pandas as pd
from sqlalchemy import create_engine

def load_dataframe():
    engine = create_engine('postgresql+psycopg2://postgres:Patriots123@localhost:5432/dem_expense_db')
    df = pd.read_sql("""
        SELECT e.expense_date, d.name AS department, v.name AS vendor,
               e.category, e.amount
        FROM expenses e
        JOIN departments d ON e.department_id = d.department_id
        JOIN vendors v ON e.vendor_id = v.vendor_id
    """, engine)
    df['expense_date'] = pd.to_datetime(df['expense_date'])
    return df
