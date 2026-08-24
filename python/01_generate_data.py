import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(101)
random.seed(101)

NUM_CUSTOMERS = 15000

cities = ["Delhi", "Mumbai", "Bangalore", "Gurgaon", "Pune", "Hyderabad", 
          "Chennai", "Kolkata", "Noida", "Ahmedabad"]

customer_ids = [f"C{10000+i}" for i in range(1, NUM_CUSTOMERS+1)]

# Age: mostly working-age adults
ages = np.random.normal(35, 10, NUM_CUSTOMERS).astype(int)
ages = np.clip(ages, 18, 70)

genders = np.random.choice(["Male", "Female", "Other"], NUM_CUSTOMERS, p=[0.52, 0.46, 0.02])

city_list = np.random.choice(cities, NUM_CUSTOMERS)

# Signup date: last 3 years
today = datetime(2026, 8, 22)
signup_dates = [today - timedelta(days=random.randint(1, 1095)) for _ in range(NUM_CUSTOMERS)]

tenure_months = [(today - d).days // 30 for d in signup_dates]

customers_df = pd.DataFrame({
    "customer_id": customer_ids,
    "age": ages,
    "gender": genders,
    "city": city_list,
    "signup_date": [d.strftime("%Y-%m-%d") for d in signup_dates],
    "tenure_months": tenure_months
})

customers_df.to_csv("data/customers.csv", index=False)
print(customers_df.head())
print(f"Total rows: {len(customers_df)}")