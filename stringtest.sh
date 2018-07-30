#!/bin/bash

var1=$1
var2=$2
var3=$#

if [[ "$var3" -eq "2" ]]; then echo "Sufficient arguments exist"
else echo "Not enough arguments."
exit

fi

if [[ "$var1" == "$var2" ]]; then echo "$var1 is equal to $var2"
elif [[ "$var1" > "$var2" ]]; then echo "$var1 is greater than $var2"
else echo "$var1 is greater than $var2"

fi




