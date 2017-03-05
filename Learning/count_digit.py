"""
This script Counts the number of digits in a number\

Copyright : Santhosh Deepu Patrayuni
"""
import sys

def count_digit(number):
	return len(number)

def main():
	number = sys.argv[1]
	print("Number of digits in", number , "is :", count_digit(sys.argv[1]))

if __name__ == "__main__":
	main()
