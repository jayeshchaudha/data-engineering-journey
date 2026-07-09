import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, SQLAlchemyError

# Configuration
CSV_FILE = "processed_orders.csv"
DB_URI = os.getenv("DATABASE_URL", "postgresql://jayesh:password@localhost:5432/de_projects")
TABLE_NAME = "orders_clean"

try:
    # STEP 1: Read CSV
    if not os.path.exists(CSV_FILE):
        raise FileNotFoundError(f"'{CSV_FILE}' not found in the current folder.")
        
    df = pd.read_csv(CSV_FILE)
    print("CSV loaded ✅")
    print(df)

    # STEP 2: Connect to PostgreSQL
    engine = create_engine(DB_URI)
    
    # Test connection explicitly before proceeding
    with engine.connect() as connection:
        print("\nConnected to PostgreSQL ✅")

    # STEP 3: Load into database
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)
    print(f"Data written to '{TABLE_NAME}' table ✅")

    # STEP 4: Read back entire table
    df_back = pd.read_sql(f"SELECT * FROM {TABLE_NAME}", engine)
    print(f"\nAll rows from {TABLE_NAME}:")
    print(df_back)

    # STEP 5: Filter delivered orders with amount > 2000
    query = f"""
        SELECT * FROM {TABLE_NAME}
        WHERE status = 'delivered'
        AND amount > 2000
    """
    df_filter = pd.read_sql(query, engine)
    print("\nDelivered orders with amount > 2000:")
    print(df_filter)

except FileNotFoundError as err:
    print(f"File Error: {err}")

except OperationalError as err:
    print(f"Database Connection Error: Could not connect to PostgreSQL. \nDetails: {err}")

except SQLAlchemyError as err:
    print(f"Database Error: An error occurred while executing SQL operations. \nDetails: {err}")

except Exception as err:
    print(f"Unexpected error: {err}")