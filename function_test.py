#!/usr/bin/python3

def add(x,y):
	
	print(x)
	print(y)
	sum=int(x)+int(y)
	print("x + y = "+str(sum))
add(4,5)

#print("x + y = "+(add(sum)))




def find_max(x,y):

	#maxnumber=max(x,y)
	print(str(x)+" = x and y ="+str(y))
	if (x > y):
		print(str(x)+" is greater than "+str(y))
	elif(y > x):
		print(str(y)+" is greater than "+str(x))
	else:
		print("0, both numbers are equal. \n")
	
	return(x,y);

x=input("Please enter a nubmer: \n")
y=input("Please enter another number: \n")
x=int(x)
y=int(y)
print(str(find_max(x,y)))

