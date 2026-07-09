# ================================
# Project  : Data Engineering Learning
# Author   : Jayesh Chaudhari
# Topic    : Functions — definitions, arguments, return values
# ================================


# ─── User-Defined Function (no inputs/outputs) ────────────────────────────────
# def starts a function definition. The indented block is the function body.
# Code inside only runs when the function is CALLED (by writing its name + ()).

def make_coffee():
    print("Start Machine")
    print("Make Coffee")
    print("Add Milk")
    print("Enjoy it")

print("Wake Up")
make_coffee()
print("Working for a while")
make_coffee()


# ─── Built-in Function ─────────────────────────────────────────────────────────
# len() is provided by Python itself — no import needed.
print(len("Python"))


# ─── Function From a Library (Import then call) ───────────────────────────────
# Library functions need: 1) import the module, 2) call as module.function()
import math
number = 4.2
print(math.ceil(number))   # rounds up to nearest whole number


# ─── User-Defined Function — basic ────────────────────────────────────────────
def greet():
    print("Hello")

greet()


# ─── Function with a Parameter ─────────────────────────────────────────────────
def clean_name(name):
    print(name.strip().lower())

clean_name("  MariA  ")
clean_name("KUMAR ")


# ─── Global vs Local Variables ─────────────────────────────────────────────────
# A variable defined OUTSIDE any function is GLOBAL — readable from inside functions.
# A variable defined INSIDE a function is LOCAL — only exists during that call.

case_rule = "lower"   # Global variable

def clean_name(name):           # name = Parameter
    cleaned = name.strip()      # Local variable
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print("Raw :", name)
    print("Cleaned :", cleaned)

clean_name("  MariA  ")
clean_name("KUMAR ")


# ─── Multiple Parameters (Positional Arguments) ────────────────────────────────
def clean_name(first_name, last_name, country):
    first = first_name.strip().lower()
    last  = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)

# Positional arguments — matched to parameters by ORDER
clean_name(" mAriA ", "SMITH", "DE")

# Keyword arguments — matched by NAME, order doesn't matter
clean_name(country="DE", first_name=" mAriA ", last_name="SMITH")


# ─── Mixed Arguments ────────────────────────────────────────────────────────────
# Positional arguments must come BEFORE keyword arguments.
clean_name(" mAriA ", last_name="SMITH", country="DE")


# ─── Default Parameter Values ───────────────────────────────────────────────────
# A default value is used when the caller doesn't provide that argument.
def clean_name(first_name, last_name, country='n/a'):
    first = first_name.strip().lower()
    last  = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)

clean_name(" Kumar ", "Suresh")   # country not provided → uses default


# ─── *args — Variable Number of Positional Arguments ───────────────────────────
# *args collects any number of positional arguments into a TUPLE.
def total(*args):
    print(sum(args))

total(1, 2)
total(1, 2, 3, 4, 5, 6)


# ─── **kwargs — Variable Number of Keyword Arguments ───────────────────────────
# **kwargs collects any number of keyword arguments into a DICTIONARY.
def create_user(**kwargs):
    print(kwargs)

create_user(first_name="Mo",
            last_name="Salah",
            age=33,
            country="Egypt")

create_user(name="Ronaldo",
             country="Portugal")


# ─── return — Sending a Value Back ──────────────────────────────────────────────
# return exits the function and sends a value back to the caller.
def clean_name(name):
    if not name:
        return None
    else:
        cleaned = name.strip().lower()
        return cleaned

cln_name = clean_name("  MariA  ")
print(cln_name)

cln_name = clean_name("")
print(cln_name)


# ─── Returning Multiple Values ───────────────────────────────────────────────────
# Returning several values with a comma returns a TUPLE.
def clean_name(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned

# Unpacking into two variables
lo_name, up_name = clean_name("  MariA  ")
print(lo_name, up_name)

# Without unpacking — captured as a single tuple
cln_name = clean_name("  MariA  ")
print(cln_name)


# ─── Task: Write Application Logs to a File ──────────────────────────────────────
def write_log(message):
    # WSL uses Linux paths! /mnt/d/ maps directly to your Windows D: drive
    # "a" mode = append — adds to the end of the file without erasing existing content
    with open("/mnt/d/Workspace/day2/app.log", "a") as file:
        file.write(message + '\n')

write_log("App Started")
write_log("user logged in")
write_log("App Stopped")


# ─── Task: Clean an Email and Split into Username/Domain ────────────────────────
def clean_and_split_email(email):
    cl_email = email.strip().lower()
    username, domain = cl_email.split("@")
    return {"username": username,
            "domain": domain}

print(clean_and_split_email("  Sara@gmAil.com"))


# ─── Task: Validate Password Length ───────────────────────────────────────────────
def is_valid_password(password):
    return len(password) >= 8

print(is_valid_password("123"))
print(is_valid_password("12345678"))


# ─── Task: Basic Email Format Check ───────────────────────────────────────────────
def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("saragmail.com"))
print(is_valid_email("sara@gmail.com"))
print(is_valid_email("sara@gmailcom"))
print(is_valid_email("saragmailcom"))


# ─── Orchestrator Function ─────────────────────────────────────────────────────────
'''
# Project
 1. Receive an email from the user
 2. Validate the email
 3. If it is invalid, log an error in a file.
 4. If it is valid, clean and structure the email
 5. Log each step of the program.
'''

def process_user_email(email):
    write_log("App Started")

    if not is_valid_email(email):
        write_log(f"Invalid Email received: {email}")
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email: {clean_email}")

    write_log("App Stopped")


email = input("Please enter your Email: ")
process_user_email(email)
