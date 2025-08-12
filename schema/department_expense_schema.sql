-- department_expense_schema.sql

-- Table of departments with unique ID, name, and allocated budget
CREATE TABLE Departments (
    department_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    budget NUMERIC(12, 2) NOT NULL
);

-- Table of vendors with optional category classification
CREATE TABLE Vendors (
    vendor_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(100)
);

-- Table of expense records linking to departments and vendors
CREATE TABLE Expenses (
    expense_id SERIAL PRIMARY KEY,
    department_id INTEGER REFERENCES Departments(department_id),
    vendor_id INTEGER REFERENCES Vendors(vendor_id),
    amount NUMERIC(12, 2) NOT NULL,
    expense_date DATE NOT NULL,
    category VARCHAR(100),
    approval_status VARCHAR(50)
);

-- View to summarize department spending by month
CREATE VIEW monthly_department_spend AS
SELECT 
    d.name AS department,
    DATE_TRUNC('month', e.expense_date) AS month,
    SUM(e.amount) AS total_spent
FROM expenses e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.name, DATE_TRUNC('month', e.expense_date)
ORDER BY d.name, month;
