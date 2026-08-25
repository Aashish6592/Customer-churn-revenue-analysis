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
    -- 4. Churn by Usage Category
WITH usage_data AS (
    SELECT
        CASE
            WHEN u.monthly_usage_hours < 20 THEN 'Low'
            WHEN u.monthly_usage_hours BETWEEN 20 AND 50 THEN 'Medium'
            ELSE 'High'
        END AS usage_category,
        c.churned
    FROM usage u
    JOIN churn c ON u.customer_id = c.customer_id
)
SELECT
    usage_category,
    COUNT(*) AS total_customers,
    SUM(churned) AS churned_customers,
    ROUND(100.0 * SUM(churned) / COUNT(*), 2) AS churn_rate_percent
FROM usage_data
GROUP BY usage_category
ORDER BY 
    CASE usage_category
        WHEN 'Low' THEN 1
        WHEN 'Medium' THEN 2
        ELSE 3
    END;

-- 5. Churn by Support Tickets
WITH ticket_data AS (
    SELECT
        CASE
            WHEN u.support_tickets = 0 THEN '0 tickets'
            WHEN u.support_tickets BETWEEN 1 AND 2 THEN '1-2 tickets'
            WHEN u.support_tickets BETWEEN 3 AND 5 THEN '3-5 tickets'
            ELSE '6+ tickets'
        END AS ticket_group,
        c.churned
    FROM usage u
    JOIN churn c ON u.customer_id = c.customer_id
)
SELECT
    ticket_group,
    COUNT(*) AS total_customers,
    SUM(churned) AS churned_customers,
    ROUND(100.0 * SUM(churned) / COUNT(*), 2) AS churn_rate_percent
FROM ticket_data
GROUP BY ticket_group
ORDER BY 
    CASE ticket_group
        WHEN '0 tickets' THEN 1
        WHEN '1-2 tickets' THEN 2
        WHEN '3-5 tickets' THEN 3
        ELSE 4
    END;

-- 6. Churn by Auto-Renewal
SELECT
    s.auto_renewal,
    COUNT(*) AS total_customers,
    SUM(c.churned) AS churned_customers,
    ROUND(100.0 * SUM(c.churned) / COUNT(*), 2) AS churn_rate_percent
FROM subscriptions s
JOIN churn c ON s.customer_id = c.customer_id
GROUP BY s.auto_renewal
ORDER BY churn_rate_percent DESC;