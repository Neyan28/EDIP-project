import pandas as pd


def transform_all(data):
    customers = data["customers"].copy()
    products = data["products"].copy()
    sales = data["sales"].copy()
    inventory = data["inventory"].copy()
    finance = data["finance"].copy()

    customers["signup_date"] = pd.to_datetime(
        customers["signup_date"]
    )

    sales["sale_date"] = pd.to_datetime(
        sales["sale_date"]
    )

    inventory["inventory_date"] = pd.to_datetime(
        inventory["inventory_date"]
    )

    finance["transaction_date"] = pd.to_datetime(
        finance["transaction_date"]
    )

    sales = sales.drop_duplicates(
        subset=["sale_id"]
    )

    inventory = inventory.drop_duplicates(
        subset=["inventory_id"]
    )

    finance = finance.drop_duplicates(
        subset=["finance_id"]
    )

    sales["revenue"] = pd.to_numeric(
        sales["revenue"],
        errors="coerce"
    ).fillna(0)

    sales["cost"] = pd.to_numeric(
        sales["cost"],
        errors="coerce"
    ).fillna(0)

    sales["profit"] = (
        sales["revenue"]
        - sales["cost"]
    )

    finance["amount"] = pd.to_numeric(
        finance["amount"],
        errors="coerce"
    ).fillna(0)

    return {
        "customers": customers,
        "products": products,
        "sales": sales,
        "inventory": inventory,
        "finance": finance
    }
