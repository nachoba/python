# PEP 8 Style Guide
# -----------------
# Python Enhancement Proposal #8, known as PEP 8, is the style guide for how
# to format Python code. Using a consistent style makes your code more ap-
# proachable and easier to read, and facilitates collaboration on projects.
#
#   The whole guide is at http://www.python.org/dev/peps/pep-0008/
#
# Here are a few rules you should be sure to follow:
#
# Whitespace
# ----------
# In Python, whitespace is syntactically significant, so Python programmers
# are especially sensitive to the effects of whitespace on code clarity.
#   * Use spaces instead of tabs for indentation
#   * Use four spaces for each level of syntactically significant indenting.
#   * Lines should be 79 characters in length or less.
#   * Continuations of long expressions onto additional lines should be inden-
#     ted by four extra spaces for their normal indentation level.
#   * In a file, functions and classes should be separated by two blank lines.
#   * In a class, methods should be separated by one blank line.
#   * Don't put spaces around list indexes, function calls, or keyword argu-
#     ment assignments.
#   * Put one -and only one- space before and after variable assignments.
#
# Naming
# ------
# PEP 8 suggest unique styles of naming for different parts in the language.
# This makes it easy to distinguish which type corresponds to each name when
# reading code.
#
#   * Functions, variables, and attributes should be in lowercase_underscore.
#   * Protected instance attributes should be in _leading_underscore format.
#   * Private instance attributes should be in __double_leading_underscore
#     format.
#   * Classes and exceptions should be in CapitalizedWord format.
#   * Module-level constants should be in ALL_CAPS format.
#   * Instance methods in classes should use self as the name of the first
#     parameter (which refers to the object).
#   * Class methods should use cls as the name of the first parameters (which
#     refers to the class).
#
# Expressions and Statements
# --------------------------
# The Zen of Python states: "There should be one -and preferably only one-
# obvious way to do it". PEP 8 attemps to codify this style in its guidance
# for expressions and statements.
# 
#   * Use inline negation (if a is not b) instead of negation of positive
#     expressions (if not a is b).
#   * Don't check for empty values (like [] or '') by checking the length
#     (if len(somelist) == 0). Use if not somelist and assume empty values
#     implicitly evaluate to False.
#   * The same thing goes for non-empty values (like [1] or 'hi'). The sta-
#     tement if somelist is implicitly True for non-empty values.
#   * Avoid single-line if statements, for and while loops, and except com-
#     pound statements. Spread these over multiple lines for clarity.
#   * Always put import statements at the top of a file.
#   * Always use absolute names for modules when importing them, not names
#     relative to the current module's own path. For example, to import the
#     foo module from the bar package, you should do:
#                                           from bar import foo
#     and not just:
#                                           import foo
#   * If you must do relative imports, use the explicit syntax:
#                                           form . import foo
#   * Imports should be in sections in the following order: standard library
#     modules, third-party modules, your own modules. Each subsection should
#     have imports in alphabetical order.
#
# The Pylint tool is a popular static analyzer for Python source code. Pylint
# provides automated enforcement of the PEP 8 style guide and detects many
# other types of common errors in Python programs. The URL of Pylint is:
#   http://www.pylint.org/


