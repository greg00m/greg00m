#!/usr/bin/python3


valuetest=False
value=input("Enter a value.")

while valuetest==False:
	try:
		#test this code to see if it is an integer
		value=int(value)
		valuetest=True

	except:
		#if "value" cannot be cast to an integer
		print("The value you entered cannot be cast to an integer, please try again.")
		value=input("Enter another value.")


print("You have successfully converted your entry into the integer: %d" %(value))
