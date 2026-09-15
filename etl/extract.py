import pandas as pd

from config import RAW_DIR


def extract_all():
    return {
        "customers": pd.read_excel(
            RAW_DIR / "customers" / "customers.xlsx"
        ),
        "products": pd.read_csv(
            RAW_DIR / "products" / "products.csv"
        ),
        "sales": pd.read_csv(
            RAW_DIR / "sales" / "sales.csv"
        ),
        "inventory": pd.read_csv(
            RAW_DIR / "inventory" / "inventory.csv"
        ),
        "finance": pd.read_csv(
            RAW_DIR / "finance" / "finance.csv"
        )
    }
