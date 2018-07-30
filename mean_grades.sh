#!/bin/bash
count=0
sum=0
infile="pretend_data.csv"
while read line; do
#cut -d "," -f 1 would retrieve the name
#use if statement to check lowest/highest score and name
	num=$(echo $line | cut -d "," -f 2) 
	echo $line
	#echo $num
	sum=$(echo "$sum+$num" | bc -l)
	count=$((count+1))
		
	echo $mean
done < $infile

mean=$(echo "scale=2;$sum/$count" | bc -l)
echo $mean
