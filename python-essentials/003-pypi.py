# Python Essentials
# -----------------
#
# Using the Python Package Index :: PyPI
# --------------------------------------
# Many developers will register their modules with the PyPI. This is located at
#            http://pypi.python.org
#
# This is the second place to look for a module that might help solve a particu-
# lar problem. the first place is always the standard library.
# There are three common ways to download and install software from the PyPI:
#
#    * Using pip
#    * Using easy_install
#    * Manually
#
# Generally, we'll use tools such as pip or easy_install for almost our instal-
# lations, but once in a while we may need to resort to a manual installation.
# Some modules may involve binary extensions to Python; these are generally
# C-language-sources, so they must be compiled to be useful.
#
# Using pip to Gather Modules
# ---------------------------
# The pip program is part of Python. To use pip to install a package, we gene-
# rally use a command such as:
#
#    pip install some-package
#
# The pip program will search PyPI for the package named some-package. The
# installed Python version and OS information will be used to locate the 
# latest-and-greatest version that's appropriate for the platform. The files
# will be downloaded, and the Python setup.py file that comes with the package
# will be run automatically to install it.
# The pip program has a number of additional features to uninstall packages and
# track which packages have been added to the initial Python installation. The
# pip program can also create installable packages of your new creation.
#
# Using easy_install to Add Modules
# ---------------------------------
# The easy_install package is part of the setuptools package. We use it like
# this to install a package:
#
#    easy_install some_package
#
# The easy_install is similar to pip, it will search PyPI for the package
# named some-package. 
#
# Installing Modules Manually
# ---------------------------
# In rare cases we may have a package that isn't in the PyPI and can't be
# located by pip or easy_install. In this case we have to manually install it.
# This involves three steps:
#    * Download the source code.
#    * Unpack the source code.
#    * Set-up using the included setup.py file which will do the final instal-
#      lation. We need to run the following command in the directory in which
#      the source code is located:
#
#        python setup.py install
#
# The setup.py script uses Python's distutils package to define what must be
# installed into the Python library directory structure. The install option
# states what we want to do with the package. In rare cases a package may
# consist of a single module file that may not contain a setup.py file. In
# this case, we will manually copy the file to our own site-packages direc-
# tory.


