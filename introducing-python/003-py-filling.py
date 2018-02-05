# Chapter 3 : Py Filling: Lists, Tuples, Dictionaries, and Sets
# ------------------------------------------------------------------------------

# Before started with Python's basic data types: booleans, integers, floats, and
# strings. If you thinks  of those as atoms, the data structures in this chapter
# are like molecules. That's, we combine those basic types in more complex ways.


# Lists and Tuples
# ----------------
# Most computer languages can represent a sequence of items indexed by their in-
# teger position: first, second, and so on down to the last.Python's strings are
# sequences, sequences of characters. 
# Python has two other sequence structures: tuples and lists. These contain zero
# or more elments. Unlike strings, the elements can be of different types.
# In fact, each element  can be any Python object.   This lets you create struc-
# tures as deep and complex as you like.

# The difference between lists and tuples is that tuples are immutable; when you
# assign elements to a tuple, they can't be changed.
# Lists are mutable, meaning you can insert and delete elements. 

# Lists
# -----
# Lists are good for keeping track of things by their order, especially when the
# order and contents might change. Unlike strings, lists are mutable.You can add
# delete, and remove elements. 

# Create with [] and list()
# -------------------------
# A list is made from zero or more elements, separated by commas, and surrounded
# by square brackets:

empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

# You can also make an empty list with the "list()" function:

another_empty_list = list()

# In a list values do not need to be unique.  If you know you  only want to keep
# track of unique values and do not care about  order, a Python "set" might be a
# better choice than a list.

print(weekdays)
print(another_empty_list)

# Conver other Data Types to Lists with list()
# --------------------------------------------
# Python's "list()" function, converts other data types to lists:

cat_list = list('cat')
print(cat_list)

# This example converts a tuple to a list:

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

