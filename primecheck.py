#!/usr/bin/python3

import os
import time
from multiprocessing import Process

def is_prime(num):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        return False
    else:
        return True

def count_primes_in_range(start, end):
  total = 0
  for x in range(start, end):
    if is_prime(x):
      total += 1



  return total



