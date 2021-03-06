import turtle

'''
Turtle Graphics :: Using Turtle Module in Python
------------------------------------------------
Turtle graphics is a popular way for introducing programming to kids.   It was 
part of the original Logo programming language developed by Wally Feurzig  and 
Seymour Papert in 1966.
Imagine a robotic turtle starting at (0, 0) in the x-y plane.  After an import 
turtle, give it the  command turtle.forward(15),  and it moves (on-screen!) 15 
pixels in the direction it is facing, drawing a line as it moves.  Give it the 
command turtle.right(25), and it rotates in-place 25 degrees clockwise.
By combining together these and similar commands,intricate shapes and pictures
can easily be drawn.

The turtle module is an extended reimplementation of the same  module from the
Python standard distribution up to version Python 2.5.It tries to keep the me-
rits of the old turtle module and to be (nearly) 100% compatible with it. This
means in the first place to enable the learning programmer to use all the com-
mands,classes and methods interactively when using the module from within IDLE
run with the -n switch.

The turtle module provides turtle graphics primitives, in both object-oriented
and procedure-oriented ways.  Because it uses tkinter  for the underlying gra-
phics,it needs a version of Python installed with Tk support.The object-orien-
ted interface uses essentially two+two classes:

    1. The TurtleScreen class defines graphics windows as a playground for the
    drawing turtles.Its constructor needs a tkinter.Canvas or a ScrolledCanvas
    as argument.  It should be used when turtle is  used as part of some appli-
    cation.
    The  function Screen()  returns a singleton object of a  TurtleScreen  sub-
    class.This function should be used when turtle is used as a standalone tool
    for doing graphics. As a singleton object, inheriting from its class is not
    possible.
    All methods of TurtleScreen/Screen also exist as functions,  ie  as part of
    the procedure-oriented interface.

    2. RawTurtle  ( alias: RawPen )  defines Turtle  objects  which  draw on a 
    TurtleScreen.Its constructor needs a Canvas,ScrolledCanvas or TurtleScreen
    as argument, so the RawTurtle objects know where to draw.
    Derived from RawTurtle is the subclass Turtle (alias: Pen), which draws on
    the Screen instance which is automatically created,if not already present.
    All methods of RawTurtle/Turtle also exist as functions,  i.e. part of the
    procedure-oriented interface.



The procedural interface provides functions which are derived from the methods
of the classes Screen and Turtle.They have the same names as the corresponding
methods.  A screen object is automatically created whenever a function derived
from a  Screen method is called.  An (unnamed) turtle object  is automatically 
created whenever any of the functions derived from a Turtle method is called.

To use multiple turtles on  a screen one has to use the object-oriented inter-
face.
'''

turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


