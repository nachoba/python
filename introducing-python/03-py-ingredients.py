# Introducing Python
# Chapter 02 :: Py Ingredients: Numbers, Strings, and Variables
# -----------------------------------------------------------------------------
# In this chapter we will begin by looking at Python's simplest built-in data
# types:
#           * booleans      which have a value of True or False
#           * integers      whole numbers such as 42 and 1_000_000
#           * float         numbers with decimal points
#           * strings       sequences of text characters
#
# Each type has specific rules for its usage and is handled differently by the
# computer. We will also introduce variables, names that refer to actual data.
#
# Variables, Names, and Objects
# -----------------------------
# In Python, everything -booleans, intengers, floats, strings, even large data
# structures, funtions, and programs- is implemented as an object.
# 
# An object is like a clear plastic box that contains a piece of data. The ob-
# ject has a type, such as boolean or integer, that determines what can be done
# with the data.
# The type also determines if the data value contained by the box can be chan-
# ged (mutable) or is constant (immutable).
# Python is strongly typed, which means that the type of an object does not
# change, even if its value is mutable.
#
# Programming languages allow you to define variables. These are names that
# refer to values in the computer's memory that you can define for use with your
# program. In Python you use = to assign a value to a variable.

a = 7
print(a)

# Variables are just names. Assignment does not copy a value; it just attaches
# a name to the object that contains the data. The name is a reference to a thing
# rather than the thing itself.
#
# In Python, if you want to know the type of anything (a variable or a literal
# value), use the:  type(thing)
# function.

print(type(a))
print(type(print))
print(type(type))

# A class is the definition of an object, class and type mean pretty much the
# same thing.
#
#
# Numbers
# -------
# Python has buit-in support for integers and floating point numbers. The allowed
# operators are:

print("\nInteger math")
print("3 +  5 = ", 3 + 5)
print("3 -  5 = ", 3 - 5)
print("3 *  5 = ", 3 * 5)
print("3 /  5 = ", 3 / 5)
print("3 // 5 = ", 3 // 5)
print("3 %  5 = ", 3 % 5)
print("3 ** 5 = ", 3 ** 5)

print("\n\nFloating-point Math")
print("3 +  5 = ", 3.0 + 5.0)
print("3 -  5 = ", 3.0 - 5.0)
print("3 *  5 = ", 3.0 * 5.0)
print("3 /  5 = ", 3.0 / 5.0)
print("3 // 5 = ", 3.0 // 5.0)
print("3 %  5 = ", 3.0 % 5.0)
print("3 ** 5 = ", 3.0 ** 5.0)


# Bases
# -----
# Integers are assumed to be base 10, decimal. But we can use a prefix to indi-
# cate another base:
#                       * 0b        for binary
#                       * 0o        for octal
#                       * 0x        for hexadecimal

print("\nNumbers in other bases")
print("1111 binary is   : ", 0b1111)
print("1111 octal is    : ", 0o1111)
print("FF hexadecimal is: ", 0xFF)


# Type Conversions
# ----------------
# To change other Python data types to an integer, use the int() function. This
# will keep the whole number and discard any fractional part.

print("\nType Conversions\n")
print("From other types to int")
print("Boolean True      = ", int(True))
print("Boolean False     = ", int(False))
print("String '99'       = ", int('99'))
print("Float 2.4535      = ", int(2.4535))

# Similarly to convert to a float, use the float() function.
print("\nFrom other types to float")
print("Boolean True      = ", float(True))
print("Boolean False     = ", float(False))
print("String '99'       = ", float('99'))
print("String '99.99'    = ", float('99.99'))
print("Int  2            = ", float(2))

# Strings
# -------
# Strings in Python are immutable. You can't change a string in-place, but you
# can copy parts of strings to another string to get the same effect.
# Python's strings can be expressed by " " or ' ', the reason of using both is
# to allow for strings like 'He said "Hello"' or "Here's something special"

print("\nStrings")
print('He said "Hello"')
print("Here's something special")

# Triple quotes are used for multiline strings
print("\nMulti-line strings")
some_string = """\tThere was a young Lady of Norway;
\tWho casually sat in a doorway;
\tWhen the door squeezed her flat,
\tShe exaclaimed, 'What of that?"""
print(some_string)

# Convert Data Types by Using str()
# ---------------------------------
# You can convert other Python data types to strings by using the str() function:
print("\nConverting to Strings")
print("98.6 = ", str(98.6), "\t", type(str(98.6)))
print("True = ", str(True))

# Some String Operators:
# ----------------------
print("\nSome string operators:")
print("You can concatenate strings " + "with +")
print("You can repeteat a string with * ", "three times " * 3)
some_string = "hello world"
print("You can extract a character with []. some_string[0] = ", some_string[0])
print("You can slice with [start: end : step]. some_string[::2]",
      some_string[::2])
print("some_string[0:6] ", some_string[0:5])
print("some_string[-5:] ", some_string[-5:])

# You can get the length of a string with the len() function
print("\nThe length of some_string is", len(some_string), "characters")

# You can split a string with .split() method
print("Split with space ", some_string.split(" "))
print("Split with o     ", some_string.split('o'))

# You can join a string with .join()method
string1 = some_string.split(" ")
print("Split the string : ", string1)
print("Join the string  : ", ", ".join(string1))

# Other string methods
print("Strip a char 'd'        : ", some_string.strip('d'))
print("Capitalize string       : ", some_string.capitalize())
print("Capitalize all the words: ", some_string.title())
print("Convert to uppercase    : ", some_string.upper())
print("Convert to lowercase    : ", some_string.lower())
print("Swap cases              : ", some_string.swapcase())
print("Center the string       : ", some_string.center(30))
print("Left Justify the string : ", some_string.ljust(30))
print("Rigth Justify the string: ", some_string.rjust(30))
print("Substitute with replace : ", some_string.replace("world", "nacho"))
