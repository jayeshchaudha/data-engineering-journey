# ================================
# Project  : Data Engineering Learning
# Author   : Jayesh Chaudhari
# Date     : 28-05-2026
# Topic    : Variables
# ================================

# Without variables, we have to repeat the name everywhere.
# If the name changes, we'd need to update every single line manually.
print("My name is Jayesh")
print("Jayesh is learning Python")
print("Jayesh wants to become Data Engineer")

# A variable stores a value under a label so we only define it once.
# Syntax: variable_name = value
name = "Jayesh"

# Now we use the variable — change it in one place, it updates everywhere.
print("My name is", name)
print(name, "is learning Python")
print(name, "wants to become Data Engineer")

# Variables can be reassigned — Python runs code line by line (top to bottom).
# Everything AFTER this line will use the new value "Maria".
name = "Maria"

print("My name is", name)
print(name, "is learning Python")
print(name, "wants to become Data Engineer")

# We can use multiple variables together in one print statement.
name = "Maria"
language = "Python"
print("My name is", name)
print(name, "is learning", language)
print(name, "wants to become Data Engineer")

# ─── Variable Challenge ──────────────────────────────────────────────────────
# Using variables to build consistent email/URL strings.
# If the channel name ever changes, only ONE line needs updating.
channel_name = "datawithbaraa"
domain = "com"

# f-strings (formatted strings) let us embed variables directly inside text.
# Syntax: f"some text {variable_name} more text"
print(f"info@{channel_name}.{domain}")
print(f"support@{channel_name}.{domain}")
print(f"www.{channel_name}.{domain}")
