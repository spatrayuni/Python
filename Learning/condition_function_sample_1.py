# This example uses conditions and definitions

import sys

def equal():
	return "Numbers are equal"

def notequals():
	return "Numbers are different"

def lessthans():
	return "First number is less than second number"

def greaterthan():
	return "First number is greater than first number"

def lessthanequal():
	return "First number is either equal or less than second number"

def greaterthanequal():
	return "First number is either equal or greater than second number"


if __name__ == "__main__":
	first = sys.argv[1]
	second = raw_input("Enter the Second value : ")

	print "%s %s" %(first,second)
	if (first == second):
		print equal()
		if (first <= second):
			print greaterthanequal()
		elif (first >= second):
			print lessthanequal()

	if (first != second):
		print notequals()
		if (first < second):
			print lessthans()
		elif (first > second):
			print greaterthan()
