CREATE SCHEMA IF NOT EXISTS warehouse;

CREATE SCHEMA IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS warehouse.dim_customer (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_name VARCHAR(200),
    region VARCHAR(100),
    signup_date DATE
);

CREATE TABLE IF NOT EXISTS warehouse.dim_product (
    product_id VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(100),
    unit_cost NUMERIC(14,2),
    unit_price NUMERIC(14,2)
);

CREATE TABLE IF NOT EXISTS warehouse.fact_sales (
    sale_id VARCHAR(50),
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    sale_date DATE,
    quantity INTEGER,
    discount NUMERIC(8,4),
    department VARCHAR(100),
    region VARCHAR(100),
    unit_price NUMERIC(14,2),
    unit_cost NUMERIC(14,2),
    revenue NUMERIC(16,2),
    cost NUMERIC(16,2),
    profit NUMERIC(16,2)
);

CREATE TABLE IF NOT EXISTS warehouse.fact_inventory (
    inventory_id VARCHAR(50),
    product_id VARCHAR(50),
    region VARCHAR(100),
    inventory_date DATE,
    quantity_on_hand INTEGER,
    reorder_level INTEGER,
    unit_cost NUMERIC(14,2),
    inventory_value NUMERIC(16,2)
);

CREATE TABLE IF NOT EXISTS warehouse.fact_finance (
    finance_id VARCHAR(50),
    transaction_date DATE,
    department VARCHAR(100),
    transaction_type VARCHAR(50),
    amount NUMERIC(16,2),
    region VARCHAR(100)
);
