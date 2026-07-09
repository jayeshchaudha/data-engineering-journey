# ================================
# Project  : Data Engineering Learning
# Author   : Jayesh Chaudhari
# Topic    : Data Structure Behaviour — list, tuple, set, dict
# ================================


# ─── List ─────────────────────────────────────────────────────────────────────
# Lists are ORDERED (items keep the position you put them in),
# MUTABLE (can be changed after creation), and allow DUPLICATES.

# Ordered — the printed order always matches the order you wrote the items in.
# It does NOT change unless you explicitly modify the list.
my_list = [10, 30, 20]
print(my_list)   # [10, 30, 20]

# Duplicates are allowed
my_list = [10, 30, 20, 10]

# Index — access an item by its position (0-based)
print(my_list[1])   # 30

# Mutable — you can change an item in place using its index.
# BUG FIX: original code had my_list[3] = 40, but my_list only has indexes 0–3
# (4 items: 10, 30, 20, 10) — wait, it actually DOES have index 3 here
# because my_list was reassigned above to [10, 30, 20, 10] (4 items).
# If my_list only had 3 items, my_list[3] would raise IndexError.
my_list[3] = 40
print(my_list)   # [10, 30, 20, 40] — Lists are mutable


# ─── Tuple ────────────────────────────────────────────────────────────────────
# Tuples are ORDERED, IMMUTABLE (cannot be changed after creation),
# and allow DUPLICATES.

my_tuple = (10, 30, 20)
print(my_tuple)   # (10, 30, 20) — Ordered

my_tuple = (10, 30, 20, 30)
print(my_tuple)          # duplicates allowed
print(my_tuple[1])        # 30 — indexed access works just like lists

# Tuple is NOT mutable — there is no .pop(), .append(), or item assignment
# my_tuple.pop()          # would raise: AttributeError

# sorted() works on tuples too, but ALWAYS returns a LIST (not a tuple).
# This does NOT make the tuple itself mutable — it's a new object.
print(sorted(my_tuple))   # [10, 20, 30, 30]  ← this is a list, my_tuple is unchanged


# ─── Set ──────────────────────────────────────────────────────────────────────
# Sets are UNORDERED, MUTABLE, and store only UNIQUE values (no duplicates).

my_set = {10, 30, 20}
print(my_set)   # unordered — printed order may not match insertion order

my_set = {10, 30, 20, 30}
print(my_set)   # {10, 20, 30} — duplicate 30 is automatically removed (Unique)

# Index — sets do NOT support indexing.
# Values are stored using a hash table, not in sequential positions.
# print(my_set[1])   # would raise: TypeError: 'set' object is not subscriptable

# Mutable — items can be added/removed after creation
my_set.remove(20)
print(my_set)   # 20 removed — sets ARE mutable


# ─── Set Methods ──────────────────────────────────────────────────────────────

a = {10, 20, 30, 40}
a.add(10)   # 10 already exists — set stays unchanged (uniqueness enforced)
a.add(50)   # 50 is new — gets added at a hash-determined position (order looks random)
print(a)

a.update([1, 2])   # .update() adds multiple items from any iterable (list here)
a.update({1, 2})   # works with another set too — duplicates ignored
a |= {1, 2}        # |= is the in-place union operator — same effect as .update()
print(a)

# .remove(value) — removes the value; raises KeyError if value is NOT in the set
a.remove(10)

# .discard(value) — removes the value if present; does NOT error if missing
# This is the SAFER choice when you're not sure the value exists
a.discard(10)

# .pop() — removes and returns a RANDOM item (sets have no defined order)
# a.pop()


# ─── Set Math (Mathematical Set Operations) ───────────────────────────────────
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

# union() / | → all unique items from both sets combined
print(a.union(b))   # {10, 20, 30, 40, 50, 60}
print(a | b)        # same result, operator syntax

# intersection() / & → items present in BOTH sets
print(a.intersection(b))   # {30, 40}
print(a & b)

# difference() / - → items in 'a' but NOT in 'b' (order matters!)
print(a.difference(b))   # {10, 20}
print(a - b)             # {10, 20}
print(b - a)             # {50, 60} — reversed gives the opposite result

# symmetric_difference() / ^ → items in EITHER set but NOT in both (excludes overlap)
print(a.symmetric_difference(b))   # {10, 20, 50, 60}
print(a ^ b)


# ─── Set Relationship Methods ─────────────────────────────────────────────────
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

# issubset() → True if EVERY item in 'a' is also in 'b'
print(a.issubset(b))   # False — 10 and 20 are not in b

a = {30, 40}
b = {30, 40, 50, 60}

print(a.issubset(b))     # True — both 30 and 40 are in b
print(b.issuperset(a))   # True — b contains everything in a (opposite relationship)

# isdisjoint() → True if the two sets have NO items in common
print(a.isdisjoint(b))   # False — they share 30 and 40

a = {100, 20}
b = {30, 40, 50, 60}
print(a.isdisjoint(b))   # True — no overlap between {100, 20} and {30,40,50,60}


# ─── Dictionary ───────────────────────────────────────────────────────────────
# Dictionaries store key:value pairs. Keys must be UNIQUE; values can repeat.
# Since Python 3.7, dicts preserve INSERTION ORDER.

my_dict = {
    'a': 10,
    'b': 20,
    'c': 30
}
print(my_dict)   # ordered by insertion: {'a': 10, 'b': 20, 'c': 30}

# Duplicate keys — the LAST value for a repeated key wins, earlier ones are discarded
my_dict = {
    'a': 10,
    'b': 20,
    'a': 30   # overwrites the earlier 'a': 10
}
print(my_dict)   # {'a': 30, 'b': 20} — key is unique, last value kept

# Values CAN be duplicated — only keys must be unique
my_dict = {
    'a': 10,
    'b': 20,
    'c': 20
}
print(my_dict)   # values 20 appear twice — that's allowed

# Indexing — dicts are accessed by KEY, not by numeric position
# print(my_dict[1])   # would raise KeyError (1 is not a key here)
print(my_dict['b'])   # 20

# Mutable — add a new key or update an existing one using []
my_dict['c'] = 80
print(my_dict)   # {'a': 10, 'b': 20, 'c': 80}


# ─── Common Dict Operations ───────────────────────────────────────────────────
user = {
    'id': 1,
    'age': 30,
    'city': 'berlin'
}

# Accessing a missing key directly raises KeyError:
# print(user["name"])   # would raise KeyError: 'name'

# .get(key, default) → returns default instead of erroring if key is missing
print(user.get("name", "Unknown"))   # "Unknown" — key doesn't exist, default returned

# Membership checks — 'in' checks KEYS by default (not values)
print('age' in user)        # True
print('name' not in user)   # True — 'name' is not a key

# View objects — live views of the dict's keys/values/pairs
print(user.keys())     # dict_keys(['id', 'age', 'city'])
print(user.values())   # dict_values([1, 30, 'berlin'])
print(user.items())    # dict_items([('id', 1), ('age', 30), ('city', 'berlin')])

# Looping over a dict directly iterates over its KEYS
for u in user:
    print(u, user[u])   # key, then look up the value manually

# .items() unpacks both key and value directly — preferred for clarity
for key, value in user.items():
    print(key, value)


# ─── Add, Remove, Update ───────────────────────────────────────────────────────
user['name'] = 'John'   # adds a new key 'name' (didn't exist before)
user['age']  = 35        # updates the existing 'age' key

# .update(dict) → merges another dict in, overwriting matching keys
# FIX: " city" (with a leading space) was a DIFFERENT key from "city" —
# dict keys are exact strings, so " city" would create an EXTRA key
# instead of updating the existing "city". Corrected to "city".
user.update({"age": 35, "city": "Paris"})
print(user)

# .pop(key) → removes the key and RETURNS its value
age = user.pop("age")
print(user)
# FIX: "rRemoved Item" → "Removed Item" (typo — extra leading 'r')
print("Removed Item:", age)

# .pop(key, default) → returns default instead of erroring if key is missing
salary = user.pop("salary", "Not found")
print(user)
print("Removed Item:", salary)   # "Not found" — 'salary' was never a key

# .popitem() → removes and returns the LAST inserted key-value pair
user.popitem()
print(user)


# ─── Creation with fromkeys() ──────────────────────────────────────────────────
# dict.fromkeys(iterable, default_value) creates a new dict
# with each item from the iterable as a key, all set to the same default value.
user = dict.fromkeys({"id", "name", "age", "city"}, None)
print(user)   # {'id': None, 'name': None, 'age': None, 'city': None} (order may vary — built from a set)


# ─── Real-world example ────────────────────────────────────────────────────────
row = {
    "id": 101,
    "name": "John",
    "country": "DE",
    "age": 29,
    "status": "active"
}


# ─── Challenge: Keep Only String Values & Convert Them to UPPERCASE ────────────
# Dict comprehension: {key_expr: value_expr for item in iterable if condition}
user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}

user_str = {
    k: v.upper()                  # transformation — uppercase the string value
    for k, v in user.items()      # loop over key-value pairs
    if isinstance(v, str)         # filter — keep only string values (skip ints)
}
print(user_str)   # {'name': 'JOHN', 'city': 'BERLIN'}