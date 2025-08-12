import os
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert
from datetime import datetime

# Set working directory to script location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Load cleaned CSV data
df = pd.read_csv("cleaned_expense_data.csv")
df.columns = [c.strip() for c in df.columns]
df["Expense_Date"] = pd.to_datetime(df["Expense_Date"])

# Connect to PostgreSQL using SQLAlchemy
engine = create_engine("postgresql+psycopg2://postgres:Patriots123@localhost:5432/dem_expense_db")

# Begin transaction block
with engine.begin() as conn:
    metadata = MetaData()
    metadata.reflect(bind=conn)

    # Insert new departments
    dept_table = Table("departments", metadata, autoload_with=conn)
    for dept in df["Department"].unique():
        conn.execute(
            insert(dept_table)
            .values(name=dept, budget=100000)
            .on_conflict_do_nothing(index_elements=["name"])
        )

    # Insert new vendors
    vendor_table = Table("vendors", metadata, autoload_with=conn)
    for vendor in df["Vendor"].unique():
        conn.execute(
            insert(vendor_table)
            .values(name=vendor, category="General")
            .on_conflict_do_nothing(index_elements=["name"])
        )

    # Map department and vendor IDs
    dept_df = pd.read_sql("SELECT department_id, name FROM departments", conn)
    vendor_df = pd.read_sql("SELECT vendor_id, name FROM vendors", conn)

    df_mapped = df.merge(dept_df, left_on="Department", right_on="name", how="left") \
                  .merge(vendor_df, left_on="Vendor", right_on="name", how="left") \
                  .rename(columns={
                      "department_id": "department_id",
                      "vendor_id": "vendor_id"
                  })

    # Prepare expense records
    expense_data = df_mapped[["department_id", "vendor_id", "Amount", "Expense_Date", "Category"]]
    expense_data.columns = ["department_id", "vendor_id", "amount", "expense_date", "category"]

    # Insert expense records
    expense_table = Table("expenses", metadata, autoload_with=conn)
    for _, row in expense_data.iterrows():
        conn.execute(expense_table.insert().values(**row.to_dict()))

print("ETL complete.")








