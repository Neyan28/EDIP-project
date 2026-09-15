def sales_kpis(sales):
    revenue = sales["revenue"].sum()
    profit = sales["profit"].sum()
    quantity = sales["quantity"].sum()

    margin = (
        profit / revenue * 100
        if revenue
        else 0
    )

    return {
        "total_revenue": float(revenue),
        "total_profit": float(profit),
        "profit_margin": float(margin),
        "units_sold": int(quantity),
        "transactions": int(len(sales))
    }


def revenue_by_department(sales):
    return (
        sales
        .groupby(
            "department",
            as_index=False
        )["revenue"]
        .sum()
        .sort_values(
            "revenue",
            ascending=False
        )
    )


def revenue_by_region(sales):
    return (
        sales
        .groupby(
            "region",
            as_index=False
        )["revenue"]
        .sum()
        .sort_values(
            "revenue",
            ascending=False
        )
    )
