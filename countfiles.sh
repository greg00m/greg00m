#!/bin/bash

count=0
for i in $(ls); do
	count=$((count+1))
done

if [[ $count -gt 10 ]];then echo "More than 10 files."
elif [[ $count -lt 10 ]];then echo "Less than 10 files."
else echo "Correct number of files found."
fi

#better way
#ls | wc -1
