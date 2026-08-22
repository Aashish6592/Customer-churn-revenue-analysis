import pandas as pd
from sqlalchemy import create_engine


DB_PASSWORD = "6592"
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "customer_churn_db"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

tables = {
    "customers": "data/customers.csv",
    "subscriptions": "data/subscriptions.csv",
    "usage": "data/usage.csv",
    "transactions": "data/transactions.csv",
    "churn": "data/churn.csv"
}

for table_name, file_path in tables.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into '{table_name}'")

print("\nAll data loaded successfully!")