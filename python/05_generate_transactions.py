import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

customers_df = pd.read_csv("data/customers.csv")
subscriptions_df = pd.read_csv("data/subscriptions.csv")
churn_df = pd.read_csv("data/churn.csv")

df = customers_df.merge(subscriptions_df, on="customer_id").merge(churn_df, on="customer_id")

today = datetime(2026, 8, 22)

transaction_rows = []
txn_counter = 1

for _, row in df.iterrows():
    signup = datetime.strptime(row["signup_date"], "%Y-%m-%d")

    # End date = churn_date if churned, else today
    if row["churned"] == 1 and pd.notna(row["churn_date"]):
        end_date = datetime.strptime(row["churn_date"], "%Y-%m-%d")
    else:
        end_date = today

    # Generate one transaction per month from signup to end_date
    current = signup
    while current <= end_date:
        # Small variation around the base monthly charge
        amount = round(row["monthly_charges"] * np.random.uniform(0.95, 1.05), 2)

        # Payment status - mostly Paid, some Failed/Refunded
        status = np.random.choice(
            ["Paid", "Failed", "Refunded"], p=[0.90, 0.07, 0.03]
        )

        transaction_rows.append({
            "transaction_id": f"T{100000 + txn_counter}",
            "customer_id": row["customer_id"],
            "transaction_date": current.strftime("%Y-%m-%d"),
            "amount": amount,
            "payment_status": status
        })
        txn_counter += 1
        current += timedelta(days=30)

transactions_df = pd.DataFrame(transaction_rows)
transactions_df.to_csv("data/transactions.csv", index=False)

print(transactions_df.head(10))
print(f"Total rows: {len(transactions_df)}")