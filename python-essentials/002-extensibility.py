# Python Essentials
# -----------------
# 
# The Idea of Extensibility via Add-Ons
# -------------------------------------
#
# Python's design includes a small core language that can be extended by impor-
# ting additional features. There are 20 statements and there are only 19 ope-
# rators. The idea is that we can have a small, correctly implemented, and con-
# sistent language.
#
# It's typical to see Python programs that import numerous packages from the
# standard library. We'll see two common variations of the "import" statement:
#
#    import math                     [1]
#    from math import sqrt, sin      [2]
#
# [1] The first version imports the entire module and creates the module as an
# object in the global namespace. The various classes and function names within
# that module must be properly qualifed with the namespace to be used. A quali-
# fied name will look similar to:
#
#    math.sqrt()
#    math.sin()
#
# [2] While the second version also imports the math module, it only introduces
# the given names into the global namespace. These names do not require quali-
# fiers. We can directly use"
#
#    sqrt()
#    sin()
#
# as if they were built-in functions. The math module object, however, is not
# available, since it was not introduced into the global namespace.
#
#
# An import happens exactly once. Python tracks the imported modules and will
# not import a module a second time. This allows us to freely import modules
# as needed without worrying about the order or other obscure dependencies
# among modules.




