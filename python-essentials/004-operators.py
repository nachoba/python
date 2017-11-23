# Introducing the Buit-In Operators
# ---------------------------------
# Operators in Python fall into three broad groups:
#   
#   Arithmetic      + - * ** / // %
#   Bit-Oriented    << >> & | ^ ~
#   Comparison      < > <= >= == !=
#
# Most of the operators are binary operators, only ~ is unary, and many
# can be used in either context.
# The arithmetic operators have meanings similar to those used in other
# programming languages.
# Bit-oriented operators apply only to integers and sets. These are not
# logical operators.
# The comparison operators also have meaning similar to those used in
# other programming languages. The result of a comparision is a Boolean
# (True or False) irrespective of the types of the two operands.
#
# Python does not have primitive types, all Python objects are proper
# instances of a class, so the method == is defined for integers, floats
# strings, etc.
# 
# Using Integers
# --------------
# Python integers are objects of the class int. These objects have the
# largest number of operators, including all of the arithmetic, bit o-
# riented, and comparison.
# Integer values are limited by memory, this means that they can be quite
# large (for instance we can compute 1000!).
# General we use integers in decimal, base 10, but they can be written in
# hexadecimal (use the 0x prefix), octal (use the 0o prefix), and binary
# (use the 0b prefix).
#
# Using the Bit-Oriented Operators
# --------------------------------
# Bit-oriented operators are defined for integers. They're not defined for
# complex or floating-point objects.
# The << and >> operators perform bit shifting.
#   1 << 8 => 256   We have shifted the value 1 to the left 8 bit positions.
#
# The &, | and ^ operators computes the bitwise "and", "or", and "xor" of
# two integer values. We can use the bin() function to visualize how the
# bitwise operators work.
#
#   bin(9)      =>  0b1001
#   bin(5)      =>  0b101
#   9 | 5       =>  0b1001 | 0b101  =>  0b1101   =>  13
#
# The ~ operator is the bitwise two's complement of an integer value. For
# instance:
#
#   ~14         =>  -15
#
# This are not logical operators. Do not confuse "a & b" with "a and b".
#
#
# Using Rational Numbers
# ----------------------
# Rational numbers are fractions composed of two integer values. Python
# doesn't have a built-in rational number type. We must import the Fraction
# class using:
#   
#   from fractions import Fraction
#
# This will introduce the Fraction class definition to our global environment.
# Once we have this, we can create objects of the class Fraction as follows:
# 
#   Fraction(355, 113)
#
# Arithmetic and comparison operators apply to fractions. Performing an 
# operation that involves a Fraction value and an int value requires that
# the int object is coerced up to the Fraction class.
# We can extract the numerator and denominator of a fraction using their
# attribute names. For example:
#
#   a = Fraction(355, 133) * 5
#   a.numerator                     =>  1775
#   a.denominator                   =>  113
#
# We have created a Fraction object a, from an expression involving a
# Fraction object and an integer. We've then extracted the numerator and
# denominator attributes of the variable a.
#
#
# Using Decimal Numbers
# ---------------------
# For currency calculations, we generally use Decimal numbers. Python does
# not have a built-in decimal number type. We import the Decimal class using:
#
#   from decimal import Decimal
#
# This will introduce the Decimal class definition to our global namespace.
# We can now create Decimal objects. It is important to avoid accidentally
# mixing Decimal and float values, because float values are only an appro-
# ximation. To be sure that Decimal values are exact, we must use only
# integers or strings:
#
#   Decimal("2.72")
#
# For common financial calculation, Decimal is required. For example:
#
#   a = Decimal('512.91')
#   b = Decimal('5.97')
#   c = Decimal('0.075')
#   (a + b) * c             =>  Decimal('38.91600')
#
# If we try this kind of financial calculation with floating-point numbers,
# we have a bit of a problem:
#
#   (512.91 + 5.97) * 0.075 =>  38.916
#
# Python coercion rules work well with Decimal and int values. But mixing
# Decimal with float leads to a TypeError exception. We must explicitly
# convert Decimal to float to do mixed-type expressions.
#
#
# Using Floating-Point Numbers
# ----------------------------
# Floating-point values are instances of the class float. These objects work
# with arithmetic and comparison operators. They don't participate in the bit
# oriented operators.
# We can write floating-point numbers two ways: as digits with a decimal point,
# as well as in "scientific" notation:
#
#   645.345
#   6.33E3 => 6.33x10^3
#
# Note that exact equality comparison between floating-point numbers, while
# permited, is generally not a goot idea. Instead of "a == b" we need to focus
# on "abs(a - b) < e"
#
# Using Complex Numbers
# ---------------------
# The top of Python's number tower is the complex type. When working with com-
# plex numbers, we often import the cmath library instead of the math library.
# The math.sqrt() function is constrained to work only with float values, and
# will raise an exception rather than provide an imaginary value. Instead we
# should use the cmath.sqrt() function.


