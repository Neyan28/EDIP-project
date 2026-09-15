import pandas as pd

from analytics.kpi import sales_kpis
def test_sales_kpis():
    data = pd.DataFrame({
        "revenue": [1000,2000],
        "profit": [200,500],
        "quantity": [5,10]})
    result = sales_kpis(data)
    assert result["total_revenue"] == 3000
    assert result["total_profit"] == 700
    assert result["units_sold"] == 15
    assert result["transactions"] == 2
