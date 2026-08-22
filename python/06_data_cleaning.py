import pandas as pd

customers_df = pd.read_csv("data/customers.csv")
subscriptions_df = pd.read_csv("data/subscriptions.csv")
usage_df = pd.read_csv("data/usage.csv")
churn_df = pd.read_csv("data/churn.csv")
transactions_df = pd.read_csv("data/transactions.csv")

print("=" * 50)
print("DATA CLEANING & VALIDATION REPORT")
print("=" * 50)

# 1. Missing customer_id checks
print("\n--- Missing customer_id ---")
for name, df in [("customers", customers_df), ("subscriptions", subscriptions_df),
                  ("usage", usage_df), ("churn", churn_df), ("transactions", transactions_df)]:
    missing = df["customer_id"].isnull().sum()
    print(f"{name}: {missing} missing customer_id")

# 2. Duplicate customer_id checks (should be unique in customers/subscriptions/usage/churn)
print("\n--- Duplicate customer_id ---")
for name, df in [("customers", customers_df), ("subscriptions", subscriptions_df),
                  ("usage", usage_df), ("churn", churn_df)]:
    dupes = df["customer_id"].duplicated().sum()
    print(f"{name}: {dupes} duplicate customer_id")

# 3. Duplicate transaction_id
dup_txn = transactions_df["transaction_id"].duplicated().sum()
print(f"\ntransactions: {dup_txn} duplicate transaction_id")

# 4. Invalid ages
invalid_age = customers_df[(customers_df["age"] < 18) | (customers_df["age"] > 100)]
print(f"\n--- Invalid ages (<18 or >100) ---\n{len(invalid_age)} rows")

# 5. Invalid tenure (negative)
invalid_tenure = customers_df[customers_df["tenure_months"] < 0]
print(f"\n--- Invalid tenure_months (<0) ---\n{len(invalid_tenure)} rows")

# 6. Negative monthly_charges
negative_charges = subscriptions_df[subscriptions_df["monthly_charges"] < 0]
print(f"\n--- Negative monthly_charges ---\n{len(negative_charges)} rows")

# 7. Negative transaction amounts
negative_amounts = transactions_df[transactions_df["amount"] < 0]
print(f"\n--- Negative transaction amounts ---\n{len(negative_amounts)} rows")

# 8. Missing subscription plans
missing_plan = subscriptions_df[subscriptions_df["plan"].isnull()]
print(f"\n--- Missing subscription plans ---\n{len(missing_plan)} rows")

# 9. Invalid payment methods (not in allowed list)
allowed_methods = ["Credit Card", "Debit Card", "UPI", "Net Banking", "Wallet"]
invalid_methods = subscriptions_df[~subscriptions_df["payment_method"].isin(allowed_methods)]
print(f"\n--- Invalid payment methods ---\n{len(invalid_methods)} rows")

# 10. churned = 1 but churn_date is NULL (or vice versa) - logical consistency check
churn_mismatch_1 = churn_df[(churn_df["churned"] == 1) & (churn_df["churn_date"].isnull())]
churn_mismatch_2 = churn_df[(churn_df["churned"] == 0) & (churn_df["churn_date"].notnull())]
print(f"\n--- churned=1 but churn_date is NULL ---\n{len(churn_mismatch_1)} rows")
print(f"--- churned=0 but churn_date is NOT NULL ---\n{len(churn_mismatch_2)} rows")

# 11. Invalid payment_status
allowed_status = ["Paid", "Failed", "Refunded"]
invalid_status = transactions_df[~transactions_df["payment_status"].isin(allowed_status)]
print(f"\n--- Invalid payment_status ---\n{len(invalid_status)} rows")

print("\n" + "=" * 50)
print("VALIDATION COMPLETE")
print("=" * 50)