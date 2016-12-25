#This script is about using the string methods
import sys

if __name__ == "__main__":
	first_word = sys.argv[1]
	second_word = sys.argv[2]

	CAPITAL = first_word.upper() + " " + second_word.upper()
	lower = CAPITAL.lower()
	lenght = length(lower)

	values = [CAPITAL,lower,lenght]
	print "%s" %values
