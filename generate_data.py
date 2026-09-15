from pathlib import Path
import random
import numpy as np
import pandas as pd

random.seed(42)
np.random.seed(42)

base = Path(__file__).resolve().parent / "data" / "raw"

for folder in ["customers", "products", "sales", "inventory", "finance"]:
    (base / folder).mkdir(parents=True, exist_ok=True)

regions = ["North", "South", "East", "West"]
departments = ["Retail", "Online", "Enterprise", "Services"]
categories = [
    "Electronics",
    "Furniture",
    "Office",
    "Accessories",
    "Software"
]

customers = pd.DataFrame({
    "customer_id": [
        f"C{i:05d}" for i in range(1, 1001)
    ],
    "customer_name": [
        f"Customer {i}" for i in range(1, 1001)
    ],
    "region": np.random.choice(regions, 1000),
    "signup_date": pd.date_range(
        "2023-01-01",
        periods=1000,
        freq="D"
    )
})

customers.to_excel(
    base / "customers" / "customers.xlsx",
    index=False
)

products = pd.DataFrame({
    "product_id": [
        f"P{i:04d}" for i in range(1, 201)
    ],
    "product_name": [
        f"Product {i}" for i in range(1, 201)
    ],
    "category": np.random.choice(categories, 200),
    "unit_cost": np.round(
        np.random.uniform(20, 1000, 200),
        2
    ),
    "unit_price": np.round(
        np.random.uniform(40, 1500, 200),
        2
    )
})

products.to_csv(
    base / "products" / "products.csv",
    index=False
)

dates = pd.date_range(
    "2025-01-01",
    "2026-09-15",
    freq="D"
)

n = 30000

sales = pd.DataFrame({
    "sale_id": [
        f"S{i:07d}" for i in range(1, n + 1)
    ],
    "order_id": [
        f"O{i:07d}" for i in range(1, n + 1)
    ],
    "customer_id": np.random.choice(
        customers["customer_id"],
        n
    ),
    "product_id": np.random.choice(
        products["product_id"],
        n
    ),
    "sale_date": np.random.choice(
        dates,
        n
    ),
    "quantity": np.random.randint(
        1,
        15,
        n
    ),
    "discount": np.round(
        np.random.uniform(0, 0.20, n),
        4
    ),
    "department": np.random.choice(
        departments,
        n
    ),
    "region": np.random.choice(
        regions,
        n
    )
})

sales = sales.merge(
    products[
        [
            "product_id",
            "unit_price",
            "unit_cost"
        ]
    ],
    on="product_id"
)

sales["revenue"] = np.round(
    sales["quantity"]
    * sales["unit_price"]
    * (1 - sales["discount"]),
    2
)

sales["cost"] = np.round(
    sales["quantity"]
    * sales["unit_cost"],
    2
)

sales["profit"] = np.round(
    sales["revenue"]
    - sales["cost"],
    2
)

sales.loc[10, "quantity"] = -5
sales.loc[20, "customer_id"] = None

sales = pd.concat(
    [
        sales,
        sales.iloc[[30, 31]]
    ],
    ignore_index=True
)

sales.to_csv(
    base / "sales" / "sales.csv",
    index=False
)

inventory_n = 10000

inventory = pd.DataFrame({
    "inventory_id": [
        f"I{i:06d}" for i in range(1, inventory_n + 1)
    ],
    "product_id": np.random.choice(
        products["product_id"],
        inventory_n
    ),
    "region": np.random.choice(
        regions,
        inventory_n
    ),
    "inventory_date": np.random.choice(
        dates,
        inventory_n
    ),
    "quantity_on_hand": np.random.randint(
        0,
        500,
        inventory_n
    ),
    "reorder_level": np.random.randint(
        20,
        100,
        inventory_n
    )
})

inventory["unit_cost"] = inventory["product_id"].map(
    products.set_index("product_id")["unit_cost"]
)

inventory["inventory_value"] = np.round(
    inventory["quantity_on_hand"]
    * inventory["unit_cost"],
    2
)

inventory.to_csv(
    base / "inventory" / "inventory.csv",
    index=False
)

finance_n = 12000

finance = pd.DataFrame({
    "finance_id": [
        f"F{i:06d}" for i in range(1, finance_n + 1)
    ],
    "transaction_date": np.random.choice(
        dates,
        finance_n
    ),
    "department": np.random.choice(
        departments,
        finance_n
    ),
    "transaction_type": np.random.choice(
        ["Expense", "Income"],
        finance_n,
        p=[0.65, 0.35]
    ),
    "amount": np.round(
        np.random.uniform(500, 100000, finance_n),
        2
    ),
    "region": np.random.choice(
        regions,
        finance_n
    )
})

finance.loc[15, "amount"] = -2500

finance.to_csv(
    base / "finance" / "finance.csv",
    index=False
)

print("Enterprise sample data generated.")
