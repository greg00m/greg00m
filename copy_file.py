#!/usr/bin/python3

file_path = "alice.txt"

try:
	fh = open(file_path, 'r') #open text file for reading
except Exception:
	print("unable to read file")

try:
	out_file = "%s.out" % (file_path) #opens text file for writing
	fh = open(file_path, 'w') #opens text file for writing
except Exception:
	print("unable to write to file")

try:
	fh = (file_path, 'r+') #opens file for read/write

except Exception:
	print("unable to add read to file attribute")

try:
	open(file_path, 'rb') #opens a binary file for reading

	fh.close()
except Exception:
	print("uanble to open a binary file for reading")



#open("copy.txt","w").write(open("alice.txt","r").read()


