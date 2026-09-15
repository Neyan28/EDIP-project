import pandas as pd

from config import REJECTED_DIR


def validate_sales(df):
    work = df.copy()

    work["sale_date"] = pd.to_datetime(
        work["sale_date"],
        errors="coerce"
    )

    work["quantity"] = pd.to_numeric(
        work["quantity"],
        errors="coerce"
    )

    invalid = work[
        work["sale_date"].isna()
        | work["customer_id"].isna()
        | work["product_id"].isna()
        | (work["quantity"] <= 0)
    ].copy()

    valid = work.drop(
        index=invalid.index
    ).copy()

    return valid, invalid


def validate_all(data):
    REJECTED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    valid_sales, invalid_sales = validate_sales(
        data["sales"]
    )

    invalid_sales.to_csv(
        REJECTED_DIR / "sales_rejected.csv",
        index=False
    )

    data["sales"] = valid_sales

    return data
