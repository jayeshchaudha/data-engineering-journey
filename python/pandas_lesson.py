import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# PANDAS LEARNING FILE
# Based on w3schools + personal practice
# ==========================================


# ==========================================
# 1. SERIES — 1D labeled array
# ==========================================

# A Series is like a single column with an index
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
# Index is auto-assigned: 0, 1, 2

# You can assign your own index labels
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(myvar["y"])   # Access by label

# Dictionary → Series (keys become index)
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

# Only select specific keys from the dict
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)


# ==========================================
# 2. DATAFRAME — 2D table (rows + columns)
# ==========================================

# A DataFrame is a collection of Series (one per column)
# Each dict key becomes a column, each list becomes that column's data

orders = [
    {"order_id": 1, "customer_name": "Rahul Sharma",  "city": "Mumbai", "amount": 4500, "status": "delivered"},
    {"order_id": 2, "customer_name": "Priya",          "city": "Delhi",  "amount": 1200, "status": "pending"},
    {"order_id": 3, "customer_name": "Amit Verma",     "city": "Pune",   "amount": 8900, "status": "delivered"},
    {"order_id": 4, "customer_name": "Sneha",          "city": "Mumbai", "amount": 2300, "status": "cancelled"},
    {"order_id": 5, "customer_name": "Vikas Yadav",    "city": "Pune",   "amount": 5600, "status": "delivered"},
]

df = pd.DataFrame(orders)
print(df)

# Named index — use order_id as row label instead of 0,1,2...
df_indexed = pd.DataFrame(orders)
df_indexed = df_indexed.set_index("order_id")
print(df_indexed)

# Access a named row after set_index
print(df_indexed.loc[3])   # row where order_id = 3


# ==========================================
# 3. EXPLORING A DATAFRAME
# ==========================================

# These are the first things you run on any new dataset
print(df.head())        # first 5 rows (default)
print(df.tail(2))       # last 2 rows
print(df.shape)         # (rows, columns)
print(df.columns)       # column names
print(df.dtypes)        # data type of each column
print(df.info())        # summary: non-null counts, dtypes, memory
print(df.describe())    # stats for numeric columns: mean, std, min, max, quartiles


# ==========================================
# 4. SELECTING DATA
# ==========================================

# Single column → returns a Series
print(df["customer_name"])

# Multiple columns → returns a DataFrame
print(df[["customer_name", "amount"]])

# By position (integer-based) — iloc
print(df.iloc[0])       # first row
print(df.iloc[0:2])     # rows 0 and 1 (end is exclusive)

# By label (index-based) — loc
print(df.loc[0])        # row where index = 0
print(df.loc[3])        # row where index = 3


# ==========================================
# 5. FILTERING ROWS
# ==========================================

# Boolean condition — replaces a for-loop with if statement
# df["status"] == "delivered" returns True/False for each row
# Wrapping df[...] keeps only the True rows

delivered = df[df["status"] == "delivered"]
print(delivered)

# Multiple conditions — use & (AND) or | (OR)
# Each condition must be wrapped in its own ()
high_value_delivered = df[(df["status"] == "delivered") & (df["amount"] > 5000)]
print(high_value_delivered)

mumbai_or_pune = df[(df["city"] == "Mumbai") | (df["city"] == "Pune")]
print(mumbai_or_pune)


# ==========================================
# 6. PANDAS READ CSV
# ==========================================

df = pd.read_csv('data.csv')
print(df.to_string())   # to_string() shows all rows without truncation

df = pd.read_csv('data.csv')
print(df)               # default print — truncates if too many rows

print(pd.options.display.max_rows)      # see current row display limit (default 60)

pd.options.display.max_rows = 9999      # increase limit so all rows print
df = pd.read_csv('data.csv')
print(df)

df = pd.read_csv('data.csv')
print(df.head(10))
print(df.tail())


# ==========================================
# 7. PANDAS READ JSON
# ==========================================

df = pd.read_json('data.json')
print(df.to_string())


# ==========================================
# 8. ANALYZING DATA
# ==========================================

df = pd.read_csv('data.csv')

print(df.head(10))
print(df.head())
print(df.tail())
print(df.info())    # non-null counts + dtypes — tells you where data is missing


# ==========================================
# 9. CLEANING — EMPTY CELLS
# ==========================================

df = pd.read_csv('data.csv')

# Option 1: return new DataFrame with NaN rows removed (original unchanged)
new_df = df.dropna()
print(new_df.to_string())

# Option 2: inplace=True modifies original directly — no new variable needed
df.dropna(inplace=True)
print(df.to_string())

# Option 3: fill ALL NaN with a fixed value
df = pd.read_csv('data.csv')
df.fillna(130, inplace=True)

# Option 4: fill only one specific column
df = pd.read_csv('data.csv')
# TEACHING NOTE: df["Calories"].fillna(130, inplace=True) is "chained assignment" —
# df["Calories"] creates a temporary copy first, then inplace=True modifies THAT copy,
# not the original df. Modern pandas raises a FutureWarning for this, and pandas 3.x
# may not update df at all. The safe, future-proof version is:
#     df["Calories"] = df["Calories"].fillna(130)
# Kept your original line below exactly as written, for reference:
df["Calories"].fillna(130, inplace=True)

# Option 5: fill with mean (average of existing values)
df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace=True)

# Option 6: fill with median (middle value — less affected by outliers than mean)
df = pd.read_csv('data.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace=True)

# Option 7: fill with mode (most frequent value)
df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]    # mode() returns a Series, [0] gets the top value
df["Calories"].fillna(x, inplace=True)


# ==========================================
# 10. CLEANING — WRONG FORMAT (DATES)
# ==========================================

df = pd.read_csv('data.csv')

# Convert string column to proper datetime type
# pandas can parse most common date formats automatically
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())

# Drop rows where date couldn't be parsed (becomes NaT — Not a Time)
df.dropna(subset=['Date'], inplace=True)


# ==========================================
# 11. CLEANING — FIXING WRONG DATA
# ==========================================

df = pd.read_csv('data.csv')

# Fix a single specific cell by row index and column name
df.loc[7, 'Duration'] = 45

# Fix all rows where value is out of expected range — cap at 120
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

# Alternative: delete the row instead of fixing it
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)


# ==========================================
# 12. REMOVING DUPLICATES
# ==========================================

df = pd.read_csv('data.csv')

# duplicated() returns True for rows that are exact copies of a previous row
print(df.duplicated())

df.drop_duplicates(inplace=True)


# ==========================================
# 13. CORRELATIONS
# ==========================================

df = pd.read_csv('data.csv')

# corr() shows how much each numeric column moves with every other column
# Value close to  1.0 → strong positive relationship
# Value close to -1.0 → strong negative relationship
# Value close to  0   → no relationship
print(df.corr(numeric_only=True))


# ==========================================
# 14. PLOTTING
# ==========================================

df = pd.read_csv('data.csv')

# Line plot — all numeric columns over index
df.plot()
plt.show()

# Scatter — does more duration mean more calories burned?
df.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

# Scatter — duration vs max pulse
df.plot(kind='scatter', x='Duration', y='Maxpulse')
plt.show()

# Histogram — distribution of one column
df['Duration'].plot(kind='hist')
plt.show()


# ==========================================
# 15. NEW COLUMN FROM EXISTING
# ==========================================

df = pd.DataFrame(orders)

# Create a new column by doing math on an existing one
# Every row gets calculated automatically — no loop needed
df["tax"] = df["amount"] * 0.18
print(df[["customer_name", "amount", "tax"]])

# Categorize with np.where — like Excel IF formula
# np.where(condition, value_if_true, value_if_false)
df["tier"] = np.where(df["amount"] > 5000, "high", "low")
print(df[["customer_name", "amount", "tier"]])


# ==========================================
# 16. VALUE COUNTS
# ==========================================

df = pd.DataFrame(orders)

# Count how many times each unique value appears in a column
# Most useful for categorical columns (status, city, etc.)
print(df["status"].value_counts())
print(df["city"].value_counts())

# Normalize=True gives percentage instead of count
print(df["status"].value_counts(normalize=True))


# ==========================================
# 17. SORT VALUES
# ==========================================

df = pd.DataFrame(orders)

# Sort by a single column — ascending by default
print(df.sort_values("amount"))

# Sort descending — highest amount first
print(df.sort_values("amount", ascending=False))

# Sort by multiple columns — city first, then amount within each city
print(df.sort_values(["city", "amount"], ascending=[True, False]))


# ==========================================
# 18. GROUPBY
# ==========================================

df = pd.DataFrame(orders)

# groupby splits the DataFrame into groups, then you apply an aggregation
# Think of it as: GROUP BY city → SUM amount (same as SQL)

# Total amount per city
print(df.groupby("city")["amount"].sum())

# Average amount per status
print(df.groupby("status")["amount"].mean())

# Multiple aggregations at once
print(df.groupby("city")["amount"].agg(["sum", "mean", "count"]))

# Group by multiple columns
print(df.groupby(["city", "status"])["amount"].sum())


# ==========================================
# 19. APPLY — run a function on each row/column
# ==========================================

df = pd.DataFrame(orders)

# apply() runs a function on every element in a column
# Lambda is just a one-line function — no need to def a separate function

# Uppercase every customer name
df["customer_name"] = df["customer_name"].apply(lambda x: x.upper())
print(df["customer_name"])

# Custom logic per row — apply on full row with axis=1
# axis=0 (default) = apply function to each column
# axis=1 = apply function to each row
def label_order(row):
    if row["amount"] > 5000 and row["status"] == "delivered":
        return "priority"
    return "normal"

df["label"] = df.apply(label_order, axis=1)
print(df[["customer_name", "amount", "status", "label"]])


# ==========================================
# 20. RENAME AND DROP COLUMNS
# ==========================================

df = pd.DataFrame(orders)

# Rename columns — pass a dict: {old_name: new_name}
df.rename(columns={"customer_name": "name", "amount": "order_value"}, inplace=True)
print(df.columns)

# Drop a column — axis=1 means column (axis=0 means row)
df.drop(columns=["order_value"], inplace=True)
print(df.columns)

# Drop a row by index
df.drop(index=2, inplace=True)
print(df)


# ==========================================
# 21. MERGE — combining two DataFrames (like SQL JOIN)
# ==========================================

# Two separate tables — customers and their orders
customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name":        ["Rahul", "Priya", "Amit", "Sneha"],
    "city":        ["Mumbai", "Delhi", "Pune", "Mumbai"],
})

orders_df = pd.DataFrame({
    "order_id":    [101, 102, 103, 104, 105],
    "customer_id": [1, 2, 2, 3, 5],       # customer_id 5 doesn't exist in customers
    "amount":      [4500, 1200, 800, 8900, 3000],
})

# INNER JOIN — only rows where customer_id exists in BOTH tables
merged = pd.merge(customers, orders_df, on="customer_id", how="inner")
print(merged)

# LEFT JOIN — all rows from left table, NaN where no match in right
merged_left = pd.merge(customers, orders_df, on="customer_id", how="left")
print(merged_left)

# RIGHT JOIN — all rows from right table, NaN where no match in left
# customer_id 5 will appear but name/city will be NaN
merged_right = pd.merge(customers, orders_df, on="customer_id", how="right")
print(merged_right)


# ==========================================
# 22. CONCAT — stacking DataFrames
# ==========================================

# concat stacks DataFrames vertically (add more rows) or horizontally (add more columns)

df1 = pd.DataFrame({
    "name":   ["Rahul", "Priya"],
    "amount": [4500, 1200],
})

df2 = pd.DataFrame({
    "name":   ["Amit", "Sneha"],
    "amount": [8900, 2300],
})

# Stack vertically — same columns, more rows (like UNION in SQL)
combined = pd.concat([df1, df2], ignore_index=True)
# ignore_index=True resets index to 0,1,2... instead of keeping original indexes
print(combined)
# --- End of reference notes block (Sections 1–22 above, now live runnable code) ---


# 1. Raw data with mixed casing, extra spaces, cities, and statuses
data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "customer_name": [
        "  rahul sharma ", 
        "PRIYA PATIL", 
        " aravind swamy", 
        "Neha Gupta  ", 
        "amit MISHRA",
        "SNEHA KULKARNI ", 
        "  vikram singh", 
        "Ananya Rao", 
        "  Rohan Joshi  ", 
        "pooja deshmukh"
    ],
    "city": ["Mumbai", "Pune", "Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi", "Pune", "Mumbai"],
    "amount": [2500, 1200, 4500, 850, 3100, 1750, 999, 5200, 1800, 2900],
    "status": ["delivered", "pending", "delivered", "cancelled", "delivered", "pending", "cancelled", "delivered", "pending", "delivered"]
}

# 2. Create the DataFrame
df = pd.DataFrame(data)


#2. Clean customer_name column (strip + title case) using .str methods
df["customer_name"] = df["customer_name"].str.strip().str.title()
print(df)

# 3. Add a new column "amount_with_tax" = amount * 1.18
df["amount_with_tax"] = df["amount"] * 1.18

# 4. Add a new column "value_category":
#    "High" if amount > 5000, "Medium" if > 2000, else "Low"
def categorize(amount):
    if amount > 5000:
        return "High"
    elif amount > 2000:
        return "Medium"
    else:
        return "Low"
df["value_category"] = df["amount"].apply(categorize)

# 5. Filter and print only delivered orders
# NOTE: df["status"] == "delivered" alone only returns True/False per row (a mask).
# Wrapping it in df[...] is what actually filters the table down to matching rows.
delivered = df[df["status"] == "delivered"]
print(delivered)

# 6. Group by city and print total amount per city
print(df.groupby("city")["amount"].sum())

# 7. Group by status and print count + total amount
# NOTE: original line grouped by "city" here, but the instruction asked for "status".
print(df.groupby("status")["amount"].agg(["count", "sum"]))

# 8. Save the final DataFrame to a CSV file called processed_orders.csv
df.to_csv("processed_orders.csv", index=False)
# Display the DataFrame
print(df)


# ==========================================
# 23. MISSING CONCEPTS — ADDED FOR COMPLETE REFERENCE
# (Not in your original file, but used constantly in real DE work)
# ==========================================

df = pd.DataFrame(orders)

# --- 23.1 PIVOT TABLE ---
# Excel-style cross-tab: rows x columns x aggregated value.
# Compare to groupby: groupby gives you ONE long list of results,
# pivot_table reshapes it into a wide grid — easier to eyeball.
pivot = pd.pivot_table(
    df,
    values="amount",     # what to aggregate
    index="city",        # becomes the rows
    columns="status",    # becomes the columns
    aggfunc="sum",        # how to aggregate (sum, mean, count...)
    fill_value=0          # replace NaN (no data for that combo) with 0
)
print(pivot)

# --- 23.2 MELT ---
# The opposite of pivot — turns WIDE data into LONG data.
# Very common before loading into a database, since DB tables
# usually want one row per (entity, attribute, value) rather than
# one column per attribute.
wide = pd.DataFrame({
    "city": ["Mumbai", "Pune", "Delhi"],
    "jan_sales": [1000, 1500, 1200],
    "feb_sales": [1100, 1300, 1400],
})
long = wide.melt(id_vars="city", var_name="month", value_name="sales")
print(long)
# city melts from 1 row per city into 1 row per (city, month) combo

# --- 23.3 map() vs apply() ---
# map() — works on a single Series (one column), simplest tool for
#         a 1-to-1 value lookup or transform. Cannot see other columns.
status_map = {"delivered": "Done", "pending": "In Progress", "cancelled": "Cancelled"}
df["status_label"] = df["status"].map(status_map)
print(df[["status", "status_label"]])

# apply() — works on a Series OR a whole DataFrame row (axis=1).
#           Use apply when your logic needs more than one column,
#           or needs actual function logic (if/else, calculations).
# (You already used this correctly in Section 19 with label_order)

# --- 23.4 astype() — explicit type conversion ---
# Important before loading into PostgreSQL: column types in pandas
# must match (or cleanly cast to) the target DB column types.
df["order_id"] = df["order_id"].astype(str)   # int -> string
df["amount"] = df["amount"].astype(float)     # int -> float
print(df.dtypes)

# --- 23.5 isin() — filter against a list of values ---
# Cleaner than chaining several == with | for the same column.
target_cities = ["Mumbai", "Pune"]
filtered = df[df["city"].isin(target_cities)]
print(filtered)

# --- 23.6 between() — range filtering ---
mid_range = df[df["amount"].astype(float).between(2000, 6000)]
print(mid_range)

# --- 23.7 nunique() — count of unique values ---
# Quick way to check cardinality of a column (e.g. "how many distinct cities?")
print(df["city"].nunique())     # number of distinct cities
print(df["city"].unique())      # the actual distinct values, as an array