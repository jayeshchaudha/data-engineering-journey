# ================================
# Topic    : Python Print & Basic Syntax
# ================================

# Single-line comment — Python ignores everything after the '#' symbol.
# Comments are notes for humans; they don't affect how the code runs.

# print() outputs text to the terminal.
# Text (strings) must be wrapped in matching quotes — either single or double.
print(" Hi Python")
print('Hello Python')

# INVALID example (don't mix quote types):
# print("Hi')   <-- This would throw a SyntaxError

print("-----------")

# Printing ASCII art — each line is its own print() call.
print("           __")
print("          / _)")
print(" _.----._/ /")
print("_/ (  | (  |")
print("/__.-'|_|--|_|")

# ─── Escape Sequences ────────────────────────────────────────────────────────
# A backslash \ tells Python: "the next character has a special meaning."

print("Hi \"Python \"")          # \" prints a literal double-quote inside a double-quoted string
print("Hi 'Python'")             # Single quotes inside double quotes — no escaping needed

print("Path: C:\\Users\\Jayesh") # \\ prints a literal backslash (needed for Windows paths)
print("Message1\n")              # \n inserts a blank new line after the text
print("Message2")

# ─── Variables & Arithmetic ──────────────────────────────────────────────────
# Python can do math directly inside print().
# The + operator adds numbers (or joins/concatenates strings).
x = 10
y = 23
print("Total:", x + y)   # Outputs: Total: 33
