import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
customers_df = pd.read_csv("data/customers.csv")
subscriptions_df = pd.read_csv("data/subscriptions.csv")
usage_df = pd.read_csv("data/usage.csv")
churn_df = pd.read_csv("data/churn.csv")

sns.set_style("whitegrid")

# 1. Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(customers_df["age"], bins=20, kde=True, color="steelblue")
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("screenshots/age_distribution.png")
plt.close()

# 2. Gender Distribution
plt.figure(figsize=(6,5))
customers_df["gender"].value_counts().plot(kind="bar", color="coral")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("screenshots/gender_distribution.png")
plt.close()

# 3. City Distribution
plt.figure(figsize=(10,5))
customers_df["city"].value_counts().plot(kind="bar", color="seagreen")
plt.title("Customer Distribution by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("screenshots/city_distribution.png")
plt.close()

# 4. Plan Distribution
plt.figure(figsize=(6,5))
subscriptions_df["plan"].value_counts().plot(kind="bar", color="mediumpurple")
plt.title("Subscription Plan Distribution")
plt.xlabel("Plan")
plt.ylabel("Count")
plt.savefig("screenshots/plan_distribution.png")
plt.close()

print("Charts saved to screenshots/ folder!")
print("\nAge summary:\n", customers_df["age"].describe())
print("\nGender counts:\n", customers_df["gender"].value_counts())
print("\nCity counts:\n", customers_df["city"].value_counts())
print("\nPlan counts:\n", subscriptions_df["plan"].value_counts())

# Merge data for churn analysis
df = customers_df.merge(subscriptions_df, on="customer_id").merge(usage_df, on="customer_id").merge(churn_df, on="customer_id")

# 5. Churn by Plan
plt.figure(figsize=(7,5))
churn_by_plan = df.groupby("plan")["churned"].mean() * 100
churn_by_plan.plot(kind="bar", color="tomato")
plt.title("Churn Rate by Plan (%)")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Plan")
plt.tight_layout()
plt.savefig("screenshots/churn_by_plan.png")
plt.close()

# 6. Churn by Contract Type
plt.figure(figsize=(6,5))
churn_by_contract = df.groupby("contract_type")["churned"].mean() * 100
churn_by_contract.plot(kind="bar", color="darkorange")
plt.title("Churn Rate by Contract Type (%)")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Contract Type")
plt.tight_layout()
plt.savefig("screenshots/churn_by_contract.png")
plt.close()

# 7. Churn by Payment Method
plt.figure(figsize=(8,5))
churn_by_payment = df.groupby("payment_method")["churned"].mean() * 100
churn_by_payment.sort_values(ascending=False).plot(kind="bar", color="crimson")
plt.title("Churn Rate by Payment Method (%)")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Payment Method")
plt.tight_layout()
plt.savefig("screenshots/churn_by_payment.png")
plt.close()

# 8. Monthly Charges vs Churn (Box Plot)
plt.figure(figsize=(7,5))
sns.boxplot(data=df, x="churned", y="monthly_charges", palette=["seagreen", "tomato"])
plt.title("Monthly Charges vs Churn")
plt.xlabel("Churned (0=No, 1=Yes)")
plt.ylabel("Monthly Charges")
plt.savefig("screenshots/charges_vs_churn.png")
plt.close()

# 9. Usage Hours vs Churn (Box Plot)
plt.figure(figsize=(7,5))
sns.boxplot(data=df, x="churned", y="monthly_usage_hours", palette=["seagreen", "tomato"])
plt.title("Usage Hours vs Churn")
plt.xlabel("Churned (0=No, 1=Yes)")
plt.ylabel("Monthly Usage Hours")
plt.savefig("screenshots/usage_vs_churn.png")
plt.close()

print("\nChurn visualization charts saved!")