from sqlalchemy import create_engine

from config import DATABASE_URL
from database.schema import create_schema


def load_all(data):
    engine = create_engine(
        DATABASE_URL
    )

    create_schema(engine)

    data["customers"].to_sql(
        "dim_customer",
        engine,
        schema="warehouse",
        if_exists="replace",
        index=False
    )

    data["products"].to_sql(
        "dim_product",
        engine,
        schema="warehouse",
        if_exists="replace",
        index=False
    )

    data["sales"].to_sql(
        "fact_sales",
        engine,
        schema="warehouse",
        if_exists="replace",
        index=False
    )

    data["inventory"].to_sql(
        "fact_inventory",
        engine,
        schema="warehouse",
        if_exists="replace",
        index=False
    )

    data["finance"].to_sql(
        "fact_finance",
        engine,
        schema="warehouse",
        if_exists="replace",
        index=False
    )
