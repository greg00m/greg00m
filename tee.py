#!/usr/bin/python3

import sys

filelist=[]
for f in range(1, len(sys.argv)):
                fh = open(sys.argv[f], "w")
                filelist.append(fh)

for line in sys.stdin:
	sys.stdout.write("%s" %(line))
	for fh in filelist:
		fh.write("%s" %(line))

for fh in filelist:
	fh.close()






