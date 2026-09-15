SELECT
    SUM(revenue) AS total_revenue
FROM warehouse.fact_sales
WHERE sale_date >= DATE_TRUNC(
    'month',
    CURRENT_DATE - INTERVAL '1 month'
)
AND sale_date < DATE_TRUNC(
    'month',
    CURRENT_DATE
);

SELECT
    department,
    SUM(revenue) AS revenue
FROM warehouse.fact_sales
WHERE sale_date >= DATE_TRUNC(
    'month',
    CURRENT_DATE - INTERVAL '1 month'
)
AND sale_date < DATE_TRUNC(
    'month',
    CURRENT_DATE
)
GROUP BY department
ORDER BY revenue DESC;

SELECT
    SUM(profit) AS total_profit
FROM warehouse.fact_sales
WHERE sale_date >= DATE_TRUNC(
    'month',
    CURRENT_DATE - INTERVAL '1 month'
)
AND sale_date < DATE_TRUNC(
    'month',
    CURRENT_DATE
);

SELECT
    SUM(inventory_value) AS inventory_value
FROM warehouse.fact_inventory;
