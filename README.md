# Departmental Expense Management System (DEMS)

**Final Project – DS 5110: Introduction to Data Management and Processing**  
**Author:** Shivam Patel  
**Institution:** Khoury College of Computer Sciences, Northeastern University  

---

## 📊 Overview

The Departmental Expense Management System (DEMS) is a complete data pipeline and interactive dashboard for analyzing departmental spend across vendors, categories, and time periods. This project showcases:

- A normalized relational database in **PostgreSQL**
- A robust ETL process using **PySpark** and **Pandas**
- An interactive dashboard built with **Dash and Plotly**
- Clean project structure with modularized code and documentation

---

## 🧱 Architecture

- **Data Source:** Raw CSV files (simulated real-world expense data)
- **ETL Pipeline:**
  - Cleaning with **PySpark**
  - Loading with **Pandas + SQLAlchemy** into PostgreSQL
- **Database:** PostgreSQL with foreign keys and a normalized schema
- **Dashboard:** Python Dash app with KPIs, filters, and visualizations
- **Documentation:** ER diagram, screenshots, and SQL views included

---

## 📂 Folder Structure

```
dems/
├── app/              # Dash app modules
│   ├── run.py
│   ├── layout.py
│   ├── callbacks.py
│   └── utils.py
├── etl/              # ETL scripts
│   ├── sparketl.ipynb
│   └── etl_load_expenses.py
├── schema/           # SQL schema + views
│   └── department_expense_schema.sql
├── data/             # Raw and cleaned CSVs
│   ├── raw/
│   └── cleaned/
├── docs/             # ERD and dashboard screenshots
│   ├── erd.png
│   ├── historical spend - dems.png
│   ├── vendor-select-dems.png
│   └── pichart-dems.png
├── tests/            # Placeholder for unit tests
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/dems.git
cd dems
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup PostgreSQL
- Create a database named `dem_expense_db`
- Run the schema script:
  ```bash
  psql -U postgres -d dem_expense_db -f schema/department_expense_schema.sql
  ```

### 4. Run ETL
- Run the PySpark notebook or the PostgreSQL loader:
  ```bash
  python etl/etl_load_expenses.py
  ```

### 5. Launch Dashboard
```bash
python app/run.py
```

---

## 📊 Features

- Date range, vendor, and department filtering
- Summary cards: Total Spend, # of Transactions, Avg Transaction
- Monthly trends, category breakdown, department comparisons
- Vendor-level spend and breakdowns
- Screenshots and ERD included in `/docs`

---

## 🔍 SQL Highlights

- Foreign keys and normalization
- Views: `monthly_department_spend` summarizes monthly totals by department
- Organized, commented schema for transparency

---

## 📎 References

- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Dash Plotly Docs](https://dash.plotly.com/introduction)
- [PySpark API Docs](https://spark.apache.org/docs/latest/api/python/)
- [Expense Management Guidelines (GSA)](https://smartpay.gsa.gov/)
- McKinney, W. (2022). *Python for Data Analysis*, O'Reilly.
- Zaharia et al. (2016). *Apache Spark: A Unified Engine for Big Data Processing*. [DOI:10.1145/2934664](https://doi.org/10.1145/2934664)

---

## 👨‍💻 Author

**Shivam Patel**  
Data Science Program  
Khoury College of Computer Sciences  
Northeastern University  
