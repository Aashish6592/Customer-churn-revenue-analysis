import pandas as pd

customers_df = pd.read_csv("data/customers.csv")
subscriptions_df = pd.read_csv("data/subscriptions.csv")
usage_df = pd.read_csv("data/usage.csv")
churn_df = pd.read_csv("data/churn.csv")

df = customers_df.merge(subscriptions_df, on="customer_id").merge(usage_df, on="customer_id").merge(churn_df, on="customer_id")

# Focus only on active (non-churned) customers
active_df = df[df["churned"] == 0].copy()

# Calculate risk score based on 5 factors
active_df["risk_score"] = (
    (active_df["contract_type"] == "Monthly").astype(int) +
    (active_df["auto_renewal"] == False).astype(int) +
    (active_df["monthly_usage_hours"] < 20).astype(int) +
    (active_df["support_tickets"] >= 3).astype(int) +
    (active_df["tenure_months"] < 12).astype(int)
)

# Assign risk level based on score
def assign_risk_level(score):
    if score >= 3:
        return "High Risk"
    elif score >= 1:
        return "Medium Risk"
    else:
        return "Low Risk"

active_df["risk_level"] = active_df["risk_score"].apply(assign_risk_level)

# Summary by risk level
risk_summary = active_df.groupby("risk_level").agg(
    customer_count=("customer_id", "count"),
    total_monthly_revenue=("monthly_charges", "sum"),
    avg_monthly_charges=("monthly_charges", "mean")
).round(2)

print(risk_summary)

# Save customer-level risk data (for Power BI)
output_cols = ["customer_id", "plan", "contract_type", "monthly_charges", "tenure_months",
               "monthly_usage_hours", "support_tickets", "auto_renewal", "risk_score", "risk_level"]
active_df[output_cols].to_csv("data/revenue_risk.csv", index=False)

print("\nRevenue risk data saved to data/revenue_risk.csv")