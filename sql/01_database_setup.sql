CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    age INT,
    gender VARCHAR(20),
    city VARCHAR(50),
    signup_date DATE,
    tenure_months INT
);

CREATE TABLE subscriptions (
    customer_id VARCHAR(10) REFERENCES customers(customer_id),
    plan VARCHAR(20),
    contract_type VARCHAR(20),
    monthly_charges DECIMAL(10,2),
    payment_method VARCHAR(30),
    auto_renewal BOOLEAN
);

CREATE TABLE usage (
    customer_id VARCHAR(10) REFERENCES customers(customer_id),
    monthly_usage_hours DECIMAL(6,2),
    login_frequency INT,
    support_tickets INT,
    complaints INT
);

CREATE TABLE transactions (
    transaction_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10) REFERENCES customers(customer_id),
    transaction_date DATE,
    amount DECIMAL(10,2),
    payment_status VARCHAR(20)
);

CREATE TABLE churn (
    customer_id VARCHAR(10) REFERENCES customers(customer_id),
    churned INT,
    churn_date DATE,
    churn_reason VARCHAR(50)
);