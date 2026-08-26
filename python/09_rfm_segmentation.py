import pandas as pd

customers_df = pd.read_csv("data/customers.csv")
subscriptions_df = pd.read_csv("data/subscriptions.csv")
usage_df = pd.read_csv("data/usage.csv")
churn_df = pd.read_csv("data/churn.csv")

# Merge all data, focus on active customers for segmentation
df = customers_df.merge(subscriptions_df, on="customer_id").merge(usage_df, on="customer_id").merge(churn_df, on="customer_id")
active_df = df[df["churned"] == 0].copy()

# Recency proxy: tenure_months (longer tenure = more established relationship)
# Frequency: login_frequency
# Monetary: monthly_charges

# Score each dimension into quintiles (1-5, 5 = best)
active_df["R_score"] = pd.qcut(active_df["tenure_months"], 5, labels=[1,2,3,4,5], duplicates="drop")
active_df["F_score"] = pd.qcut(active_df["login_frequency"], 5, labels=[1,2,3,4,5], duplicates="drop")
active_df["M_score"] = pd.qcut(active_df["monthly_charges"], 5, labels=[1,2,3,4,5], duplicates="drop")

active_df["RFM_score"] = (
    active_df["R_score"].astype(int) +
    active_df["F_score"].astype(int) +
    active_df["M_score"].astype(int)
)

# Segment based on total RFM score (max 15, min 3)
def assign_segment(score):
    if score >= 13:
        return "High Value"
    elif score >= 10:
        return "Loyal"
    elif score >= 7:
        return "Potential Loyal"
    elif score >= 5:
        return "At Risk"
    else:
        return "Low Engagement"

active_df["customer_segment"] = active_df["RFM_score"].apply(assign_segment)

# Save segmented data
output_cols = ["customer_id", "tenure_months", "login_frequency", "monthly_charges",
               "R_score", "F_score", "M_score", "RFM_score", "customer_segment"]
active_df[output_cols].to_csv("data/customer_segments.csv", index=False)

print(active_df["customer_segment"].value_counts())
print("\nSegmentation saved to data/customer_segments.csv")