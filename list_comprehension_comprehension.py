#!/usr/bin/python3

#to use the "random" function in randlist
import random

randlist=[random.randint(1,100) for x in range(1,1000)]

divby7list=[x for x in randlist if x%7==0]
divby8list=[x for x in randlist if x%8==0]

print(len(divby7list))
print(len(divby8list))


mystring="There once was a dog named Rogerrr. He was a good boy, but his bite was worse than his bark!"


listofr=[x for x in mystring.split(" ") if "r" in x]
print(listofr)
print(mystring)
