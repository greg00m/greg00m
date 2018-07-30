#!/bin/bash


infile="alice.txt"
while read line; do
	thecount=$(echo $line | grep -o "the" | wc -l)

if [[ "$thecount" -ge "1" ]]; then echo $line
fi

done < $infile

