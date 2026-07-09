# ==========================================
# Topic    : Strings — Types, Methods & Manipulation
# ==========================================

# ─── Checking Types & Conversions ─────────────────────────────────────────────
# type() returns what kind of data a variable holds.
# str() converts a value to a string.

name = "Jayesh"
print(type(name))  # <class 'str'>

age = 24
print(type(age))   # <class 'int'>

# You CANNOT directly join a string and an integer with +.
# str(age) converts the integer to a string first so they can be combined.
print("Your Age is: " + str(age))

# Arithmetic on the original integer, then convert result to string.
age = age + 5   # 24 + 5 = 29  (integer math)
age = str(age)  # convert 29 → "29"
print(type(age))   # <class 'str'>


# ─── Measuring String Length ──────────────────────────────────────────────────
# len() counts every character — letters, digits, spaces, symbols.

password = "123a"
print(len(password))   # 4

# A common real-world validation: enforce minimum password length.
if len(password) < 8:
    print("Your Password is too short!")

# Triple-quoted strings span multiple lines — useful for paragraphs or large text blocks.
text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""
# .count(substring) counts how many times a value appears (CASE SENSITIVE).
print(text.count("Python"))   # 2  (lowercase "python" is NOT counted)


# ─── Transformations ──────────────────────────────────────────────────────────

# 1. replace(old, new) → swaps every occurrence of old with new.
#    Great for standardising data (commas → dots, $ signs, etc.)

price = "1234,56"
print(price.replace(",", "."))   # "1234.56"  (European → standard decimal)

price = "$1,299.99"
# Chain replace() calls — each one processes the result of the previous.
print(price.replace("$", "").replace(".", ""))   # "1,29999"

phone_number = "+49 (176) 123-4567"
# Normalise a phone number by removing all non-digit characters.
print(phone_number.replace("+", "00").replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))

# 2. Concatenation (+) → joins two or more strings together.
first_name = "Michael"
last_name  = "Scott"
full_name  = first_name + " " + last_name   # manually add a space between them
print(full_name)

# 3. f-strings (formatted strings) → modern, readable way to embed variables.
is_student = False

# Old way — requires explicit str() conversion and lots of + operators.
print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + ".")

# Modern way — variables go directly inside {}. No type casting needed.
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")

# f-strings can evaluate expressions directly inside {}.
print(f"2 + 3 = {2 + 3}")   # "2 + 3 = 5"

# To print a literal curly bracket inside an f-string, use double brackets {{ }}.
print(f"{{for escaping curly brackets}}")

# 4. split(separator) → breaks a string into a list at each occurrence of separator.
stamp = "2026-06-04 14:30"
print(stamp.split(" "))   # ['2026-06-04', '14:30']  — split on the space

# 5. String repetition with * → repeats the string N times.
print("=" * 30)    # prints 30 equal signs (useful for visual dividers)
print("ha" * 3)    # "hahaha"
print("=" * 30)


# ─── Indexing & Slicing ───────────────────────────────────────────────────────
# Strings are sequences — each character has a numbered position (index).
# Positive index: starts at 0 from the LEFT.
# Negative index: starts at -1 from the RIGHT.

text = "Python"
#        P  y  t  h  o  n
# Index: 0  1  2  3  4  5
#       -6 -5 -4 -3 -2 -1

print(text[0])    # "P"  → first character (positive index)
print(text[-6])   # "P"  → same character using negative index
print(text[5])    # "n"  → last character (positive)
print(text[-1])   # "n"  → last character (negative) — most common way
print(text[3])    # "h"  → character at position 3

# Slicing syntax: string[start:end]
# start is INCLUDED, end is EXCLUDED.
date = "2026-06-04"

# Extract the year (characters 0, 1, 2, 3)
print(date[0:4])   # "2026"
print(date[:4])    # "2026" — 0 is the default start, so [:4] is the same

# Extract the month
print(date[5:7])   # "06"

# Extract the day — no end boundary means "go to the end of the string"
print(date[8:])    # "04"
print(date[-2:])   # "04" — using a negative start index


# ─── Cleaning Data: Whitespace ────────────────────────────────────────────────
# Dirty data from forms or databases often has stray spaces.

text = " Engineering"
print(text.lstrip())   # "Engineering"  — removes spaces from the LEFT only

text = "Engineering "
print(text.rstrip())   # "Engineering"  — removes spaces from the RIGHT only

text = " Engineering "
print(text.strip())    # "Engineering"  — removes spaces from BOTH sides

text = "  Data Engineering  "
print(text.strip())    # "Data Engineering" — middle spaces are NOT removed

# strip() can also remove specific characters (not just whitespace).
text = "####ABC###"
print(text.strip("#"))   # "ABC"


# ─── Data Quality Check ───────────────────────────────────────────────────────
text = "   Engineering"

print(len(text))          # 14  (includes the 3 leading spaces)
print(len(text.strip()))  # 11  (without the spaces)

# Calculate the exact number of unwanted leading/trailing spaces.
no_of_spaces = len(text) - len(text.strip())
print(no_of_spaces)   # 3


# ─── Challenge: Cleaning a Messy String ───────────────────────────────────────
string = "968-Maria, ( D@t@ Engineer ) ;; 27y  "
# Target output: name: maria | role: data engineer | age: 27

# Step 1 & 2: Slice out the name and convert to lowercase.
name = string[4:9].lower()         # "maria"

# Step 3: Slice out the role, fix the @ typo, and lowercase.
role = string[13:26].replace("@", "a").lower()   # "data engineer"

# Step 4: Slice the age using negative indexing (2nd and 3rd from the end).
age = string[-5:-3]   # "27"

# Step 5: Build the final output using an f-string.
print(f"name: {name} | role: {role} | age: {age}")


# ─── Searching in Strings ─────────────────────────────────────────────────────

# .startswith() → True if the string begins with the given substring
phone = "+91-94217-18267"
print(phone.startswith("+91"))     # True — Indian number prefix check

# .endswith() → True if the string ends with the given substring
email = "chaudharij1503@gmai.com"
print(email.endswith("gmail.com")) # False — note the typo: "gmai.com" not "gmail.com"

# in operator → True if the substring exists anywhere in the string
print("@" in email)   # True

url = "https://api.company.com/v1/data"
print("/api" in url)  # True — useful for URL routing checks

# .find(substring) → returns the INDEX of the first occurrence.
# Returns -1 if not found (unlike .index() which raises an error).
# Adding +1 moves past the found character to start reading AFTER it.
phone1 = "+91-94217-18267"
phone2 = "91-94052-76764"
phone3 = "0091-94052-76764"

find1 = phone1.find("-") + 1   # position after the first dash
find2 = phone2.find("-") + 1
find3 = phone3.find("-") + 1

# Slice from that position onwards to extract just the local number
print(phone1[find1:])   # "94217-18267"
print(phone2[find2:])   # "94052-76764"
print(phone3[find3:])   # "94052-76764"


# ─── Validation ───────────────────────────────────────────────────────────────

# .isalpha() → True if ALL characters are letters (no digits, spaces, or symbols)
country = "India"
print(country.isalpha())   # True

# .isnumeric() → True if ALL characters are digits.
# Does NOT accept decimals, dashes, or spaces — so phone numbers fail.
phone = "3.19"
print(phone.isnumeric())   # False — the dot makes it fail
