#!/usr/bin/python3

alist="this,is,a,list,5"
newlist=alist.split(",")
print(newlist)
print(" ".join(newlist))
print("%d"%(newlist[4]))
#will generate an error because we are trying to print a string as a number



