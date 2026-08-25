-- 1. Rank customers by revenue within each plan (window function)
SELECT
    s.customer_id,
    s.plan,
    s.monthly_charges,
    RANK() OVER (PARTITION BY s.plan ORDER BY s.monthly_charges DESC) AS revenue_rank
FROM subscriptions s
JOIN churn c ON s.customer_id = c.customer_id
WHERE c.churned = 0
ORDER BY s.plan, revenue_rank
LIMIT 20;

-- 2. Rank plans by churn rate (using CTE + window function)
WITH plan_churn AS (
    SELECT
        s.plan,
        ROUND(100.0 * SUM(c.churned) / COUNT(*), 2) AS churn_rate
    FROM subscriptions s
    JOIN churn c ON s.customer_id = c.customer_id
    GROUP BY s.plan
)
SELECT
    plan,
    churn_rate,
    RANK() OVER (ORDER BY churn_rate DESC) AS churn_rank
FROM plan_churn;

-- 3. Monthly Churn Trend (churn count by month)
SELECT
    DATE_TRUNC('month', churn_date) AS churn_month,
    COUNT(*) AS churned_customers
FROM churn
WHERE churned = 1
GROUP BY churn_month
ORDER BY churn_month;

-- 4. Running Total of Revenue Over Time (window function)
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', transaction_date) AS txn_month,
        SUM(amount) AS monthly_total
    FROM transactions
    WHERE payment_status = 'Paid'
    GROUP BY txn_month
)
SELECT
    txn_month,
    monthly_total,
    SUM(monthly_total) OVER (ORDER BY txn_month) AS running_total_revenue
FROM monthly_revenue
ORDER BY txn_month;

-- 5. Quarterly Churn Analysis (date functions)
SELECT
    EXTRACT(YEAR FROM churn_date) AS churn_year,
    EXTRACT(QUARTER FROM churn_date) AS churn_quarter,
    COUNT(*) AS churned_customers
FROM churn
WHERE churned = 1
GROUP BY churn_year, churn_quarter
ORDER BY churn_year, churn_quarter;