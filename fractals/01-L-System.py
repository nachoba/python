# Fractals using the fractal package
# pip install fractal
# https://github.com/ChenL1994/fractal

from fractal import Pen
from math import sqrt

p = Pen([500, 270])
p.setPoint([140, 60])
p.setWidth(1)
p.doD0L(omega = "L", P = {"L": "L+R", "R": "L-R"}, delta = 90, times = 15, length = 200, rate = sqrt(2))
p.wait()
