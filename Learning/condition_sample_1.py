# This is a sample if else condition example
import sys

if __name__ == "__main__":
	if sys.argv[1] == "True" or sys.argv[1] == "T":
		print "You are right"
	elif sys.argv[1] == "False" or sys.argv[1] == "F":
		print "You are wrong"
	else:
		print "Wrong entry"