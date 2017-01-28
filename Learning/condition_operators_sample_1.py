""" This example is about the conditions along with different operators
There are six:

Equal to (==)
Not equal to (!=)
Less than (<)
Less than or equal to (<=)
Greater than (>)
Greater than or equal to (>=)

We will try to use most of them in this example"
"""
import sys

if __name__ == "__main__":
	if sys.argv[1] == sys.argv[2]:
		print "Both are same and the number is %s" %sys.argv[1]
	elif sys.argv[1] != sys.argv[2]:
		print "Both are different numbers %s %s" %(sys.argv[1],sys.argv[2])
	if sys.argv[1] < sys.argv[2]:
		print "%s is less than %s or we can say %s is greater than %s" %(sys.argv[1], sys.argv[2], sys.argv[2], sys.argv[1])
	if sys.argv[1] > sys.argv[2]:
		print "%s is less than %s or we can say %s is greater than %s" %(sys.argv[2], sys.argv[1], sys.argv[1], sys.argv[2])
