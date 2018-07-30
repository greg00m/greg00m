#!/usr/bin/python3

from functools import reduce

#create area function for "square" and create
#evaulate "rectangle" same as "square", need "length and width" arguements, length 2x and width 2x

class Shape:
        def __init__(self, num_sides, side_lengths=[]):
                self.num_sides = num_sides
                self.side_lengths = side_lengths

        def perimeter(self):
                #self.side_lengths = side_lengths
                return reduce(lambda x, y: x + y, self.side_lengths)



class Square(Shape):

	def __init__(self, side_lengths, num_sides=4):
		self.num_sides = num_sides
		self.side_lengths = []
		self.side_lengths = [side_lengths] * 4

	def area(self):
		self.my_area = self.side_lengths[0] ** 2
		return self.my_area

	def print_shape_details(self):
		print("Shape has %d sides, perimeter %f, area %f" % (self.num_sides, self.perimeter(), self.area()))

	def print_info(self):
		self.print_shape_details()

class Rectangle(Shape):

	def __init__(self, side_length, side_width, num_sides=4):
		self.num_sides = num_sides
		self.side_lengths = []
		self.side_lengths.append(side_length)
		self.side_lengths.append(side_length)
		self.side_lengths.append(side_width)
		self.side_lengths.append(side_width)

	def area(self):
		self.my_area = self.side_lengths[0] + self.side_lengths[2]
		return self.my_area

	def print_shape_detail(self):
		print("Shape has %d sides, perimeter %f, area %f" % (self.num_sides, self.perimeter(), self.area()))

	def print_info(self):
		self.print_shape_detail()

sq_area_calc=Square(5)

sq_area_calc.print_info()

rec_area_calc=Rectangle(3,4)

rec_area_calc.print_info()
