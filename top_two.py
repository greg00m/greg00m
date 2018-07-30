#!/usr/bin/python3



mylist=[10,23,66,4,87,200,0]

def top_two(mylist):
	largest_integer = max(mylist)
	mylist.remove(largest_integer)

	second_largest_integer = max(mylist)
	return largest_integer, second_largest_integer

first, second=top_two(mylist)

print("The two highest numbers from the list are: %d and %d"%(first, second))



#mylist=[10,23,66,4,87,200,0]
#largest, larger = mylist[0], mylist[0]

#def top_two(mylist):
	#for num in alist:
	#    if num > largest:
	#        largest, larger = num, largest
	#    elif num > larger:
	#        larger = num
	#print("The two highest numbers from the list are: %d and %d"%(first, second))
	#return largest, larger


#first, second=top_two(mylist)

#print("The two highest numbers from the list are: %d and %d"%(first, second))
