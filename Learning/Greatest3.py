''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

"""
Objective : This challenge will help you in getting familiarity with Python languages and operators which will be helpful when you solve further problems on Techgig

Task : You just need to take three number as input from stdin and you need to find greatest of them

Input : You will be taking three numbers as an input from stdin one on each line respectively

Output : You need to print the greatest of the three numbers to the stdout
"""

 """"
if __name__ == "__main__":
	greatest = 0
	for i in range(0,3):
		x = input("Enter Value :")
		if greatest < x:
			greatest = x

print "Greatest number is %s" %greatest"""

def main():
	greatest = 0
	for i in range(0,3):
		x = input()
		if greatest < x:
			greatest = x
	print "%s" %greatest 
main()

