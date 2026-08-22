import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

customers_df = pd.read_csv("data/customers.csv")
subscriptions_df = pd.read_csv("data/subscriptions.csv")
usage_df = pd.read_csv("data/usage.csv")

# Merge everything needed to calculate churn probability
df = customers_df.merge(subscriptions_df, on="customer_id").merge(usage_df, on="customer_id")

# Normalize factors to 0-1 range for probability calculation
usage_factor = 1 - (df["monthly_usage_hours"] / df["monthly_usage_hours"].max())  # low usage -> high factor
contract_factor = (df["contract_type"] == "Monthly").astype(int)
tickets_factor = df["support_tickets"] / df["support_tickets"].max()
renewal_factor = (df["auto_renewal"] == False).astype(int)
tenure_factor = 1 - (df["tenure_months"] / df["tenure_months"].max())  # low tenure -> high factor

# Weighted combination -> base probability
churn_score = (
    0.30 * usage_factor +
    0.25 * contract_factor +
    0.20 * tickets_factor +
    0.15 * renewal_factor +
    0.10 * tenure_factor
)

# Scale to a realistic churn rate range (~15-25% overall)
churn_prob = np.clip(churn_score * 0.5, 0.02, 0.85)

churned = np.random.binomial(1, churn_prob)

# Generate churn_date and churn_reason only for churned customers
today = datetime(2026, 8, 22)
churn_reasons = ["Price Too High", "Poor Service", "Low Usage", "Competitor",
                  "Technical Issues", "Customer Support", "No Longer Needed", "Other"]

churn_dates = []
reasons = []

for i, row in df.iterrows():
    if churned[i] == 1:
        signup = datetime.strptime(row["signup_date"], "%Y-%m-%d")
        max_days = (today - signup).days
        days_after_signup = random.randint(30, max(31, max_days))
        c_date = signup + timedelta(days=days_after_signup)
        churn_dates.append(c_date.strftime("%Y-%m-%d"))

        # Bias reason based on driving factor
        if row["support_tickets"] >= 5:
            reasons.append(random.choice(["Customer Support", "Technical Issues", "Poor Service"]))
        elif row["monthly_usage_hours"] < 15:
            reasons.append(random.choice(["Low Usage", "No Longer Needed"]))
        else:
            reasons.append(random.choice(churn_reasons))
    else:
        churn_dates.append(None)
        reasons.append(None)

churn_df = pd.DataFrame({
    "customer_id": df["customer_id"],
    "churned": churned,
    "churn_date": churn_dates,
    "churn_reason": reasons
})

churn_df.to_csv("data/churn.csv", index=False)
print(churn_df.head(10))
print(f"Total rows: {len(churn_df)}")
print(f"Churn rate: {churn_df['churned'].mean()*100:.2f}%")