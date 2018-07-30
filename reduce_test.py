#!/usr/bin/python3

from functools import reduce
#Reduce is how python does factorial

#This is the more manual way to do factorial
#def mult(inputlist):
#	t o t a l = 1
#	for x in i n p u t l i s t :
#		t o t a l = t o t a l  x
#		return t o t a l


#another way to do factorial
#mylist=[5,4,3,2,1]
#newlist=(what you did in map_test.py)
#finallist=list(map(lambda x : mult(x), newlist))

mylist=[9,7,3]
mapped_list=list(map(lambda x: list(range(x, -1, -1)), mylist))
final_list=list(map(lambda x: reduce(lambda y,z: y*z, list(range(x, 0, -1))), mylist))

print(mylist)
print(mapped_list)
print(final_list)

