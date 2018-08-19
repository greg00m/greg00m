#!/usr/bin/python3



file_path = "pretend_data.csv"
infile = open(file_path) #Defaults to read mode

count=0
sum=0
max=0
min=0

for line in infile:
	line = line.strip()
	grades = line.split(",")
	count=count+1
	sum=sum+int(grades[1])
	print("%d" %(int(grades[1])))
	if int(grades[1]) > int(max):
		max = grades[1]
	if int(grades[1]) < int(min):
		min = grades[1]
infile.close()

avg=sum/count
print(" ")
print("%.2f" %(avg))
print(max)
print(min)




