#https://notes.pipal.in/2017/intuit/
#https://notes.pipal.in/2017/intuit/day1.html
"""Python Training
Day 1

"""
# Simple Print statement
name = "Santhosh"
print("My name is ", name)

#Entering text in multiple lines
text ="""This is s a good way to know if we 
can use multi line text
"""
print("\n",text)

#\n is used for new line and \t is used for tab
print("\nSanthosh\tDeepu\tPatrayuni\nMob:0000")

# Lists can contain lists and even dictionaries and its hetrogenous so we can include both integers adn strings
print("\nLists")
x=["a","b",5,[3,4]]
print(x[3][0])

print("\nLists in Lists")
matrix = [[1,2,3],[4,5,6],[7,8,9]]
column = [matrix[0][0],matrix[1][0],matrix[2][0]]
print(column)

#tuple is different from lists, they are used to represent constant variables
print("\nTuple")
yellow = (255,255,0)
r,g,b = yellow


#Dictionaries to represent Key Value pairs
print("\nDictionaries")
person = {"name":"Alice","email":"x@example.com"}
print(person['name'])

#Cant have duplicate keys in the dictionary
print ("\n")
x = {1,2,3,2,1}
print(x)

#Booleans and Special types are available
print("\nTrue\tFalse")
#None is a special character

#Functions
#print ane len are built-in functions
#Python doesn't support operations on incompatible datatypes
print ("\n")
x = "0947529084750928834750928347509283457"
print("Length of the number is ",len(str(x)))

# ** is used for doing the squares
print ("\n",2**3)

#Custom Functions
#it takes 4 spaces for indentation
x = 4
def square(x):
	y = x * x
	return y
y = square(x)
print("\nSquare of ",x,"is",y)
print("\n",square(5))

def cube(x):
	y = x ** 3
	return y
print("\n",cube(5), cube(10))


def count_digits(x):
	return len(str(x))
print("\nLength of the Variable is ",count_digits(230495823245234))


def squarecube(x):
	s = x * x
	c = x ** 3
	return s,c
x = squarecube(3)
print(x)
print("\nSquare of 3 ",x[0],";Cube of 3",x[1])

# Print vs Return
# if the function is returing it can be use to do further actions however if its only printing then we can reuse it further
def square1(x):
	return x*x

def square2(x):
	print(x*x)

print("\nPrint vs Square",square1(square1(4)),"\n")
square2(4)

# Calling functions as arguments inside another function
def square(x):
	return x*x
def sum_of_squares(x,y):
	return square(x) + square(y)
print("\n Sum of squares output",sum_of_squares(3,4))

def cube(x):
	return x ** 3
def sum_of_cubes(x,y):
	return cube(x)+cube(y)
print("\n Sum of cubes output",sum_of_cubes(3,4))

def sum(f,x,y):
	return f(x) + f(y)

print("\nSum of Squares",sum(square,3,4))
print("Sum of cubes",sum(cube,3,4))

#max is a function
print("\nMax of 2 and 3 is ",max(2,3))
#Using max with strings
print("\nMax of Strings",max("one","two","three","four","five"))
#The above function compares using dictionary ordering and will return "two" 
print("\nMax of Strings",max(("one","two","three","four","five"),key=len))
#The above function will return "three"

print("\nMin of Strings",min(("one","two","three","four","five"),key=len))

# Counting the number of zeros
def count_zeros(x):
	return str(x).count("0")

print("\nCounting Zero",count_zeros(100))

#Methods
sentence = "this is a way to go in Python"
print(sentence.upper())
print((sentence.upper()).lower())

x = "one two three, four five"
print("\n",x.split())
print(x.split(","))

def count_of_words(x):
	return len(x.split())

def longest_of_words(x):
	return max(x.split(),key=len)

print("\nCount of words",count_of_words("life is suffering"))
print("\nLongest of words",longest_of_words("one two three four five"))

# import statement ikports a module and allows us to tcall functions defined in that
import time
print("\n",time.asctime())

from time import asctime
print(asctime())

t = time
print(t.asctime())

#List of all the files in the directory
import os
print("\n",os.getcwd())
print(os.listdir)

#Number of files in the current directory
def count_of_files(x):
	return len(os.listdir(x))

print("\nCount of files in current directory",count_of_files("."))
print("\nCount of files in /tmp",count_of_files("/tmp"))

#Size of file
print(os.path.getsize("Day1.py"))

#Largest of all files in the current directory
#max(values,key=function)
print(max(os.listdir("."),key=os.path.getsize))

#Dir is a built-in function
print("\n",dir(time))

import multiprocessing
print("\n",dir(multiprocessing))
print("CPU count is ",multiprocessing.cpu_count())
print("CPU count using OS module is ",os.cpu_count())

# Random module will give random values
import random
print(random.choice(["one","two","three","four","five"]))

#Print Randomly the prefix value 
def say_hello(name):
	x = random.choice(["Picha","arrey","dashga"])
	return x+" "+name

print(say_hello("Santhosh"))

#Printing both Prefix and Suffix randomly
def say_hello(name):
	x = random.choice([("Namaskar","Ji"),("Namaskaram","Garu"),("Namaskara","Avure"),("Ram Ram","Sahib")])
	print(x[0], name, x[1])

say_hello("santhosh")

# Command line arguments
# the 'sys' module keeps in the command line arguments in a special variable argv
# First element in the list is always Program name
# Remember that Arguments are always strings
print("\n")

#Input "python3 Day1.py Deepu SAnthosh"
import sys
print(sys.argv)
print(sys.argv[1],"  ",sys.argv[2])

#Square of the argument being passed
#Input "python3 Day1.py Deepu SAnthosh 4
print(int(sys.argv[3])*int(sys.argv[3]))

#Add the sum of command line arguments
print(int(sys.argv[3])+int(sys.argv[4]))

# Conditional Expressions
# >
# <
# and
# in
# not in

#Strings have other useful methods
# startswith()
# endswith()

t = 30
print(t==30)
print(31>t)

vowels = ['a','e','i','o','u']
def is_vowel(x):
	return x in vowels

print(is_vowel("t"))