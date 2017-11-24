from fractal import Mandelbrot

man = Mandelbrot([800, 800])
man.setRange(5, 5)
man.doMandelbrot(300)
man.wait()
