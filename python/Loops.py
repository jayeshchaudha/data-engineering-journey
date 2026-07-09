# ================================
# Project  : Data Engineering Learning
# Author   : Jayesh Chaudhari
# Topic    : Loops — for, break, continue, pass, else, while
# ================================


# ─── for loop basics ──────────────────────────────────────────────────────────
# A for loop iterates over any sequence (tuple, string, list, range, etc.)
# and runs the indented block once for each item.
# The loop variable (i, value, item) takes the value of each item in turn.

for i in (1, 2, 3):
    print(i)

# Iterating over a string — each character is one iteration
values = "Python"
for value in values:
    print(value)

# range(start, stop) generates integers from start up to (but NOT including) stop
for item in range(1, 6):      # 1, 2, 3, 4, 5
    print(item)

# range(start, stop, step) — step controls the increment (here: every 2nd number)
for item in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(item)


# ─── Accumulator pattern ──────────────────────────────────────────────────────
# Start a variable at 0 outside the loop, then add to it on each iteration.
# Very common in data work for running totals, counts, etc.
scores = [50, 60, 80, 55, 75]
total  = 0
for score in scores:
    total = total + score   # same as: total += score
    print(total)            # prints running total after each addition
print(f"Final total: {total}")


# ─── String cleaning inside a loop ────────────────────────────────────────────
# Common ETL pattern: normalise a list of filenames before processing.
# Note: reassigning 'file' inside the loop does NOT change the original list —
# it only changes the local variable for that iteration.
files = [' Report.csv', 'DATA.csv', 'final.TXT  ']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing {file}")


# ─── Multiplication table ──────────────────────────────────────────────────────
# range(1, 11) gives 1 through 10 — the classic times-table range.
tables = 7
for item in range(1, 11):
    print(f"7 X {item} = {7 * item}")


# ─── Left-aligned star pyramid ────────────────────────────────────────────────
# String repetition (*) inside a loop builds rows of increasing length.
# star=1 → "*", star=2 → "**", ..., star=6 → "******"
value = "*"
for star in range(1, 7):
    print(value * star)


# ─── break — exit the loop immediately ───────────────────────────────────────
# break stops the loop the moment a condition is met.
# Items after the break point are never processed.
# Use case: stop scanning the moment bad data is found (fail fast).
names = ["John", "maria", "", "Kumar"]
for name in names:
    if name == "":
        print("Empty value detected!")
        break               # loop stops here — "Kumar" is never reached
    print(f"Name = {name}")


# ─── continue — skip current iteration, go to next ───────────────────────────
# continue skips the rest of the current iteration and moves to the next item.
# Use case: filter out bad records but keep processing the rest.
names = ["John", "maria", "", "Kumar"]
for name in names:
    if name == "":
        print("Empty value detected!")
        continue            # skip the print below, move on to "Kumar"
    print(f"Name = {name}")


# ─── pass — do nothing (placeholder) ─────────────────────────────────────────
# pass is a no-op — Python requires an indented block to have at least one statement.
# Use it as a placeholder while you plan the real logic.
# NOTE: unlike break/continue, pass does NOT affect loop flow —
# execution continues to the print() below it every time.
names = ["John", "maria", "", "Kumar"]
for name in names:
    if name == "":
        print("Empty value detected!")
        pass                # placeholder — loop still continues to print below
    print(f"Name = {name}") # this runs for ALL names including the empty one


# ─── BUG EXAMPLE + FIX ───────────────────────────────────────────────────────
# ORIGINAL CODE (buggy):
#   name = name.replace("", "Unknown")
#
# WHY IT'S WRONG:
#   "".replace("", "Unknown") does NOT produce "Unknown".
#   replace("", x) inserts x between EVERY character + at both ends.
#   Result: "UnknownJUnknownoUnknownhUnknownUnknown" for "John"
#   and "Unknown" for "" — the empty case works by accident, the rest break.
#
# CORRECT FIX: use an explicit equality check instead.
names = ["John", "maria", "", "Kumar"]
for name in names:
    if name == "":
        name = "Unknown"    # direct assignment — clean and unambiguous
    print(f"Name = {name}")


# ─── Skipping weekends with continue ─────────────────────────────────────────
# Membership check (in) combined with continue to filter a list.
days    = ['Mon', 'Sun', 'Wed', 'Tue']
weekend = ['Sat', 'Sun']
for day in days:
    if day in weekend:
        continue            # skip weekend days
    print(f'Workday: {day}')


# ─── SQL injection detection with break ──────────────────────────────────────
# Real-world security pattern: scan inputs for dangerous characters.
# Break immediately on the first threat found — no need to scan further.
emails = [
    'data@gmail.com',
    'baraa@outlook.de',
    'DROP TABLE USERS;',    # SQL injection attempt
    'maria@gmail.com'
]
for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker Attack')
        break               # stop processing — don't touch remaining emails
    print(f'Processing Email: {email}')


# ─── else on a for loop ───────────────────────────────────────────────────────
# The else block runs ONLY if the loop completed WITHOUT hitting a break.
# This is unique to Python — most other languages don't have loop-else.
# Use case: "if we scanned everything and found nothing bad → all clear"

# Example 1: loop completes normally → else runs
items = [1, 3, 4, 7]
for i in items:
    print(i)
else:
    print("Loop is completed")  # always runs here (no break in the loop)

# Example 2: break fires → else is skipped
items = [1, 3, 4, 7]
for i in items:
    if i % 2 == 0:
        print("Even number found", i)
        break               # 4 is even → break fires → else is skipped
else:
    print("All numbers are odd")   # NOT printed because break fired

# Example 3: break fires on None → else is skipped
names = ['Kamara', 'Tuba', None, 'Monika']
for name in names:
    if name is None:
        print("Found missing name")
        break
else:
    print('All names are available')   # skipped — None was found

# Example 4: no break → else confirms all files are CSV
files = ['data1.csv', 'report.pdf', 'reports2.csv']
for file in files:
    if not file.endswith('.csv'):
        print("Different file:", file)
        break
else:
    print("All are csv files")   # skipped — report.pdf triggered the break


# ─── Challenge: Duplicate filename detector ───────────────────────────────────
# Goal: check if any base filename (without extension) appears more than once.
# Approach: use a set as "memory" — sets store only unique values.
# If we try to add a name that's already in the set → it's a duplicate.
#
# Why a set and not a list?
# set lookup (in) is O(1) — instant regardless of size.
# list lookup (in) is O(n) — gets slower as the list grows.
# For large file lists in a pipeline, this difference matters.

file_lists = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',   # duplicate base name "report"
    'data.csv'
]

seen_names      = set()   # empty set — will store base names we've already seen
duplicate_found = False   # flag to track the result outside the loop

for find_list in file_lists:
    file_name = find_list.split(".")[0]   # "report.csv" → ["report", "csv"] → "report"

    if file_name in seen_names:
        # This base name was already added in a previous iteration → duplicate
        duplicate_found = True
        break                        # no need to keep scanning
    else:
        seen_names.add(file_name)    # first time seeing it → remember it

# The flag approach lets us use the result outside the loop cleanly.
if duplicate_found:
    print("Duplicate found")
else:
    print("All files are unique")


# ─── Nested loops ─────────────────────────────────────────────────────────────
# A nested loop has one loop inside another.
# The inner loop completes ALL its iterations for each single iteration of the outer loop.
# Total iterations = outer_count × inner_count × ...

for x in range(3):
    for y in range(2):
        for z in range(2):
            print(f'({x}, {y}, {z})')

# Common use case: generating all combinations (colour + size = SKUs)
colors = ['red', 'blue', 'green']
sizes  = ['L', 'M', 'S']

for color in colors:
    for size in sizes:
        print(f"{color} - Size {size}")

# Generating dated report filenames for a pipeline
# range(1, 29) covers days 1–28 (safe for all months)
years  = [2026, 2027]
months = ['Jan', 'Feb', 'Mar']
days   = range(1, 29)

for y in years:
    for m in months:
        for d in days:
            print(f'reports_{y}_{m}_{d}.csv')

# Generating NULL-check SQL for every table + column combination
# FIX: "SELCT" corrected to "SELECT"
tables  = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']

for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')


# ─── while loop ───────────────────────────────────────────────────────────────
# A while loop keeps running as long as its condition is True.
# Use when you don't know in advance how many iterations are needed.
# Syntax: while <condition>:

# Basic counter — condition becomes False when i reaches 4
i = 0
while i < 4:
    i += 1   # IMPORTANT: always update the variable or the loop runs forever
    print(i)

# Keep asking until the user types "yes"
answer = ""
while answer != "yes":
    answer = input("Do you agree? (yes/no): ")
print("Thank you for accepting 😈")


# ─── while True with break ────────────────────────────────────────────────────
# while True creates an intentional infinite loop.
# The only way out is a break statement inside the loop.
# This is the standard pattern for "keep asking until valid input".

# NOTE: "while True: print(...)" with no break would run forever —
# only use while True when you have a break condition inside.

while True:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        break               # exits the loop — code below the loop runs next
print("Thank You")


# ─── while with attempts counter + else ───────────────────────────────────────
# Combining a counter with while lets you limit the number of tries.
# The else on a while loop works the same as on a for loop:
# it runs ONLY if the loop ended because the condition became False
# (i.e. NOT because of a break).

attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we're on the same page")
        break           # user agreed — exit early, else is skipped
    attempts += 1       # wrong answer — count the attempt and try again
else:
    print("3 strikes. You are out!")   # only prints if all 3 attempts failed
print("Thank You")
