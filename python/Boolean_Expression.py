# ================================
# Project  : Data Engineering Learning
# Author   : Jayesh Chaudhari
# Topic    : Boolean Expressions & Logical Operators
# ================================

# ─── bool() — Truthy and Falsy Values ────────────────────────────────────────
# Every value in Python is either "truthy" (behaves like True)
# or "falsy" (behaves like False) when evaluated in a condition.
# bool() lets you explicitly check which one it is.

print(True)    # True
print(False)   # False
print(type(True))  # <class 'bool'>

# TRUTHY — anything with content or a non-zero value
print(bool(123))   # True — non-zero number
print(bool("hi"))  # True — non-empty string

# FALSY — empty, zero, or None
print(bool())      # False — no argument = nothing
print(bool(0))     # False — zero
print(bool(""))    # False — empty string
print(bool(None))  # False — no value

# Rule of thumb for data work:
# Empty string, 0, None → falsy (treat as "missing data")
# Any real value → truthy (treat as "data exists")


# ─── any(), all(), isinstance() ───────────────────────────────────────────────
email    = ""
phone    = "0176-123456"
username = ""

# any([...]) → True if AT LEAST ONE value in the list is truthy
# Useful for: "does the user have at least one contact method?"
print(any([email, phone, username]))   # True — phone has a value

# all([...]) → True only if EVERY value in the list is truthy
# Useful for: "has the user filled in all required fields?"
print(all([email, phone, username]))   # False — email and username are empty

# isinstance(value, type) → checks if a value is of a specific type
# More reliable than type() for validation because it handles inheritance
print(isinstance(123, int))    # True
print(isinstance(True, str))   # False — True is bool, not str

# String methods that return booleans — useful for format validation
print("Hello".endswith("o"))   # True
print("Hello".startswith("o")) # False


# ─── Comparison Operators ─────────────────────────────────────────────────────
# These compare two values and always return True or False.

print(10 == 10)   # True  — equal to
print(10 != 10)   # False — not equal to
print(7 > 3)      # True  — greater than
print(7 >= 3)     # True  — greater than OR equal to
print(3 < 7)      # True  — less than
print(7 <= 7)     # True  — less than OR equal to

# Strings are compared alphabetically (by ASCII value)
print("a" < "b")   # True  — 'a' comes before 'b'
print("a" == "A")  # False — lowercase != uppercase (case sensitive)

# Chained comparisons — Python allows this; other languages often don't.
# Reads naturally: "is 1 less than 4, AND is 4 less than 6?"
print(1 < 4 < 6)          # True

# Real-world example: age range check (instead of writing two separate conditions)
age = 20
print(18 <= age <= 30)    # True — is age between 18 and 30 (inclusive)?


# ─── Logical Operators: and, or, not ──────────────────────────────────────────
# Combine multiple boolean conditions into one result.

# and → True only if BOTH sides are True
print(3 > 1 and 5 < 1)   # False — second condition fails
print(3 > 1 and 5 > 1)   # True  — both conditions pass

# or → True if AT LEAST ONE side is True
print(3 > 1 or 5 < 1)    # True  — first condition passes
print(3 > 1 or 5 > 1)    # True  — both pass (either would be enough)

# Real-world example: trigger alert if either resource is overloaded
cpu_usage    = 70
memory_usage = 95
# NOTE: result is not printed here — add print() to see it
(cpu_usage > 90 or memory_usage > 90)   # True — memory is over 90

# Login validation: both email AND password must be valid to grant access
email    = True
password = False
print(email and password)   # False — password fails, so access denied

# not → flips/inverts the boolean result
print(not 3 > 2)   # False — 3 > 2 is True, not True = False
print(not True)    # False

# Practical use: check if a string is empty (falsy → not falsy = True means it's empty)
name = ""
print(not name)    # True — name IS empty

# Access control logic combining all three operators:
# Allow access if: (logged in OR guest) AND NOT banned
is_logged_in = True
is_guest     = True
is_banned    = True
condition = (is_logged_in or is_guest) and not is_banned
print(condition)   # False — user is banned, so blocked regardless of login status


# ─── Membership Operators: in, not in ────────────────────────────────────────
# Check if a value exists inside a sequence (string, list, tuple, etc.)

print("f" not in "Python")   # True  — 'f' does not appear in "Python"
print(3 in [1, 2, 3])        # True  — 3 is in the list

# Real-world example: domain blocklist check
domain         = "google.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]

print(domain not in banned_domains)   # True — google.com is not banned, allow it


# ─── Identity Operators: is, is not ──────────────────────────────────────────
# == checks if two values are EQUAL (same content)
# is  checks if two variables point to the EXACT SAME object in memory

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)   # True  — same content
print(x is y)   # False — two separate list objects in memory (different addresses)

# Small integers (-5 to 256) are cached by Python, so 'is' returns True for them.
# This is a CPython implementation detail — don't rely on 'is' for value comparison.
x = 10
y = 10
print(x == y)   # True
print(x is y)   # True — Python reuses the cached integer object for small numbers

# Best practice: always use == for value comparison, use 'is' only for None checks
email = None
print(email is not None and email != "")   # False — email is None


# ─── Challenge Solutions ──────────────────────────────────────────────────────

user_name = "Jayesh"
age       = 18

# 1. Name is not empty AND age is at least 18
Criteria1 = user_name != "" and age >= 18

password = "password123"
# 2. Password is at least 8 characters AND contains no spaces
Criteria2 = len(password) >= 8 and (" " not in password)

email = "python@gmail.com"
# 3. Email is not empty, contains '@', and ends with '.com'
Criteria3 = email != "" and "@" in email and email.endswith(".com")

# 4. Username is a string, is not None, and is longer than 5 characters
#    Note: check 'is not None' BEFORE isinstance() — safe order of evaluation
Criteria4 = user_name is not None and isinstance(user_name, str) and len(user_name) > 5

is_user_admin       = True
is_user_moderator   = True
is_user_banned      = True
is_user_verif_email = Criteria3   # reuse the email check result from above

# 5. User is admin or moderator, AND (not banned AND has verified email)
#    is_user_banned = True here, so condition is False — banned user blocked
Criteria5 = (is_user_admin or is_user_moderator) and (not is_user_banned and is_user_verif_email)

print(Criteria1)   # True
print(Criteria2)   # True
print(Criteria3)   # True
print(Criteria4)   # True  (len("Jayesh") = 6 > 5)
print(Criteria5)   # False (user is banned)