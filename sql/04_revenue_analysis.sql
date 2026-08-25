-- 1. Revenue Lost (from churned customers)
SELECT
    ROUND(SUM(s.monthly_charges), 2) AS revenue_lost
FROM subscriptions s
JOIN churn c ON s.customer_id = c.customer_id
WHERE c.churned = 1;

-- 2. Revenue by Plan (active customers only)
SELECT
    s.plan,
    COUNT(*) AS active_customers,
    ROUND(SUM(s.monthly_charges), 2) AS total_monthly_revenue,
    ROUND(AVG(s.monthly_charges), 2) AS avg_charge_per_customer
FROM subscriptions s
JOIN churn c ON s.customer_id = c.customer_id
WHERE c.churned = 0
GROUP BY s.plan
ORDER BY total_monthly_revenue DESC;

-- 3. Failed/Refunded Transactions Impact
SELECT
    payment_status,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM transactions
GROUP BY payment_status
ORDER BY total_amount DESC;

-- 4. Revenue at Risk (active customers with high-risk profile)
-- High risk = high charges + low usage + monthly contract + no auto-renewal + multiple tickets
SELECT
    COUNT(*) AS high_risk_customers,
    ROUND(SUM(s.monthly_charges), 2) AS revenue_at_risk
FROM subscriptions s
JOIN usage u ON s.customer_id = u.customer_id
JOIN churn c ON s.customer_id = c.customer_id
WHERE c.churned = 0
    AND s.contract_type = 'Monthly'
    AND s.auto_renewal = false
    AND u.monthly_usage_hours < 20
    AND u.support_tickets >= 3;

-- 5. Churn Reason Breakdown
SELECT
    churn_reason,
    COUNT(*) AS customer_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM churn
WHERE churned = 1
GROUP BY churn_reason
ORDER BY customer_count DESC;