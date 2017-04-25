"""
To find the cuberoot of the entered number
"""

def cuberoot(n):
	if n > 0:
		return round((n ** (1./3.)))
	else:
		return round((-(-n) ** (1./3.)))

def main():
	x = int(input())
	print(int(cuberoot(x)))

if __name__ == "__main__":
	main()