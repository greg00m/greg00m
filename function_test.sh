#!/bin/bash

function add {
  echo $(($1+$2))
}

function multiply {
  echo $(($1*$2))
}




addresult=$(add $1 $2) 
multiplyresult=$(multiply $1 $2)

echo $addresult
echo $multiplyresult


#subshell method for factorial

function factorial {
	if [["$1" -eq "1"]];then  #better to use -eq than == 
	  echo "1"
	else
	  echo $(($1 * $(factorial $(($1 - 1)))))
	fi
}

ret=$(factorial 7)

echo "Factorial is $ret"


