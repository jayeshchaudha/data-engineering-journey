import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://jayesh:password@localhost:5432/de_projects")

df = pd.DataFrame({
    "order_id": [101, 102, 103],
    "customer_name": ["Rahul Sharma", "Priya Patil", "Amit Verma"],
    "amount": [4500, 1200, 8900],
})

# Write DataFrame to a new table
df.to_sql(
    "orders",          # table name
    engine,             # connection
    if_exists="replace",  # replace / append / fail
    index=False          # don't write pandas' index as a column
)

print("Loaded into PostgreSQL ✅")

# Read an entire table
df_back = pd.read_sql("SELECT * FROM orders", engine)
print(df_back)

# Read with a query — filter at the database level (faster than pandas filtering)
df_filtered = pd.read_sql("SELECT * FROM orders WHERE amount > 2000", engine)
print(df_filtered)