"""This script is to give an example on the indexing of a string
Each string is a list for which we can run a loop or if u want to print only a specific characters
"""

import sys
if __name__ == "__main__":
	first_word = sys.argv[1]
	second_word = sys.argv[2]
	print "%s %s" %(first_word,second_word)

	first_letter = first_word[0]
	second_letter = second_word[0]
	print "%s%s" %(first_letter,second_letter)

	concated_letters = first_letter + second_letter
	print "%s" %(concated_letters)

	short_word = first_word[0:3] + second_word[0:]
	print "%s" %short_word