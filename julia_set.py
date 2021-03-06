## This script generates the geometrical fractal(set of points in a complex plane spread out according to an algorithm) of Mandelbrot set: Zn+1 = Zn^2 + C, Z0 = C, where Z is a complex number of the form x+iy
## Simply to put, Mandelbrot set is a set of all C's such that a corresponding Zn doesn't equal infinity when n -> infinity

import numpy
from PIL import Image
from cmath import sin, cos

#Declaring the constants
Min_Re = -2.0
Max_Re = 1.0
Min_Im = -1.5
Max_Im = 1.5
maxIterations = 4096

#width, height = image.size 	# width and height of the rectangle, in which we are going to plot our Mandelbrot set, are equal to the image widht and height

image_width = 1024			# considering an image of resolution 512X512 pixels
image_height = 1024
image = Image.new("RGB", (image_width, image_height))

for y in range(image_height):
	Zy = y * (Max_Im - Min_Im) / (image_height - 1) + Min_Im
	for x in range(image_width):
		Zx = x * (Max_Re - Min_Re) / (image_width - 1) + Min_Re
		# Z = Zx + Zy * 1j	
		Z = 1.0 + 0.1 * 1j
		c = Z
		for n in range(maxIterations):	# Iterating for a certain number of times and checking whether |Z| > 2. If so, it will jump to infinity and hence we quit the iterations for a pixel corresponding to (x,y)			
			if abs(Z.imag) > 5.0: 
				break							
			Z = c * sin(Z) 				# if (x,y) is inside, then for the next iteration, Zn+1 = C * sin(Z)
		R = n % 4 * 512
		G = n % 8 * 256
		B = n % 16 * 64
		image.putpixel((x, y), B*32768 + G*128 + R*8)

image.save("julia_fractal.png", "PNG")
print "Julia_fractal created, Sayo nara.."









