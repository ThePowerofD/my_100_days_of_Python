import traceback #Imports traceback so i can get all the text from an error
import logging # Imports logging module
## Try catch syntaxys

#Try:
    #Try Something
#except:
    # 

#File not Found
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"} #Create dictionary
    print(a_dictionary["sdfsdf"]) #Value no existent in dictionary so it fails
    #print(a_dictionary["key"])
except FileNotFoundError: # Can add ->FileNotFoundError<- so ti expects a specific error for exception
    file = open("a_file.txt", "w")
    #file.write("Something") # Too borad exception clause so it will no give exception if various erros are present so we need to specify type of error for exception Can also add other excepts
except KeyError as error_message:
    print(f"That Key {error_message} does not exist")

else:
    content = file.read()
    print(content)
finally:
    file.close()



### ---Excercises ---###
#Key Error
try:
    a_dictionary = {"key":"value"}
    value = a_dictionary["non_existent_key"]
except Exception as error:
    print(f"An Error occurred it is a {error} type error")

#Index Error
try:
    fruit_list = ["Apple", "Bannana", "Pear"]
    fruit = fruit_list[3]
except Exception as error:
    print(f"An Error occurred it is a {error} type error")

#Type Error --- Using the logging module

# Configure logging ONCE (usually at the top of your program). Import module
# filename -> where logs are written | level -> minimum severity to record
# format   -> how each line looks (timestamp - level - message)
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    text = "abc"
    print(text + 5)
except Exception as error:
    # exc_info=True adds the full traceback to the log automatically
    logging.error("A TypeError occurred while adding str + int", exc_info=True)

# ---------------------------------------------------------------------------
# LOGGING REFERENCE
# ---------------------------------------------------------------------------
# Instead of print(), real programs LOG errors to a file with timestamps.
#
# Setup (run once):
#   logging.basicConfig(filename="app.log", level=logging.ERROR, format=...)
#
# Severity levels (low -> high). "level=" sets the MINIMUM that gets recorded:
#   Function              | When to use
#   ----------------------|--------------------------------------------------
#   logging.debug(msg)    | detailed info for diagnosing problems
#   logging.info(msg)     | normal events ("started", "user logged in")
#   logging.warning(msg)  | something unexpected, but still working
#   logging.error(msg)    | a failure - something didn't work
#   logging.critical(msg) | a serious failure - program may not continue
#
# The "format" string - a template for what each log line looks like.
# The %(...)s pieces are placeholders that logging fills in automatically;
# anything else (like the " - ") is literal text you chose as a separator.
#   Placeholder      | Gets replaced with        | Example
#   -----------------|---------------------------|--------------------------
#   %(asctime)s      | the date & time           | 2026-07-03 14:22:01,533
#   %(levelname)s    | the severity level        | ERROR
#   %(message)s      | the text YOU wrote        | A TypeError occurred...
#   %(lineno)d       | the line number           | 57
#   %(filename)s     | the file name             | main.py
# (The trailing "s"/"d" is old-style formatting: s = string, d = number.)
#
#   format="%(asctime)s - %(levelname)s - %(message)s"
#      -> 2026-07-03 14:22:01,533 - ERROR - A TypeError occurred...
#
# Logging inside an except:
#   logging.error("message", exc_info=True)   # <- adds the full traceback
#   (exc_info=True mixes logging + traceback: it grabs the current exception's
#    traceback and attaches it to the log entry. Only works inside an except.)
#
# Result written to app.log looks like:
#   2026-07-03 14:22:01,533 - ERROR - A TypeError occurred while adding str + int
#   Traceback (most recent call last):
#     File "main.py", line 57, in <module>
#       print(text + 5)
#   TypeError: can only concatenate str (not "int") to str
#
# print() vs logging:
#   print()   -> quick, goes to console, no timestamp/severity, gone when closed
#   logging   -> timestamped, leveled, saved to a file, standard for real apps
# ---------------------------------------------------------------------------



#Writing erros with traceback
try:
    num = 10 / 0
except Exception as error:
    error_text = traceback.format_exc()
    print(error_text)

#Traceback
# ---------------------------------------------------------------------------
# QUICK REFERENCE
# ---------------------------------------------------------------------------
#
# The four blocks:
#   try:      code that might raise an error (runs first, always)
#   except:   runs ONLY if a matching error occurs
#   else:     runs ONLY if NO error occurred in try
#   finally:  runs ALWAYS (error or not) - used for cleanup
#
# When an error is NOT matched by any except:
#   - it escapes/propagates (crashes unless caught further out)
#   - else is SKIPPED, but finally STILL runs before the crash
#
# ---------------------------------------------------------------------------
# Printing / saving errors:
#
#   Call                       | Where it goes        | Returns
#   ---------------------------|----------------------|-------------------------
#   traceback.print_exc()      | prints to console    | nothing
#   traceback.format_exc()     | nowhere (yet)        | the traceback as a string
#   print(error)               | prints to console    | - (short message only)
#
# print(error)              -> "division by zero"  (short, no location)
# traceback.print_exc()     -> full traceback: file, line number, error type
#
# ---------------------------------------------------------------------------
# Do you need "as error"?  Match it to what the handler body uses:
#
#   Handler body                          | Write
#   --------------------------------------|-----------------------------
#   traceback.print_exc() only            | except Exception:
#   print(error) / f"{error}"             | except Exception as error:
#   logging.error(..., exc_info=True)     | except Exception:
#
# (If you bind "as error" but never use it, linters warn: unused variable.)
# ---------------------------------------------------------------------------

### --= Excersises End ---###