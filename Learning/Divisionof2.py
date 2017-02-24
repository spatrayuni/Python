"""
Task : You just need to take two numbers as input from stdin and you need to Divide them

Input Format : You will be taking two numbers as an input as an input from stdin one on each line respectively 

Output Format : You need to print the output of the division to stdout

if __name__ == "__main__":
	y = []
	for i in range(0,2):
		x = input() 
		if i == 0:
			y.append(x)
		else:
			sub = y[0] - x
	print "%s"%sub
"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT



''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
	y = []
	for i in range(0,2):
		x = input() 
		if i == 0:
			y.append(x)
		else:
			div = x / y[0]
	print "%s"%div
main()