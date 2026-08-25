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