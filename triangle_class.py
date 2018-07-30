#!/usr/bin/python3

import math
import sys

class triangle:
	def __init__  (self, base, height, hypotenuse):
		self.a=base
		self.b=height
		self.c=hypotenuse

		
		if (self.a>(self.b+self.c)):
			print("The base cannot be the longest side, please try again.")
			sys.exit()	
		
	def perimeter (self):
		self.p=(self.a+self.b+self.c)
		print("The perimeter of this triangle is: %d" %(self.p))

	def height (self):
		
		print("The height of this triangle is: %d" %(self.p-self.c-self.a))

	def triangle_area(self):
		self.area=math.sqrt(self.p/2*((self.p)/2-self.a)*((self.p)/2-self.b)*((self.p)/2-self.c))
		print("The area of this triangle is: %d" %(self.area))

	def print_info(self):
		self.perimeter()
		self.height()
		self.triangle_area()

area_calc=triangle(7, 3, 3)
area_calc.print_info()


