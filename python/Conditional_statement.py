# ================================
# Project  : Data Engineering Learning
# Author   : Jayesh Chaudhari
# Topic    : Conditional Statements
# ================================

# ─── if ───────────────────────────────────────────────────────────────────────
# The simplest conditional — runs the indented block ONLY if the condition is True.
# If the condition is False, nothing happens (no else).
score = 100
if score >= 90:
    print("A")


# ─── if / else ────────────────────────────────────────────────────────────────
# else is the fallback — runs if the if condition is False.
# Exactly one of the two blocks always runs.
score = 50
if score >= 90:
    print("A")
else:
    print("F")


# ─── if / elif / else ─────────────────────────────────────────────────────────
# elif (else if) lets you check multiple conditions in order.
# Python checks from top to bottom and runs the FIRST block that matches.
# Once a match is found, the rest are skipped — order matters.
score = 85
if score >= 90:
    print("A")
elif score >= 80:    # only checked if score < 90
    print("B")
elif score >= 70:    # only checked if score < 80
    print("C")
else:                # catches everything below 70
    print("F")


# ─── Nested if ────────────────────────────────────────────────────────────────
# An if block inside another if block.
# Use when a second condition only makes sense AFTER the first one passes.
# Keep nesting shallow (max 2–3 levels) — deep nesting gets hard to read.
score             = 90
submitted_project = True

if score >= 90:
    if submitted_project:      # inner check — only reached if score >= 90
        print("A+")
    else:
        print("A")             # good score but no project submitted
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")


# ─── Independent if statements ────────────────────────────────────────────────
# Two completely separate if/else blocks — both are always evaluated.
# Use when the two conditions are unrelated (unlike elif which is one decision).
score             = 50
submitted_project = False

if score >= 90:           # decision 1: score category
    print("High Score")
else:
    print("Low Score")

if submitted_project:     # decision 2: project status (independent of score)
    print("Project is submitted")
else:
    print("Project is not submitted")


# ─── Inline if (Ternary / Conditional Expression) ────────────────────────────
# Compact one-liner for simple if/else assignments.
# Syntax: value_if_true if condition else value_if_false
# Use only for simple cases — complex logic should stay as a full if/elif block.
score = 85

x = "A" if score >= 90 else "F"
print(x)   # "F" — score doesn't reach 90

# Chained ternary — readable if short, but avoid going deeper than 2 levels.
y = "A" if score >= 90 else "B" if score >= 80 else "F"
print(y)   # "B" — score is 85, matches the second condition


# ─── match / case (Python 3.10+) ──────────────────────────────────────────────
# Similar to switch/case in other languages.
# Cleaner than a long if/elif chain when matching a single value against many options.
# The | operator means OR — matches either value.
# case _ is the default (like else) — catches anything not matched above.
country = "IND"
match country:
    case "United States":
        print("US")
    case "India" | "IND":    # matches either "India" or "IND"
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:                   # default — no match found
        print("Unknown Country")


# ─── Challenge 1: Email Validator ────────────────────────────────────────────
# Real data validation logic — this is the kind of check used in ETL pipelines
# before loading data into a database to reject bad records early.

'''
Validate the Quality and Correctness of Email Values
- Must not be empty
- Must contain '.' and '@'
- Must contain exactly one '@' symbol
- Must end with '.com', '.org', or '.net'
- Must not be longer than 254 characters (RFC 5321 standard limit)
- Must start and end with a letter or digit
'''

email = "Python@email.com"

# Always clean before validating — strip() removes invisible leading/trailing spaces
# that would cause valid emails to fail checks silently.
email = email.strip()

# Each elif is only reached if ALL previous conditions passed.
# This is called "guard clause" style — fail fast and give a specific message.

if (email is None) or (email == ""):
    print("Email id is empty")

elif ("." not in email) or ("@" not in email):
    # Both . and @ are required structural characters in any email
    print('Email does not have "." or "@"')

elif email.count("@") != 1:
    # "user@@domain.com" is invalid — exactly one @ required
    print("Email has more than one @ symbol")

elif not email.endswith((".com", ".org", ".net")):
    # endswith() accepts a tuple — checks if it ends with ANY of the values
    print('Email must end with ".com", ".org", or ".net"')

elif len(email) > 254:
    # RFC 5321: maximum email length is 254 characters
    print("Email is longer than 254 characters")

elif not (email[0].isalnum() and email[-1].isalnum()):
    # isalnum() → True if the character is a letter OR digit
    # email[-1] uses negative indexing to get the last character
    print("Email must start and end with a letter or digit")

else:
    # All checks passed — email is structurally valid
    print(email)


# ─── Challenge 2: Password Validator ─────────────────────────────────────────
# Same guard-clause pattern — each check is a specific failure reason.
# In a real system, you'd collect ALL failures at once, but this approach
# is clear and easy to understand as a learning exercise.

'''
Validate the Quality and Correctness of Password
- Must not be empty
- Must be at least 8 characters
- Must include at least 1 uppercase letter
- Must include at least 1 lowercase letter
- Must not be the same as the email
- Must not contain any spaces
- Must start and end with a letter or digit
'''

password = "password"
password = password.strip()

if (password == "") or (password is None):
    print("Password is empty")

elif len(password) < 8:
    print("Password is less than 8 characters")

elif not any(char.isupper() for char in password):
    # any(...) with a generator — loops through every character and checks .isupper()
    # Returns True if AT LEAST ONE character is uppercase
    # "for char in password" is a generator expression (mini loop inside any())
    print("Password must have at least 1 uppercase letter")

elif not any(char.islower() for char in password):
    # Same pattern — checks if at least one lowercase character exists
    print("Password must have at least 1 lowercase letter")

elif email == password:
    # Direct string comparison — password must differ from the email address
    print("Password must be different from email")

elif password.count(" ") > 0:
    # .count(" ") counts how many space characters exist
    # Any spaces in a password is a security and parsing risk
    print("Password must not contain spaces")

elif not (password[0].isalnum() and password[-1].isalnum()):
    # Same boundary check as email — first and last char must be letter or digit
    print("Password must start and end with a letter or digit")

else:
    print("Password is valid")
