# ================================
# Topic    : Python Basics — Data Types & String Methods
# ================================

# ─── Strings ──────────────────────────────────────────────────────────────────
# A string is any sequence of characters wrapped in quotes.
name = "Jayesh"
city = "Pune"
print(name, city)   # comma in print() adds a space between items

# ─── Integers & Floats ────────────────────────────────────────────────────────
# int   → whole numbers (no decimal point)
# float → numbers with a decimal point
age    = 25
salary = 75000.50
print(type(age))     # <class 'int'>
print(type(salary))  # <class 'float'>

# ─── Boolean ──────────────────────────────────────────────────────────────────
# bool has exactly two values: True or False (capital first letter).
# Very common for flags, conditions, and data quality checks.
is_active = True
print(type(is_active))  # <class 'bool'>

# ─── None ─────────────────────────────────────────────────────────────────────
# None represents "no value" or "missing data" — equivalent to NULL in SQL.
value = None
print(value)  # None

# ─── Common String Methods ────────────────────────────────────────────────────
# Real-world data often has extra whitespace from forms, CSV files, etc.
name = " Jayesh Madhavrao Chaudhari "

# .strip() → removes whitespace from BOTH the left AND right side.
# This is usually the first step when cleaning dirty data.
print(name.strip())               # "Jayesh Madhavrao Chaudhari"

# Method chaining: call multiple methods in a single line.
# Python reads left to right — .strip() runs first, then .upper() or .lower().
print(name.strip().upper())       # "JAYESH MADHAVRAO CHAUDHARI"
print(name.strip().lower())       # "jayesh madhavrao chaudhari"

# ─── Splitting Strings ────────────────────────────────────────────────────────
# .split(separator) breaks a string into a list of substrings at every separator.
# Very common for parsing emails, file paths, CSV rows, timestamps, etc.
email = "jayesh@company.com"
parts = email.split("@")   # Result: ["jayesh", "company.com"]

print(parts)     # ['jayesh', 'company.com']
print(parts[0])  # "jayesh" — index 0 is the FIRST item (Python uses 0-based indexing)
