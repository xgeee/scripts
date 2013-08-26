#!/usr/bin/env python
from sys import argv
if len(argv) != 3:
	exit("USAGE : " +argv[0]+ " <CHARSET> <NBCHARS>\nEx: " +argv[0]+ " ab 4")
w=list(argv[1][0]*int(argv[2]))
print "".join(w)
def n(s, d):
	try:
		s[d] = argv[1][argv[1].index(s[d])+1]
		return s
	except:
		s[d] = argv[1][0]
		return n(s,d+1)
while True:
	try:
		print "".join(n(w,0))
	except:
		break


		


