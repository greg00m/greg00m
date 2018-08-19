#!/usr/bin/python3

def concatenate_string(first, second):
	retval = ""
	if first != None and second != None:
		retval = "%s%s" %(first, second)
	return retval

def test():
	checkval = "Hello World!"
	ret = concatenate_string("Hello", "World!")
	if ret == checkval: 
		print("Concatenate works!")
	else: 
		print("Concatenate is broken.")

#Define a main function 
def main():
	print("Program has been run direcly by Python (calling test)")
	test()

#Check if special variable __name__ is __main__
if __name__ == "__main__":
	#if so, call the main fucntion
	main()

else:
	print("Python script has been included in another program.")
