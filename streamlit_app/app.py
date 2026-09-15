import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

from config import DATABASE_URL

st.set_page_config(
    page_title="EDIP",
    layout="wide"
)

st.title(
    "Enterprise Decision Intelligence Platform"
)

engine = create_engine(
    DATABASE_URL
)

kpi_query = """
SELECT
    COALESCE(SUM(revenue),0) AS revenue,
    COALESCE(SUM(profit),0) AS profit,
    COALESCE(SUM(quantity),0) AS units_sold,
    COUNT(*) AS transactions
FROM warehouse.fact_sales
"""

department_query = """
SELECT
    department,
    SUM(revenue) AS revenue
FROM warehouse.fact_sales
GROUP BY department
ORDER BY revenue DESC
"""

region_query = """
SELECT
    region,
    SUM(revenue) AS revenue
FROM warehouse.fact_sales
GROUP BY region
ORDER BY revenue DESC
"""

with engine.connect() as connection:
    kpis = pd.read_sql(
        kpi_query,
        connection
    )

    departments = pd.read_sql(
        department_query,
        connection
    )

    regions = pd.read_sql(
        region_query,
        connection
    )

revenue = float(
    kpis.loc[0, "revenue"]
)

profit = float(
    kpis.loc[0, "profit"]
)

units = int(
    kpis.loc[0, "units_sold"]
)

transactions = int(
    kpis.loc[0, "transactions"]
)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Revenue",
    f"₹{revenue:,.0f}"
)

c2.metric(
    "Profit",
    f"₹{profit:,.0f}"
)

c3.metric(
    "Units Sold",
    f"{units:,}"
)

c4.metric(
    "Transactions",
    f"{transactions:,}"
)

st.subheader(
    "Revenue by Department"
)

st.bar_chart(
    departments.set_index(
        "department"
    )
)

st.subheader(
    "Revenue by Region"
)

st.bar_chart(
    regions.set_index(
        "region"
    )
)

st.dataframe(
    departments,
    use_container_width=True
)
