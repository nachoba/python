# Python's Numeric Tower
# ----------------------
#
# Python has three built-in numeric types: int, float, complex, plus two
# more types -Fractional and Decimal- imported from the standard library.
# The numbers module in the standard library provides four base class de-
# finitions for the numeric types. We rarely need to use this module ex-
# plicitly; it's a convention that we need when we have to implement our
# own numeric types.
#
# The numeric types form a kind of "tower" that parallels the various
# kinds of numbers seen in conventional mathematics.
#
# The foundation of the tower is integers.
# Rational numbers are above integers.
# Floating-point values are still further up.
# Complex numbers are at the top of the tower.
#
# There are two general coercion rules to have in mind:
# 1. If both operands are of the same type, the result has that type.
# 2. If the operands are mixed, one of them will be coerced "up" the
#    numeric tower: integer -> rational -> floating-point -> complex.
#
# There is one notable exception to the preceding rules. The / and //
# operators define two different kinds of division. The / operator provides
# true division: even integer operands will yield a floating-point result.
#
# The // operator provides floor division: the result will be truncated as
# if it were an integer-only division. The resulting type won't be coerced
# but the answer will be truncated.


