# ================================
# Topic    : Built-in Functions & Methods
# ================================
# Python comes with many built-in tools (functions) ready to use
# without importing anything.
#
# FUNCTION  → called independently:   type(x), len(x)
# METHOD    → called on a variable:   x.upper(), x.bit_length()

text   = "hi"
number = 10

# type() → returns the data type of a variable
print(type(text))    # <class 'str'>
print(type(number))  # <class 'int'>

# len() → returns the number of characters in a string.
# Works on sequences (strings, lists, tuples) — NOT on plain integers.
print(len(text))     # 2  (characters: 'h' and 'i')
# print(len(number)) → would raise: TypeError: object of type 'int' has no len()

# .upper() → string method that returns a new ALL-CAPS version.
# Note: the original variable is NOT changed — strings are immutable in Python.
print(text.upper())        # "HI"

# .bit_length() → integer method that returns the number of bits needed
# to store the number in binary. Useful for understanding memory size.
# 10 in binary = 1010 → needs 4 bits
print(number.bit_length()) # 4
