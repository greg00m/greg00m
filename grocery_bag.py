#!/usr/bin/python3

#create a grocery bag and fill it with items, grocery bag should be a dictionary

class ShoppingBag:
	def __init__(self):
		self.my_bag = {}

	def __add__(self, another_bag):

		temp = ShoppingBag()
		for foodname in self.my_bag:
			temp.my_bag[foodname] = self.my_bag[foodname]

		for foodname in another_bag.my_bag:
			if foodname in temp.my_bag:
				temp.my_bag[foodname] = another_bag.my_bag[foodname] + temp.my_bag[foodname]
			else:
				temp.my_bag[foodname] = another_bag.my_bag[foodname]
		return temp

	def __sub__(self, another_bag):
		temp = ShoppingBag()
		for foodname in self.my_bag:
			temp.my_bag[foodname] = self.my_bag[foodname]

		for foodname in another_bag.my_bag:
			if foodname in temp.my_bag:
				temp.my_bag[foodname]= another_bag.my_bag[foodname] - 0
			else: 
				temp.my_bag[foodname] = another_bag.my_bag[foodname]


		return temp


	def add_item(self, foodname = "", quantity = 0):
		 
		if foodname in self.my_bag:
			self.my_bag[foodname] = self.my_bag[foodname]+quantity
		else:
			self.my_bag[foodname] = quantity



my_bag = ShoppingBag()
another_bag = ShoppingBag()
my_bag.add_item("bananas", 10)
my_bag.add_item("apples", 5)
another_bag.add_item("apples", 7)
combined_bag = my_bag + another_bag
subtracted_combined_bag = combined_bag - another_bag    

print(combined_bag.my_bag)
print(subtracted_combined_bag.my_bag)
