#!/usr/bin/python3

mylist=[9,7,3]

mapped_list=list(map(lambda x: list(range(x, -1, -1)), mylist))

print(mapped_list)
