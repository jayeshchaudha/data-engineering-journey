# ================================
# Topic    : Numeric Data Types & Math Operations
# ================================

# ─── Three Numeric Types ──────────────────────────────────────────────────────
x = 5          # int     → whole number
y = 5.7        # float   → decimal number
z = 2 + 3j     # complex → has a real part (2) and imaginary part (3j)
               #           rarely used in general data work

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# ─── Type Conversion ──────────────────────────────────────────────────────────
# int(), float(), str() convert values between types.
# Very common: data arrives as strings from CSV/APIs and must be cast to numbers.

x = "24"
print(type(x))  # <class 'str'>
x = int(x)      # Convert the string "24" → integer 24
print(type(x))  # <class 'int'>

x = "3.14"
x = float(x)   # Convert the string "3.14" → float 3.14
print(type(x))  # <class 'float'>

# complex(real, imaginary) builds a complex number from two values
x = 3
y = 4
print(complex(x, y))   # (3+4j)

# ─── Math Operators ───────────────────────────────────────────────────────────
x = 5
y = 2

print(x + y)   #  7  → Addition
print(x - y)   #  3  → Subtraction
print(x * y)   # 10  → Multiplication
print(x / y)   #  2.5 → Division (ALWAYS returns a float, even if divisible evenly)
print(x // y)  #  2  → Floor division — divides and rounds DOWN to nearest integer
print(x % y)   #  1  → Modulo — returns the REMAINDER (useful for even/odd checks)
print(x ** y)  # 25  → Exponentiation — x to the power of y (5² = 25)

# Shorthand assignment operators — common in loops and accumulators
x += 2         # Same as: x = x + 2  (also: -=, *=, /=, //=, %=, **=)
print(x)       # 7

# ─── Absolute Value & Rounding ────────────────────────────────────────────────
# abs() → removes the minus sign from negatives (absolute value)
x = 2
y = 10
z = abs(x - y)   # abs(2 - 10) = abs(-8) = 8
print(z)         # 8

import math      # The math module adds advanced math functions

price = 35.54879865

print(round(price))       # 36    → rounds to nearest whole number (standard rounding)
print(math.floor(price))  # 35    → always rounds DOWN  (floor = the ground)
print(math.ceil(price))   # 36    → always rounds UP    (ceil = the ceiling)
print(round(price, 2))    # 35.55 → round to exactly 2 decimal places

# math.trunc() strips the decimal part without rounding (same as int() for positives)
print(math.trunc(price))  # 35

# ─── Random Numbers ───────────────────────────────────────────────────────────
import random

print(random.random())         # Random float between 0.0 and 1.0  (e.g. 0.7312...)
print(random.randint(1, 10))   # Random INTEGER between 1 and 10 (both ends included)

# ─── Validation Methods ───────────────────────────────────────────────────────
# .is_integer() → True if a float has no fractional part (e.g. 7.0), False otherwise
x = 7.0
print(x.is_integer())   # True

y = 7.1
print(y.is_integer())   # False

# isinstance(value, type) → checks if a variable belongs to a specific type.
# More reliable than type() for type-checking in real programs.
x = 70.4
print(isinstance(x, int))    # False — it's a float, not an int
print(isinstance(x, float))  # True

# ─── Challenge ────────────────────────────────────────────────────────────────
# Generate a random integer between 1 and 100.
# Check whether it is even (evenly divisible by 2 → no remainder).
x = random.randint(1, 100)
y = x / 2             # Divide by 2
y = y.is_integer()    # True if result is a whole number → the original was even
print(f"Random number is {x} and Is number even: {y}.")