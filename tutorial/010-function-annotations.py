# Function Annotations
# --------------------
# Function annotations are completely optional metadata information about the
# types used by user-defined functions.
# Annotations are stored in the __annotations__ attribute of the function as a
# dictionary and have no effect on any other part of the function.
# Parameter annotations are defined by a colon after the parameter name, fol-
# lowed by an expression evaluating to the value of the annotation.
# Return annotations are defined by a literal -> followed by an expression,
# between the parameter list and the colon denoting the end of the def state-
# ment.

def foo(ham: str, eggs: str = 'eggs') -> str:
    """A function that demonstrates function annotations"""
    print("Annotations:", foo.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


foo('spam')

print()

foo('foo', 'bar')

print()

print(help(foo))
