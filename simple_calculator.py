#!/usr/bin/python3

userinput1=input("Please enter a number from 1 to 10: \n")
operator=input("Please enter one of the math operators: + - / * : \n")
userinput2=input("Please enter another number from 1 to 10: \n")
userinput1=int(userinput1)
userinput2=int(userinput2)


if operator == "+":
		result=userinput1+userinput2
		print(result)
elif operator == "-":
		result=userinput1-userinput2
		print(result)		
elif operator == "/":
		result=userinput1/userinput2
		print(result)
elif operator == "*":
		result=userinput1*userinput2
		print(result)		

else:
	print("Please enter one of the given operators:  \n")
	operator=input("Please enter one of the math operators: + - / * :  \n")
	if operator == "+":
                result=userinput1+userinput2
                print(result)
	elif operator == "-":
                result=userinput1-userinput2
                print(result)
	elif operator == "/":
                result=userinput1/userinput2
                print(result)
	elif operator == "*":
                result=userinput1*userinput2
                print(result)
	else:
		print("Please read the directions. \n")
 
