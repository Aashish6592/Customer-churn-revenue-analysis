WITH tenure_data AS (
    SELECT
        CASE
            WHEN cu.tenure_months BETWEEN 0 AND 6 THEN '0-6 months'
            WHEN cu.tenure_months BETWEEN 7 AND 12 THEN '7-12 months'
            WHEN cu.tenure_months BETWEEN 13 AND 24 THEN '13-24 months'
            ELSE '25+ months'
        END AS tenure_group,
        c.churned
    FROM customers cu
    JOIN churn c ON cu.customer_id = c.customer_id
)
SELECT
    tenure_group,
    COUNT(*) AS total_customers,
    SUM(churned) AS churned_customers,
    ROUND(100.0 * SUM(churned) / COUNT(*), 2) AS churn_rate_percent
FROM tenure_data
GROUP BY tenure_group
ORDER BY 
    CASE tenure_group
        WHEN '0-6 months' THEN 1
        WHEN '7-12 months' THEN 2
        WHEN '13-24 months' THEN 3
        ELSE 4
    END;