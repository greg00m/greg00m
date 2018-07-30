#!/usr/bin/python3

userinput1=input("Please enter a number from 1 to 100: \n")
userinput2=input("Please enter another number from 1 to 10: \n")
userinput1=int(userinput1)
userinput2=int(userinput2)

if userinput2<userinput1:
	print(str(userinput2)+" is smaller than "+str(userinput1)+", enter another number. \n")
	userinput2=int(input("Please enter another number from 1 to 100: \n"))
numdict={}
	#or numdict{}=dict(), this is the explicit constructor

numdict[4]=set()
numdict[7]=set()
numdict["4or7"]=set()

for x in range(userinput1,userinput2):
	if x%4==0 and x%7==0:
		numdict["4or7"].add(x)
			
	elif x%4==0:
		numdict[4].add(x)
	elif x%7==0:
                numdict[7].add(x)

print(numdict)

