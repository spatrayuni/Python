#https://notes.pipal.in/2017/intuit/
#https://notes.pipal.in/2017/intuit/day2.html#Modifying-and-Growing-Lists
# input python3 Day2.py 32 42 4 .

#If Statement
n = 35
if n % 2 ==0:
	print("even")
else:
	print("odd")


def check_even(n):
	if n % 2 ==0:
		print("even")
	else:
		print("odd")

import sys
check_even(int(sys.argv[1]))

#multiple conditions can be done using elif statements

def check_number(n):
	if n < 0:
		print("\n",n," is a minus number")
	elif n < 10:
		print(n," is a single digit number")
	elif n < 100:
		print(n," is a two digit number")
	else:
		print(n," is a big number")

check_number(int(sys.argv[1]))

"""
Problem: Write a function minimum to compute the minimum of two numbers, without using the built-in function min. Please note that the function should return a value, not print.
>>> minimum(3, 7)
3
>>> minimum(33, 7)
7
>>> 1 + minimum(3, 7)
4
>>> 1 + minimum(3, 3)
4    
Problem: Write a function minimum3 to compute minimum of three numbers. Can you do this by using the minimum function defined above?
>>> minimum3(2, 3, 4)
2
>>> minimum3(12, 3, 4)
3    
>>> minimum3(12, 13, 4)
4 
"""

def min_number(x,y):
	if x < y:
		return x
	else:
		return y

print("\nMinimum between of ",sys.argv[1]," and",sys.argv[2],"is ",min_number(int(sys.argv[1]),int(sys.argv[2])))
print(1+min_number(int(sys.argv[1]),int(sys.argv[2])))

def min_number_3(x,y,z):
	if x < y:
		if x < z:
			return x
		else:
			return z
	else:
		if y < z:
			return y
		else:
			return z

def min_number_3_1(x,y,z):
	if z < min_number(x,y):
		return z
	else:
		return min(x,y)

def min_number_3_2(x,y,z):
	return min_number(z,min_number(x,y))

print("\nMinimum between of ",sys.argv[1],",",sys.argv[2]," and",sys.argv[3],"is ",min_number_3(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
print(1+min_number_3(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))

print("\nMinimum between of ",sys.argv[1],",",sys.argv[2]," and",sys.argv[3],"is ",min_number_3_1(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
print(1+min_number_3_1(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))

print("\nMinimum between of ",sys.argv[1],",",sys.argv[2]," and",sys.argv[3],"is ",min_number_3_2(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
print(1+min_number_3_2(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))

# For Loop in lists
print("\n")
names = ["rajesh","neha","anand","santhosh"]

for name in names:
	print(name)

sentence = "when in doubt, use brute force"

for word in sentence.split():
	print(word)


"""
Problem: Write a program ls.py that takes path to a directory as command-line argument and prints all the files in that directory. The output should contain one filename per line.
$ python ls.py .
Makefile
day1.ipynb
day1.html
hello.py
Hint: see os.listdir
"""
import os
def ls(location):
	for file in os.listdir(location):
		print(file)

ls(sys.argv[4])


print("\n\n")
# List the files only which has .py extension
import os
def ls(location):
	for file in os.listdir(location):
		if ".py" in file:
			print(file)
ls(sys.argv[4])

#One more way to do the above example
print("\n\n")
import os
def ls(location):
	for file in os.listdir(location):
		if file.endswith(".py"):
			print(file)

ls(sys.argv[4])

#Range is a built-in function used normally in For loop to loop for a number of times

print("\n\n")
# List the files only which has .py extension
def range_example(n):
	for i in range(5):
		print("hello",n)

range_example("santhosh")

#Python has a built-in function sum to compute sum of a list of numbers.
#sum([1, 2, 3, 4, 5])
#sum(range(10))

def my_sum(numbers):
    result = 0
    print("result =", result)
    for n in numbers:
        result = result + n
        print("n =", n, "result =", result)
    return result

print(my_sum([10, 20, 30, 40, 50]))
# print(my_sum(range(10)))
# print(my_sum(range(1000000)))

#Write a function product to compute product of given list of numbers.
"""
Problem: Write a function product to compute product of given list of numbers.
>>> product([1, 2, 3, 4])
24
"""
print("\n")
def product(x):
	sum = 1
	for y in x:
		sum = sum * y
	return sum
print(product([1,2,3,4]))

"""
Problem: Write a function factorial that takes a number as argument and computes its factorial. Can you use the above implementation of product in computing it?
>>> factorial(4)
24
"""
print("\n")
def factorial(x):
	if x <0:
		print("This is a minus number")
	else:
		fact = 1
		for i in range(1,x+1):
			fact = i * fact
	return fact
print(factorial(5))

#using product fucntion
# Always try to reuse code
def factorial_1(n):
	return product(range(1,n+1))
print(factorial_1(int(sys.argv[3])))

#Modifying and Growing Lists
names.append("Shiva")
print(names)

#Let us write a function squares to compute squares of all numbers in a list.
def square(n):
	result = []
	for i in n:
		result.append(i*i)
	return result
print(square([1,2,3]))
print(sum(square([1,2,3])))

"""
Write a function evens that takes a list of numbers as argument and returns a new list containing only the even numbers out of them.
>>> evens([1, 2, 3, 4, 5, 6])
[2, 4, 6]
"""
def even(n):
	even_n = []
	for i in n:
		if i % 2 == 0:
			even_n.append(i)
	return even_n
print(even([1,2,3]))

# List Comprehensions
#[expression for var in a list if condition]
x = [1,2,3,4,5,6]
print([a*a for a in x])
print([a*a for a in x if a%2 == 0])

"""
Problem: Write a function list_pyfiles that takes path to a directory as argument and returns all the python files in that directory.
>>> list_pyfiles(".")
['echo.py', 'square.py', ...]
"""
import os
def list_files(path):
	return [file for file in os.listdir(path) if file.endswith(".py")]
print(list_files(sys.argv[4]))

#How to find total size of all python files in the current directory?
print("\n")
def size_of_all_files(path):
	return sum([os.path.getsize(f) for f in os.listdir(".") if f.endswith(".py")])
print(size_of_all_files(sys.argv[4]))


# Iterating over a sequence of values
for i in range(2, 5):
    print(i, i*i)

#Iterating over two lists together
names = ["a", "b", "c", "d"]
scores = [10, 20, 30, 40]
#Zip will go through both the list and make a list of tuples by combining both first and second list
for name, score in zip(names, scores):
    print(name, score)

for pair in zip(names, scores):
    print(pair)

"""
Problem: Write a function vector_add to add two vectors.
>>> vector_add([1, 2, 3, 4], [10, 20, 30, 40])
[11, 22, 33, 44]
"""
x=[1,2,3,4]
y=[10,20,30,40]
def vector_add(x,y):
	return [a+b for a,b in zip(x,y)]
print(vector_add(x,y))

# Iterating over the index and the value together
#enumerate will give index and value of the list
names = ["a", "b", "c", "d"]
list(enumerate(names))
"""
Output:
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
"""


chapters = ["Getting started", "Lists", "Working with Files"]

for i, title in enumerate(chapters):
    print("chapter", i+1, ":", title)
"""
Output:
chapter 1 : Getting started
chapter 2 : Lists
chapter 3 : Working with Files
"""
print("\n")
for i, title in enumerate(chapters, start=1):
    print("chapter", i, ":", title)
"""
Output:
chapter 1 : Getting started
chapter 2 : Lists
chapter 3 : Working with Files
"""

## List indexing
# -1 is the index of last element in the list, similary -2 will be last by one element in the list and so on and so forth

def get_ext(path):
	return path.split(".")[-1]
print(get_ext("a.py"))
print(get_ext("a.tar.gz"))

def get_ext_1(path):
	return [file.split(".")[-1] for file in os.listdir(path)]
print(get_ext_1(sys.argv[4]))

#Earlier we wrote a program echo.py to print the first command-line argument. Let us improve that to print all command-line arguments.

import sys
print(sys.argv)

args = sys.argv[1:] # skip the program name
print(args)

print(" ".join(args))
"""
output
!python echo2.py hello world
['echo2.py', 'hello', 'world']
['hello', 'world']
hello world
"""


"""
Problem: Write a program sum.py that takes multiple numbers as command-line arguments and prints their sum.
$ python sum.py 1 2 3
6
$ python sum.py 1 2 3 4 5
15
"""
print(sum([int(arg) for arg in sys.argv[1:-1]]))

#Example of sorted function
files = os.listdir(".")
fieles2 = sorted(files,key=os.path.getsize)
print(fieles2)

# Input # python3 Day2.py 32 42 4 .


































































