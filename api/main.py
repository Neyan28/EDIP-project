from fastapi import FastAPI
from sqlalchemy import create_engine, text

from config import DATABASE_URL

app = FastAPI(
    title="EDIP API"
)

engine = create_engine(
    DATABASE_URL
)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/kpis")
def kpis():
    query = text(
        "SELECT "
        "COALESCE(SUM(revenue),0) AS revenue, "
        "COALESCE(SUM(profit),0) AS profit, "
        "COALESCE(SUM(quantity),0) AS units_sold, "
        "COUNT(*) AS transactions "
        "FROM warehouse.fact_sales"
    )

    with engine.connect() as connection:
        row = (
            connection
            .execute(query)
            .mappings()
            .one()
        )

    revenue = float(
        row["revenue"]
    )

    profit = float(
        row["profit"]
    )

    margin = (
        profit / revenue * 100
        if revenue
        else 0
    )

    return {
        "total_revenue": revenue,
        "total_profit": profit,
        "profit_margin": margin,
        "units_sold": int(
            row["units_sold"]
        ),
        "transactions": int(
            row["transactions"]
        )
    }


@app.get("/revenue-by-department")
def revenue_by_department():
    query = text(
        "SELECT department, SUM(revenue) AS revenue "
        "FROM warehouse.fact_sales "
        "GROUP BY department "
        "ORDER BY revenue DESC"
    )

    with engine.connect() as connection:
        rows = (
            connection
            .execute(query)
            .mappings()
            .all()
        )

    return [
        dict(row)
        for row in rows
    ]
