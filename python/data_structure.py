# ================================
# Project  : Data Engineering Learning
# Author   : Jayesh Chaudhari
# Topic    : Data Structures — Lists, Iterators, Lambda, List Comprehension
# ================================
# NOTE: The original file had the entire code wrapped inside ''' ... '''
# which turned all of it into a string — nothing would have run.
# That wrapper has been removed so all code is live.


# ─── Creating Lists ───────────────────────────────────────────────────────────
# A list is an ordered, mutable (changeable) collection.
# It can hold any mix of types — ints, strings, booleans, None, even other lists.

empty = []
print(empty)         # []
print(type(empty))   # <class 'list'>

letters = ['a', 'b', 'c', 'd']
print(letters)
print(type(letters))

number = [1, 2, 3, 4]
print(number)
print(type(number))

# Mixed-type list — Python allows it, though in data work you usually want consistency
mixed = [1, "a", [1, "true"], True, None]
print(mixed)
print(type(mixed))

# list() constructor — alternative way to create an empty list
empty = list()
print(empty)

# list() on a string splits it into individual characters
letters = 'Python'
print(list(letters))   # ['P', 'y', 't', 'h', 'o', 'n']

# list(range(n)) produces a list of integers from 0 to n-1
numbers = list(range(5))
print(numbers)   # [0, 1, 2, 3, 4]

# Nested lists — a list that contains other lists (like a 2D table/matrix)
matrix = [['a', 'b', 'c'],
          ['d', 'e', 'f']]
mixed_matrix = [['a', 'b'],
                [1, 2, 3],
                [True]]
print(matrix)
print(mixed_matrix)


# ─── Accessing & Reading ──────────────────────────────────────────────────────
# Indexing: positive index starts at 0 from the left.
# Negative index starts at -1 from the right.

lst = ['a', 'b', 'c', 'd']
print(lst)
print(lst[0])    # 'a'  — first item
print(lst[-1])   # 'd'  — last item

# Accessing items in a nested (2D) list: matrix[row][column]
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
print(matrix[2])        # ['g', 'h', 'i']  — full third row
print(matrix[-1][-1])   # 'i'              — last row, last column
print(matrix[1][1])     # 'e'              — middle item

# Slicing: list[start:stop] — stop is NOT included
lst = ['a', 'b', 'c', 'd']
print(lst[:2])   # ['a', 'b']  — first 2 items
print(lst[2:])   # ['c', 'd']  — from index 2 to end
print(lst[:])    # ['a', 'b', 'c', 'd']  — full copy

# Slicing a nested list — returns whole rows
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
print(matrix[:2])      # first 2 rows
print(matrix[1:])      # row 1 to end
print(matrix[1][:2])   # row 1, first 2 columns → ['d', 'e']


# ─── Unpacking ────────────────────────────────────────────────────────────────
# Unpacking assigns list items to individual variables in one line.
# The number of variables must exactly match the number of items.

person = ['Maria', 29, 'Data Engineer', 'Spain']
name, age, role, country = person
print(name)    # 'Maria'
print(role)    # 'Data Engineer'

# The * (star) operator captures "the rest" into a list.
# Only ONE star is allowed per unpacking statement.
# FIX: comment "exCT NUMBER" → "EXACT NUMBER" and "varian=ble" → "variable"
person = ['Maria', 29, 'Data Engineer', 'Spain']
name, *details, country = person   # name='Maria', details=[29, 'Data Engineer'], country='Spain'
print(name)
print(details)
print(country)

name, *details = person            # name='Maria', details=[29, 'Data Engineer', 'Spain']
print(name)
print(details)

*details, country = person         # details=['Maria', 29, 'Data Engineer'], country='Spain'
print(details)
print(country)

# Unpacking works on any sequence — strings too
value = 'Hi'
first, *rest = value
print(first)   # 'H'
print(rest)    # ['i']

# Underscore _ is the convention for "I don't need this value"
person = ['Maria', 29, 'Data Engineer', 'Spain']
name, _, role, _ = person   # age and country are discarded
print(name)
print(role)

person = ['Maria', 29, 'Data Engineer', 'Spain']
name, *_ = person           # keep only name, discard everything else
print(name)


# ─── Aggregate Functions ──────────────────────────────────────────────────────
# Python built-ins that summarise a list in one call — very common in data work.

numbers = [1, 5, 5, 2, 4, 3]
print("Max:",    max(numbers))    # 5
print("Min:",    min(numbers))    # 1
print("Sum:",    sum(numbers))    # 20
print("Length:", len(numbers))    # 6

# all() → True only if EVERY item is truthy (non-zero, non-empty, not None, not False)
# 0 and "" and None and False are all "falsy" in Python
print("All:", all(numbers))             # True  — no zeros or falsy values
print("All:", all([1, 0, 2]))           # False — 0 is falsy
print("All:", all(['a', '', 'b']))      # False — empty string is falsy
print("All:", all(['a', 1, 'b']))       # True  — all truthy

# any() → True if AT LEAST ONE item is truthy
print("Any:", any(numbers))             # True
print("Any:", any([1, 0, 2]))           # True  — 1 and 2 are truthy
print("Any:", any(['a', '', 'b']))      # True  — 'a' and 'b' are truthy
print("Any:", any(['a', 1, 'b']))       # True
print("Any:", any([0, 0, 0]))           # False — all falsy

# .count(value) → how many times value appears in the list
print("Count:", numbers.count(5))      # 2

# .index(value) → position of the FIRST occurrence
print("Index:", numbers.index(5))      # 1  (first 5 is at index 1)

# Membership test
print(4 in numbers)        # True
print(8 not in numbers)    # True

# == compares VALUES — two separate lists with same items are equal
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)   # True

# < compares element by element from left to right
list1 = [1, 2, 3]
list2 = [5, 2, 3]
print(list1 < list2)    # True — 1 < 5 at position 0

# 'is' checks if both variables point to the SAME object in memory (not just equal values)
list1 = [1, 2, 3]
list2 = [5, 2, 3]
print(list1 is list2)   # False — different objects in memory


# ─── Changing a List ──────────────────────────────────────────────────────────

# .append(item) — adds one item to the END of the list
letters = ['a', 'b', 'c']
letters.append('x')
letters.append('y')
print(letters)   # ['a', 'b', 'c', 'x', 'y']

# .insert(index, item) — inserts item BEFORE the given index
letters = ['a', 'b', 'c']
letters.insert(0, 'x')   # insert at position 0 (start)
print(letters)            # ['x', 'a', 'b', 'c']

# Same operations work on nested lists
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix.append(['x', 'y', 'z'])      # adds a new row at the end
matrix.insert(0, ['a', 'a', 'a'])   # adds a new row at the start
print(matrix)

# You can also modify a specific inner list
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix[1].append('x')     # adds 'x' to row 1
matrix[0].insert(0, 'z')  # inserts 'z' at the start of row 0
print(matrix)


# ─── Removing from a List ─────────────────────────────────────────────────────

# .clear() — removes ALL items, leaves an empty list
letters = ['a', 'b', 'c']
letters.clear()
print(letters)   # []

# .remove(value) — removes the FIRST occurrence of the value
letters = ['a', 'b', 'a']
letters.remove('a')   # removes first 'a'
letters.remove('a')   # removes second 'a'
print(letters)        # ['b']

# .pop() — removes and RETURNS the last item (no argument = last)
letters = ['a', 'b', 'c']
removed = letters.pop()
print(letters)               # ['a', 'b']
print('Removed Item:', removed)  # 'c'

# .pop(index) — removes and returns the item at the given index
letters = ['a', 'b', 'c']
removed = letters.pop(1)
print(letters)               # ['a', 'c']
print('Removed Item:', removed)  # 'b'

# Removing rows from a nested list
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix.remove(['a', 'b', 'c'])   # removes the matching row by value
matrix.pop()                      # removes the last row
print(matrix)

# Removing items from within a specific inner list
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix[1].remove('e')   # remove 'e' from row 1
matrix[-1].pop(0)       # remove first item from the last row
print(matrix)


# ─── Updating a List ──────────────────────────────────────────────────────────

# Direct index assignment replaces the item at that position
letters = ['a', 'b', 'c']
letters[1] = 'x'
# NOTE: letters = 'z' replaces the whole list variable with a string — not a list update
# That's why print(letters) below outputs 'z', not a list
letters = 'z'
print(letters)   # 'z'  ← the variable now holds a string, not a list

# Updating a row (or cell) in a nested list
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix[-1]    = ['x', 'y', 'z']   # replace entire last row
matrix[0][0]  = '-'               # replace top-left cell
matrix[1][1]  = '-'               # replace centre cell
matrix[2][2]  = '-'               # replace bottom-right cell
print(matrix)


# ─── Sorting ──────────────────────────────────────────────────────────────────

# .sort() — sorts the list IN PLACE (modifies the original, returns None)
letters = ['c', 'a', 'b']
letters.sort()
print(letters)               # ['a', 'b', 'c']
letters.sort(reverse=True)
print(letters)               # ['c', 'b', 'a']

# Nested lists sort by comparing the first element of each inner list
matrix = [
    ['g', 'h', 'i'],
    ['d', 'e', 'f'],
    ['a', 'b', 'c']
]
matrix.sort()
print(matrix)   # sorted by first element: ['a'...], ['d'...], ['g'...]
matrix.sort(reverse=True)
print(matrix)

# sorted() — returns a NEW sorted list, original is unchanged
letters = ['c', 'a', 'b']
new_list = sorted(letters)
print('Original List: ', letters)   # ['c', 'a', 'b']  — unchanged
print("Sorted List: ",   new_list)  # ['a', 'b', 'c']

new_list = sorted(letters, reverse=True)
print('Original List: ', letters)
print("Sorted List: ",   new_list)


# ─── Reversing ────────────────────────────────────────────────────────────────

# .reverse() — reverses the list IN PLACE
letters = ['c', 'a', 'b']
letters.reverse()
print(letters)   # ['b', 'a', 'c']

# reversed() — returns a reverse iterator (wrap in list() to see the values)
# Original list is NOT modified
letters = ['c', 'a', 'b']
new_list = list(reversed(letters))
print('Original List: ', letters)    # ['c', 'a', 'b']
print("Reversed List: ", new_list)   # ['b', 'a', 'c']
# FIX: "reversed List" → "Reversed List" (capitalised for consistency)


# ─── Copying Lists ────────────────────────────────────────────────────────────

# Assignment (=) does NOT copy — both variables point to the SAME list object
letters = ['a', 'b', 'c']
letters_copy = letters
print('Original: ', letters)
print('Copy: ',     letters_copy)

# Any change through either variable affects both
letters = ['a', 'b', 'c']
letters_copy = letters
letters_copy.append('z')
print('Original: ', letters)       # ['a', 'b', 'c', 'z']  ← also changed!
print('Copy: ',     letters_copy)  # ['a', 'b', 'c', 'z']

# .copy() — shallow copy: creates a NEW list object at the top level
# Changes to the copy don't affect the original for flat lists
letters = ['a', 'b', 'c']
letters_copy = letters.copy()
print('Original: ', letters)
print('Copy: ',     letters_copy)

# FIX: "copird" → "copied"
letters = ['a', 'b', 'c']
letters_copy = letters.copy()
letters_copy.append('z')
print('Original: ', letters)       # ['a', 'b', 'c']  — unchanged
print('Copy: ',     letters_copy)  # ['a', 'b', 'c', 'z']

# Shallow copy with nested lists:
# The outer list is copied, but the INNER lists are still shared references.
# Changing inner items affects BOTH original and copy.
matrix = [
    ['a', 'b'],
    ['d', 'e']
]
matrix_copy = matrix.copy()
print('Original: ', matrix)
print('Copy:     ', matrix_copy)

matrix = [
    ['a', 'b'],
    ['d', 'e']
]
matrix_copy = matrix.copy()
matrix.pop()                     # removes last row from original only
matrix_copy[0].append('z')      # modifies inner list — affects BOTH (shared reference)
print('Original: ', matrix)
print('Copy:     ', matrix_copy)


# ─── Deep Copy ────────────────────────────────────────────────────────────────
# copy.deepcopy() creates a fully independent copy — no shared inner references.
# Safe to use when you have nested lists and don't want changes to cross over.

import copy

matrix = [
    ['a', 'b'],
    ['d', 'e']
]
matrix_copy = copy.deepcopy(matrix)
matrix.pop()                    # only affects original
matrix_copy[0].append('z')     # only affects copy
print('Original: ', matrix)
print('Copy:     ', matrix_copy)

# Summary comparison of the three copy strategies
original = [
    ['a', 'b'],
    ['d', 'e']
]

# Assignment — same object, fully shared
copy1 = original
print("Same Object?",   original is copy1, "\n")

# FIX: "Sahllow copy" → "Shallow copy", "Assigment" → "Assignment"
# Shallow copy — new outer list, shared inner lists
copy2 = original.copy()
print("Same Object?",   original is copy2)
print("Shared Lists?",  original[0] is copy2[0], "\n")   # True — inner lists are shared

# Deep copy — fully independent at every level
copy3 = copy.deepcopy(original)
print("Same Object?",   original is copy3)
print("Shared Lists?",  original[0] is copy3[0], "\n")   # False — nothing shared


# ─── Combining Lists ──────────────────────────────────────────────────────────

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

# + concatenates into a new flat list
comb = letters + numbers
print(comb)   # ['a', 'b', 'c', 1, 2, 3]

# * repeats the list n times
comb = letters * 2
print(comb)   # ['a', 'b', 'c', 'a', 'b', 'c']

# Nesting with [] creates a list of lists (NOT flat)
comb = [letters, numbers]
print(comb)   # [['a', 'b', 'c'], [1, 2, 3]]

# .extend(other_list) adds all items from other_list INTO the original (in place)
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)   # ['a', 'b', 'c']      — unchanged
print(numbers)   # [1, 2, 3, 'a', 'b', 'c']  — letters merged in


# ─── zip() ────────────────────────────────────────────────────────────────────
# zip() pairs up items from two or more sequences by position.
# Stops at the shortest sequence — extra items in longer sequences are dropped.

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = list(zip(letters, numbers))
print(comb)   # [('a', 1), ('b', 2), ('c', 3)]

letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]   # 4 is dropped — letters is shorter
comb = list(zip(letters, numbers))
print(comb)   # [('a', 1), ('b', 2), ('c', 3)]

# zip() with 3 sequences — stops at shortest ("Hi" has 2 characters)
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
comb = list(zip(letters, numbers, "Hi"))
print(comb)   # [('a', 1, 'H'), ('b', 2, 'i')]

# Real-world use: joining two related lists into pairs
ids   = [101, 102, 103]
names = ['Ali', 'Sara', 'John']
print(list(zip(ids, names)))   # [(101, 'Ali'), (102, 'Sara'), (103, 'John')]


# ─── Iterators ────────────────────────────────────────────────────────────────

# Building a new list by transforming items with a for loop
letters = ['a', 'b', 'c']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)   # prints the growing list after each append

# enumerate() → pairs each item with its index
# Returns (index, value) tuples
letters = ['a', 'b', 'c']
print(list(enumerate(letters)))           # [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(enumerate(letters, start=1)))  # [(1, 'a'), (2, 'b'), (3, 'c')]

for index, value in enumerate(letters):
    print(index, value)

# reversed() — iterates in reverse without modifying the original
letters = ['a', 'b', 'c']
print(list(reversed(letters)))   # ['c', 'b', 'a']

for l in reversed(letters):
    print(l)

# zip() in a for loop — unpack each tuple into two variables
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
comb = list(zip(letters, numbers))
print(comb)
for l, n in zip(letters, numbers):
    print(l, n)


# ─── map() ────────────────────────────────────────────────────────────────────
# map(function, iterable) applies a function to EVERY item and returns an iterator.
# Wrap in list() to see all results at once.

letters = ['a', 'b', 'c']
print(list(map(str.upper, letters)))   # ['A', 'B', 'C']

numbers = ['1', '2', '3']
print(list(map(int, numbers)))         # [1, 2, 3]  — strings converted to ints

# To chain two transformations (strip then upper), use a lambda or nested map.
# map() only accepts ONE function — you cannot pass a tuple of functions.
# FIX: "calude" → "Claude" in the comment below
names = ['  Maria ', 'John   ', '  Kumar']
# To apply both strip and upper: use a lambda or two map() calls chained:
# list(map(str.upper, map(str.strip, names)))
print(list(map(str.strip, names)))   # strips whitespace only

for n in map(str.strip, names):
    print(n)


# ─── filter() ─────────────────────────────────────────────────────────────────
# filter(function, iterable) keeps only items for which function returns True.
# filter(None, ...) keeps only truthy items (removes False, 0, "", None).

letters = ['a', '', 'b', None, 'c', False]
print(list(filter(None, letters)))    # ['a', 'b', 'c']
print(list(filter(bool, letters)))    # ['a', 'b', 'c']  — identical result

# FIX: missing comma between 'Python' and 43 → SyntaxError in original
# 'Python' and 43 are different types — str.isalpha filters out '123' and 43
items = ['sql', '123', 'Python', '43']
print(list(filter(str.isalpha, items)))   # ['sql', 'Python']

for i in filter(str.isalpha, items):
    print(i)


# ─── Lambda Functions ─────────────────────────────────────────────────────────
# lambda is an anonymous (nameless) function defined in a single line.
# Syntax: lambda arguments: expression
# Use for short, throwaway functions — especially with map() and filter().

# FIX: "multiple" → "multiply" (naming the function after what it does)
multiply = lambda x: x * 2
print(multiply(2))    # 4

add = lambda x, y: x + y
print(add(1, 2))      # 3

# Lambda with 'in' operator — checks membership in a string
check = lambda i: i in "Python"
print(check("y"))   # True


# ─── Lambda + map() ───────────────────────────────────────────────────────────
# Common pattern: transform a list of values with a one-liner lambda

price = ['$12.50', '$9.99', '$100.00']
# Strip the '$' and convert to float in one step
print(list(map(lambda p: float(p.replace('$', '')), price)))
# [12.5, 9.99, 100.0]


# ─── Lambda + filter() ────────────────────────────────────────────────────────

prices = [120, 30, 300, 80]
# Keep only prices >= 100
print(list(filter(lambda p: p >= 100, prices)))   # [120, 300]

students = [['Maria', 85],
            ['Kumar', 90],
            ['Max',   60]]

# Keep only students with score > 70
print(list(filter(lambda row: row[1] > 70, students)))
# [['Maria', 85], ['Kumar', 90]]

# Keep only students whose name starts with 'M'
students = [['Maria', 85],
            ['Kumar', 90],
            ['Max',   60]]
print(list(filter(lambda row: row[0].startswith('M'), students)))
# [['Maria', 85], ['Max', 60]]


# ─── List Comprehension ───────────────────────────────────────────────────────
# A compact way to build a new list: [transform  for item in iterable  if condition]
# Equivalent to a for loop + append, but in one readable line.
# Very common in Python data pipelines.

domains = ['www.google.com',
           'openai.com',
           'localhost',
           'www.DATAWITHBARA.COM']

# With transformation + filter:
# 1. d.lower()           → make everything lowercase
# 2. .replace('www.','') → strip the www. prefix
# 3. if '.' in d         → keep only entries that look like real domains
cleaned = [
    d.lower().replace('www.', '')   # data transformation
    for d in domains                # for loop
    if '.' in d                     # filter (localhost has no dot → excluded)
]
print(cleaned)   # ['google.com', 'openai.com', 'datawithbara.com']

# Without transformation — just filter, keep the variable as-is
domains = ['www.google.com',
           'openai.com',
           'localhost',
           'www.DATAWITHBARA.COM']
cleaned = [
    d                  # keep the item unchanged
    for d in domains
    if '.' in d        # filter only
]
print(cleaned)   # ['www.google.com', 'openai.com', 'www.DATAWITHBARA.COM']