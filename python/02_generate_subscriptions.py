import pandas as pd
import numpy as np

np.random.seed(202)

customers_df = pd.read_csv("data/customers.csv")

n = len(customers_df)

# Plan distribution - Basic most common, Premium least
plans = np.random.choice(["Basic", "Standard", "Premium"], n, p=[0.45, 0.35, 0.20])

# Contract type - link with tenure: higher tenure -> higher chance of Annual
annual_prob = np.clip(customers_df["tenure_months"] / 60, 0.1, 0.7)  # scales with tenure
contract_type = [
    np.random.choice(["Monthly", "Annual"], p=[1 - p, p])
    for p in annual_prob
]

# Monthly charges based on plan
plan_charge_map = {"Basic": (299, 499), "Standard": (599, 899), "Premium": (999, 1499)}
monthly_charges = [
    round(np.random.uniform(*plan_charge_map[plan]), 2) for plan in plans
]

payment_methods = np.random.choice(
    ["Credit Card", "Debit Card", "UPI", "Net Banking", "Wallet"],
    n, p=[0.30, 0.20, 0.30, 0.10, 0.10]
)

# Auto renewal - annual customers more likely to have it True
auto_renewal = [
    np.random.choice([True, False], p=[0.75, 0.25]) if c == "Annual"
    else np.random.choice([True, False], p=[0.40, 0.60])
    for c in contract_type
]

subscriptions_df = pd.DataFrame({
    "customer_id": customers_df["customer_id"],
    "plan": plans,
    "contract_type": contract_type,
    "monthly_charges": monthly_charges,
    "payment_method": payment_methods,
    "auto_renewal": auto_renewal
})

subscriptions_df.to_csv("data/subscriptions.csv", index=False)
print(subscriptions_df.head())
print(f"Total rows: {len(subscriptions_df)}")