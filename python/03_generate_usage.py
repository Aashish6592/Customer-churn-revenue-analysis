import pandas as pd
import numpy as np

np.random.seed(303)

customers_df = pd.read_csv("data/customers.csv")
n = len(customers_df)

# Hidden engagement score - drives everything else
engagement_score = np.random.beta(2, 2, n)  # values mostly between 0-1, bell-shaped

# Usage hours: scales with engagement (0 to ~80 hours/month)
monthly_usage_hours = np.round(engagement_score * 80 + np.random.normal(0, 5, n), 1)
monthly_usage_hours = np.clip(monthly_usage_hours, 0, 100)

# Login frequency: scales with engagement (0 to ~30 logins/month)
login_frequency = np.round(engagement_score * 30 + np.random.normal(0, 3, n)).astype(int)
login_frequency = np.clip(login_frequency, 0, 40)

# Support tickets: inverse of engagement (low engagement -> more tickets)
support_tickets = np.round((1 - engagement_score) * 5 + np.random.poisson(0.5, n)).astype(int)
support_tickets = np.clip(support_tickets, 0, 15)

# Complaints: correlated with support tickets, but not always
complaints = [
    max(0, t - np.random.randint(0, 3)) for t in support_tickets
]

usage_df = pd.DataFrame({
    "customer_id": customers_df["customer_id"],
    "monthly_usage_hours": monthly_usage_hours,
    "login_frequency": login_frequency,
    "support_tickets": support_tickets,
    "complaints": complaints
})

usage_df.to_csv("data/usage.csv", index=False)
print(usage_df.head())
print(f"Total rows: {len(usage_df)}")