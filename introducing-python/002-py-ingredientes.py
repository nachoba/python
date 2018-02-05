# Chapter 2 : Py Ingredientes: Numbers, Strings, and Variables
# ------------------------------------------------------------------------------

# We will begin our journey by looking at Python's simplest built-in data types:
#   * booleans      Which have the value True or False
#   * integers      Whole numbers such as 42 and 1000000
#   * floats        Numbers with decimal points such as 3.1415 or 1.0e8
#   * strings       sequences of text characters

# In a way, they are like atoms; we will use them individually for now, and com-
# bine them into larger "molecules" later. 
# Each type has specific rules for its usage  and is handled  differently by the
# computer. We'll also introduce variables; names that refer to actual data.


# Variable, Names, and Objects
# ----------------------------
# In Python,  everything -booleans, integers, floats, strings,  even large  data
# structures, functions, and programs- is implemented as an object. An object is
# like a clear plastic box that contains a piece of data. The object has a type,
# such as boolean or integer, that determines what can be done with the data. If
# an object has a type int, you know that you could add it to another int.
# The type also determines if the data value contained can be changed  (mutable)
# or is constant (immutable).  An immutable object is an object that can be ins-
# pected but cannot be changed.
# A mutable object can be changed, but its type can't be changed.  Python, is  a
# strongly typed language,which means that the type of an object does not change
# even if its value is mutable.

# Variables are names that refer to values in the computer's memory that you can
# define for use with your program. In Python, you use "=" to assign a value  to
# a variable. 

a = 7
print(a)
# Produces:
# 7

# Python variables are just names. Assignment does not copy a value; it just at-
# taches a name to the object that contains the data. The name is a reference to
# a thing rather than the thing itself.
# In Python, if  you want  to know the type of anything (a varialbe or a literal
# value), use "type(thing)".

b = type(a)
print(b)
string = 'abc'
print(type(string))
# Produces:
# <class 'int'>
# <class 'str'>

# A class is the definition of an object.  In Python, class and type mean pretty
# much the same thing. 
# Variable names can only contain these characters:
#   * Lowercase letters (a through z)
#   * Uppercase letters (A through Z)
#   * Underscore (_)

# Names cannot begin with a digit.  Also, Python treats names that begin with an
# underscore in special ways.

# Numbers
# -------
# Python has built-in support for integers and floating point numbers. The usual
# math operators are available:

#   +   addition                        5 + 8       =   13
#   -   subtraction                     90 - 10     =   80
#   *   multiplication                  4 * 7       =   28
#   /   floating point division         7 / 2       =   3.5
#   //  integer (truncating) division   7 // 2      =   3
#   %   modulus (remainder)             7 % 3       =   1
#   **  exponentiation                  3 ** 4      =   81

# You can combine the arithmetic operators with assignment by putting the opera-
# tor before the =
# For instance:
#                   a -= 3
# is the same as:
#                   a  = a - 3

print(9 % 5)
# Produces:
# 4
# Which is the remainder when the first number is divided by the second.

print(divmod(9, 5))
# Produces:
# (1, 4)
# So the function divmod( ) returns a tuple with  both, the quotient and the re-
# mainder at once.

# Precedence
# ----------
# P-arentheses
# E-xponentiation
# M-ultiplication
# D-ivision
# A-ddition
# S-ubtraction

# Bases
# -----
# Integers are assumed to be decimal (base 10) unless you use a prefix to speci-
# fy another base. 
# 0b or 0B          binary          base 2
# 0o or 0O          octal           base 8
# 0x or 0X          hexadecimal     base 16

print('10 in binary is ' + str(0b10))
# Produces:
# 10 in binary is 2

# Type Conversions
# ----------------
# To change other Python data types to an integer, use the int() function.  This
# will keep the whole number and discard any fractional part.
# Python's simplest data type is the boolean, which has only two values True and
# False. When converted to integers, they represent the values 1 and 0:

print('True,  when converted to an integer is', int(True))
print('False, when converted to an integer is', int(False))
# Produces:
# True,  when converted to an integer is 1
# False, when converted to an integer is 0

# Converting a floating number to an integer  just lops off everything after the
# decimal point:

print('The floating number 98.6, when converted to an integer is', int(98.6))
# Produces:
# The floating number 98.6, when converted to an integer is 98

# Finally, here is an example of converting a text string that contains only di-
# gits, possibly with + or - signs:

print('The string "99"  is', int('99'))
print('The string "-23" is', int('-23'))
# Produces:
# The string "99"  is 99
# The string "-23" is -23

# int() will make integers from floats or strings of digits, but will not handle
# strings containing decimal points or exponents. An exception will occur.

# If you mix numeric types,  Python will sometimes try to  automatically convert
# them for you:

print(4 + 7.0)
print(False + 1)
# Produces:
# 11.0
# 1

# Python handles humungous integers with no problem, there's no risk of an inte-
# ger overflow. 

# Floats
# ------
# Integers are whole numbers, but floating-point numbers (called floats in  Py-
# thon) have decimal points.  Floats are handled similarly to integers: you can
# use the operators (+, -, *, /, //, **, %) and divmod() function.
# To convert other types to float, you use the float() function. As before, boo-
# leans act like tiny integers. 

print('Converting a boolean True to a float:', float(True))
print('Converting an integer to a float:', float(98))
print('Converting a string with integers to a float:', float('99'))
print('Converting a string with floats to a float:', float('98.6'))

# Produces:
# Converting a boolean True to a float 1.0
# Converting an integer to a float 98.0
# Converting a string with integers to a float 99.0
# Converting a string with floats to a float 98.6

# Strings
# -------
# Python 3 can  contain characters from any written language in  the world, plus
# a lot of symbols. Python supports the Unicode standard.
# Strings are our first example  of a Python sequence.  In this case, they are a
# sequence of characters.  Strings in Python are immutable; you can not change a
# string in-place,but you can copy parts of strings to another string to get the
# same effect.

# Create with Quotes: you make a string by enclosing characters in either single
# or double quotes.  The main purpose to having  two types of quotes is that you
# can have single quotes inside double quotes and viceversa.

print("Hello this is Python's string.")
print('She said "Hello".')
# Produces:
# Hello this is Python's string.
# She said "Hello".

# You can also use three single quotes (''') or three double quotes (""").  This
# kind of quotes are common to create multiline strings
poem = '''
There was a Young Lady of Norway,
Who casually sat in a doorway;
When the door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway.'''

print(poem)
# Produces:
# There was a Young Lady of Norway,
# Who casually sat in a doorway;
# When the door squeezed her flat,
# She exclaimed, "What of that?"
# This courageous Young Lady of Norway.

# Convert Data Types by Using str()
# ---------------------------------
# You can convert other Python data types to strings by using the str() function

print(str(98.6))
print(str(True))
# Produces:
# 98.6
# True

# Python  uses the str() function internally  when you call print() with objects
# that are not strings and when doing string interpolation.

# Escape Sequences with \
# -----------------------
# Python lets you escape the maning of some characters within strings to achieve
# effects that would otherwise be hard to express. By preceding a character with
# a backslash (\), you give it a special meaning. 
#   \n      newline
#   \t      tab
#   \'      '
#   \"      "
#   \\      \

print("This\tstring\t\tis\ttabbed")
print("This\tsentence\tis\ttabbed")
# Produces:
# This    string          is      tabbed
# This    sentence        is      tabbed

# Combine with +
# --------------
# You can combine literal strings or string  variables in  Python by using the +
# operator. Python does not add a space when concatenating strings, but it  adds
# a space between each argument to a print() statement,and a new line at the end

print("This is a sentence " + "concatenated with" + " another sentence.")
# Produces:
# This is a sentence concatenated with another sentence.

# Duplicate with *
# ----------------
# You use the * opeator to duplicate a string:

print("No " * 4)
# Produces:
# No No No No

# Extract a Character with []
# ---------------------------
# To get a single  character from a string, specify its "offset"  inside  square
# brackets after the string's name. The first (leftmost) offset is 0, next is 1,
# and so on.
# The last (rightmost) offset can be specified with -1, going to the left are -2
# -3, and so on.

letters = 'abcdefghijklmnopqrstuvwxyz'
print("The letter at offset  0 is", letters[0])
print("The letter at offset  1 is", letters[1])
print("The letter at offset -1 is", letters[-1]) 
print("The letter at offset -2 is", letters[-2])
# Produces:
# The letter at offset  0 is a
# The letter at offset  1 is b
# The letter at offset -1 is z
# The letter at offset -2 is y

# If you specify an  offset that is the length of the string or longer, you will
# get and exception. Indexing works the same with the other sequence types:lists
# and tuples.
# Because strings are immutable, you can't insert  a character directly into one
# or change the character at a specific index, instead you need to use some com-
# bination of string functions such as replace() or a slice.

name = "Nacho"
print(name.replace('N', 'C'))
# Produces:
# Cacho

# Slice with [ start : end : step ]
# ---------------------------------
# You can extract a substring (part of a string) from a string by using a slice.
# You define a slice by using square  brackets, a start offset,  and end offset,
# and an optional step size.
# Some of these can be omitted.  The slice will  include characters  from offset
# start to one before end.
#
#   * [:]                    extracts the entire squence from start to end. 
#   * [ start : ]            specifies from the start offset to the end.
#   * [ : end ]              specifies from the beginning to the end  offset mi-
#                            nus 1.
#   * [ start : end ]        indicates  from the start offset to the end  offset
#                            minus 1.
#   * [ start : end : step ] extracts  from the start  offset to the  end offset
#                            minus 1, skipping characters by step.
#
# As before, offsets go 0, 1, and so on from the start to the right, and -1, -2,
# and so forth from the end to the left.  If you don't specify start,  the slice
# uses 0 (the beginning).If you don't specify end,it uses the end of the string.

print(letters[:])               # Prints the whole letters sequence.
print(letters[20:])             # Prints 'uvwxyz' from offset 20 to the end.
print(letters[12:15])           # Prints 'mno'  from offset 12 to 14.   The last
                                # last offset is not printed.
print(letters[-3:])             # Prints the three last characters: 'xyz'.
print(letters[4:20:3])          # Prints from offset 4 to 19, by 3: 'ehknqt'
print(letters[-1::-1])         # Starts at the end, to the start, by -1

# Get Length with len()
# ---------------------
# The len() function counts characters in a string. Also, the len() function can
# be used with other sequence types.

print(len(letters))
print(len(''))
# Produces:
# 26
# 0

# Split with split()
# ------------------
# Unike len(), some functions are specific to strings.  To use a string function
# type the name of the string, a dot, the name of the function,and any arguments
# that the function needs:
#                               string.function(arguments)
# 
# You can use the built-in "split()" function to break  a string into a  list of
# smaller strings based on some separator. A list is a sequence of values, sepa-
# rated by commas and surrounded by square brackets.

todos = 'get gloves,get maks,give cat food,call taxi'
print(todos.split(','))
# Produces:
# ['get gloves', 'get maks', 'give cat food', 'call taxi']

# If you do not specify a separator, "split()" uses any sequence of white  space
# character -newlines, spaces, and tabs.

print(todos.split())
# Produces:
# ['get', 'gloves,get', 'maks,give', 'cat', 'food,call', 'taxi']


# Combine with join()
# -------------------
# The function join() is the opposite of split(): it collapses a list of strings
# into a single string. You have to specify the string that glues everything to-
# gether first, and then the list of strings to glue:
#                                                       string.join(list)
#
# So, to join the list "lines" with separating newlines, you would say:
#                                                       '\n'.join(lines)

cryptos = ['Bitcoin', 'Monero', 'Etethereum']
print(', '.join(cryptos))
# Produces:
# Bitcoin, Monero, Etethereum


# Other String Functions
# ----------------------
# .startswith()     Does the string starts with ... 
# .endswith()       Does the string ends with ...
# .find()           Find the first occurrence of ...
# .rfind()          Find the last occurrence of ... 
# .count()          Count the ocurrences of ...
# .isalnum()        Are all characters alpha-numeric?

print(poem)
print(poem.startswith('\n'))
print(poem.endswith('all'))
print(poem.find('of'))
print(poem.rfind('of'))
print(poem.count(' a '))
print(poem.isalnum())
# Produces
# True      => Starts with a newline character
# False     => Does not end with 'all'
# 24        => The first occurrence of 'of' is at offset 24
# 157       => The last occurrence of 'of' is at offset 157
# 2         => There are two ' a ' in the poem
# False     => Not all characters are alphanumeric (there are some punctuation)


# Case and Alignment
# ------------------
# Some more built-in string functions.
# .strip()          => Remove ... from both ends
# .capitalize()     => Capitalize the first word
# .tittle()         => Capitalize all the words
# .upper()          => Convert all characters to uppercase
# .lower()          => Convert all characters to lowercase
# .swapcase()       => Swap upper and lowercase
# .center(n)        => Center the string within n spaces
# .ljust(n)         => Left justify within n spaces
# .rjust(n)         => Right justify within n spaces

setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())
print(setup.center(40))
print(setup.ljust(40))
print(setup.rjust(40))
# Produces:
# a duck goes into a bar
# A duck goes into a bar...
# A Duck Goes Into A Bar...
# A DUCK GOES INTO A BAR...
# a duck goes into a bar...
# A DUCK GOES INTO A BAR...
#        a duck goes into a bar...
# a duck goes into a bar...
#                a duck goes into a bar...


# Substitute with replace()
# -------------------------
# You use replace() for simple substring substitution.You give the old substring
# the new one, and how  many instances of the  old substring  to replace. If you 
# omit this final count argument, it replaces all instances.

print(setup.replace('duck', 'marmot'))
print(setup.replace('a ', 'a famous ', 100))
# Produces:
# a marmot goes into a bar...
# a famous duck goes into a famous bar...

# When you know the exact substring(s) you want to change, "replace()" is a good
# choice.  But watch out, in the second example, vif we had substituted  for the
# single  character 'a' rather than the two character string 'a ', we would have
# also changed a in the middle of other words!!

print(setup.replace('a', 'a famous', 100))
# Produces:
# a famous duck goes into a famous ba famousr...

# Sometimes you want  to ensure that the substring is a whole  word, or the beg-
# ginning of a word, and so on. In those, cases, you need regular expressions.


# Things to Do
# ------------
# 2.1 How many seconds are in an hour? Use the interactive interpreter as a cal-
# culator and multiply the  number of seconds in  a minute (60) by the number of
# minutes in an hour (also 60).

seconds_per_hour = 60 * 60
print("There're", seconds_per_hour, "seconds in an hour")

# 2.3 How many seconds are in a day?

seconds_per_day = seconds_per_hour * 24
print("There're", seconds_per_day, "seconds in a day")

