#!/usr/bin/python3

file_path = "alice.txt" #opens a text file for reading

try:
	fh = open(file_path, 'r')
	for line in fh:
		sys.stdout.write(line)

except Exception:
	print("unable to open the file")

fh.close()
