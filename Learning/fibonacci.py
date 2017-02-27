"""
Objective : This challenge will help you in getting familiarity with python, loops and operators which will be helpful when you will solve 
further problems on Techgig

Task : You just need to take a number as input from stdin which will tell how many terms of fibonacci needs to be printed

"""


def fibonacci(n):
	fibo = []
	for i in range(n):
		if i ==0 or i==1:
			fibo.append(i)
		else:
			fibo.append(fibo[i-1] + fibo[i-2])
	return fibo


def main():
	number = int(input())
	print(" ".join([str(i) for i in fibonacci(number)]))


if __name__ =="__main__":
	main()