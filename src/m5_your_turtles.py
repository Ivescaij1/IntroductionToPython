"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  Junfei Cai  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

turtleB = rg.SimpleTurtle('turtle')
turtleB.pen = rg.Pen('Black', 3)
turtleB.speed = 20

size = 100

for k in range(9):
    turtleB.draw_regular_polygon(8, size)

    turtleB.pen_up()
    turtleB.right(90+22.5)
    turtleB.forward(10)
    turtleB.left(90+22.5)

    turtleB.pen_down()
    size = size + 10


turtleR = rg.SimpleTurtle('turtle')
turtleR.pen = rg.Pen('Red', 3)
turtleR.speed = 10

size = 120

turtleR.pen_up()
turtleR.forward(50)
turtleR.pen_down()

for k in range(8):
    turtleR.draw_circle(size)

    turtleR.pen_up()
    turtleR.left(90)
    turtleR.forward(10)
    turtleR.right(90)

    turtleR.pen_down()
    size = size - 10

window.close_on_mouse_click()