-- 1. Total Customers
SELECT COUNT(*) AS total_customers FROM customers;

-- 2. Total Churned vs Active Customers
SELECT
    SUM(churned) AS churned_customers,
    COUNT(*) - SUM(churned) AS active_customers
FROM churn;

-- 3. Overall Churn Rate
SELECT
    COUNT(*) AS total_customers,
    SUM(churned) AS churned_customers,
    ROUND(100.0 * SUM(churned) / COUNT(*), 2) AS churn_rate_percent
FROM churn;

-- 4. Total Revenue (from all transactions with status 'Paid')
SELECT
    ROUND(SUM(amount), 2) AS total_revenue
FROM transactions
WHERE payment_status = 'Paid';

-- 5. Average Monthly Charges (active customers only)
SELECT
    ROUND(AVG(s.monthly_charges), 2) AS avg_monthly_charges
FROM subscriptions s
JOIN churn c ON s.customer_id = c.customer_id
WHERE c.churned = 0;

-- 6. Monthly Recurring Revenue (MRR) - sum of monthly charges of active customers
SELECT
    ROUND(SUM(s.monthly_charges), 2) AS monthly_recurring_revenue
FROM subscriptions s
JOIN churn c ON s.customer_id = c.customer_id
WHERE c.churned = 0;