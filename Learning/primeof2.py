"""
Objective : This challenge will help in getting familiarity with python, loops and operators which will be helpful when you solve further problems in techgig

Task : You just need to take two numbers as input from stdin and you need to find prime numbers between two numbers and print them

"""

def get_prime(x,y):
	prime_nums = []
	for i in range(x,y+1):
		flag = True
		for j in range(2,i):
			if (i % j) != 0:
				flag = True
			else:
				flag = False
				break
		if flag == True:
			print(i)


def main():
	x,y = int(input()), int(input())
	get_prime(x,y)

if __name__ == "__main__":
	main()