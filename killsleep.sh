#!/bin/bash

sleep 30 &
SLEEPPID=$!
echo "PID " $SLEEPPID "is sleeping."
sleep 5
echo "PID " $SLEEPPID "is sleeping."
kill $SLEEPPID
