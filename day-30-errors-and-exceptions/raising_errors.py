import logging

## Raising Errors ##
# So far we CAUGHT errors Python threw at us.
# RAISING is when WE throw an error on purpose, because our code is
# "working" but the DATA is invalid and we want to stop loudly.


# --- Example 1: basic raise -------------------------------------------------
# Python is happy with a negative age, but it's nonsense for our program,
# so WE decide it's invalid and raise an error.
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")   # <- we throw it
    return age

# Uncomment to see it crash:
# set_age(-5)      # -> ValueError: Age cannot be negative


# --- Example 2: raising + catching together ---------------------------------
# An error we raise behaves exactly like a built-in one: except can catch it.
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as error:
    print(f"Invalid input: {error}")


# --- Example 3: re-raise (log it, then let it crash) ------------------------
# A bare "raise" inside an except re-throws the SAME error you just caught.
#
# NOTE - WHERE DO THE LOGS GO? You have a CHOICE, set by "filename":
#   logging.basicConfig(level=logging.ERROR)                 # no filename
#       -> logs print to the CONSOLE (stderr). No file is created.  <-- THIS FILE
#   logging.basicConfig(filename="app.log", level=logging.ERROR)
#       -> logs are SAVED to the file "app.log". Nothing prints.    <-- main.py
# So "app.log" only appears when you run main.py, not this file.
logging.basicConfig(level=logging.ERROR)
try:
    num = 10 / 0
except ZeroDivisionError:
    logging.error("Math failed", exc_info=True)   # record it first...
    # raise                                        # ...then let it propagate
    #  (commented so this file runs to the end - uncomment to see it crash)


# ---------------------------------------------------------------------------
# RAISING REFERENCE
# ---------------------------------------------------------------------------
# WHY raise? Code can "work" while the DATA is invalid (age = -5, empty name).
# Raising lets YOU stop the program loudly instead of passing bad data along.
#
# Syntax:  raise <ErrorType>("your message")
#   raise ValueError("Age cannot be negative")
#   raise TypeError("expected a number")
#   raise Exception("something generic went wrong")
#
# Which type to raise:
#   Situation                                   | Common type
#   --------------------------------------------|------------------------
#   wrong VALUE (negative age, empty name)      | ValueError
#   wrong TYPE (got str, wanted int)            | TypeError
#   key / index doesn't exist                   | KeyError / IndexError
#   generic / unsure                            | Exception
#
# Raising + catching are two halves of the same system:
#   raise    -> YOU cause an error on purpose (this situation is invalid)
#   except   -> code REACTS to an error (yours or a built-in one)
#
# Bare "raise" inside an except = RE-RAISE (re-throw the same error):
#   except ZeroDivisionError:
#       logging.error("Math failed", exc_info=True)   # record it
#       raise                                          # then let it crash
#   -> you get BOTH a log entry AND the program still fails loudly
# ---------------------------------------------------------------------------
