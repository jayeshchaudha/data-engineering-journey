# ================================
# Topic    : User Input
# ================================
# input() pauses the program and waits for the user to type something.
# Whatever the user types is returned as a STRING and stored in the variable.
# The text inside input("...") is the prompt message shown to the user.
#
# IMPORTANT: input() ALWAYS returns a string.
# If you need a number, convert it: age = int(input("Enter age: "))

name = input("Enter Your Name:")

country = "Germany"  # Hardcoded variable (fixed value, not from user)

# The comma in print() automatically inserts a space between each item.
print(name, "comes from", country)
