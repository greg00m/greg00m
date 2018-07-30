#!/bin/bash

Var1=3
Var2=7
Var3=$((Var1+Var2))
Var4=$((Var1*Var2))
Var5=$((Var1/Var2))
Var6=$((Var1**Var2))


echo $((Var3)) Var4 Var5 Var6
echo "$Var3 $Var4 $Var5 $Var6"
echo $((Var3+Var4-Var5**Var6))


