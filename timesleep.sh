#!/bin/bash

Date1=$(date +%s)
sleep 10
Date2=$(date +%s)

echo $((Date2-Date1))



