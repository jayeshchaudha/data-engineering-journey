# ================================
# Topic    : Data Types
# ================================
# Python automatically detects the data type based on how you write the value.
# This is called "dynamic typing" — you don't declare types manually.

a = 10      # int      → whole number
b = 3.15    # float    → decimal number
c = "Hello" # str      → text in double quotes
d = 'Hi'    # str      → text in single quotes (same as double quotes)
e = "1234"  # str      → looks like a number but it's TEXT because of the quotes
f = True    # bool     → boolean — only two values: True or False
g = False   # bool
h = None    # NoneType → represents "no value" / missing data (like NULL in SQL)
i = ""      # str      → empty string (still a string, just has no characters)
j = " "     # str      → a string with one space character (not truly empty)

'''
Challenge:
Create 5 variables - each with a different data type:
 1. Your age
 2. Your height (with decimals)
 3. Your name
 4. Are you a student?
 5. Something with no value yet
Then print the values, data types, and lengths of all variables.
'''

# ─── 5 Variables ─────────────────────────────────────────────────────────────
age            = 30
height         = 5.5
name           = "Jayesh"
student_status = False   # Not currently a student
Job_status     = None    # Not assigned yet

# ─── Print Values ─────────────────────────────────────────────────────────────
print("--- Values ---")
print(age)
print(height)
print(name)
print(student_status)
print(Job_status)

# ─── Print Data Types ─────────────────────────────────────────────────────────
# type() returns the class/type of a variable, e.g. <class 'int'>
print("\n--- Data Types ---")
print(type(age))
print(type(height))
print(type(name))
print(type(student_status))
print(type(Job_status))

# ─── Print Lengths ────────────────────────────────────────────────────────────
print("\n--- Lengths ---")

# Integers don't have a len() — but .bit_length() tells us
# how many binary bits are needed to represent the number.
# e.g. 30 in binary is 11110 → 5 bits
print(age.bit_length())   # 5

# len() works on strings — counts every character including spaces.
print(len(name))          # 6

# NOTE: len(age) raises TypeError because integers have no length.
# print(len(age))         # ← intentionally commented out
