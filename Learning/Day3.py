#https://notes.pipal.in/2017/intuit/
#https://notes.pipal.in/2017/intuit/day3.html

"""
Other Trainings
https://notes.pipal.in/2016/intuit-israel/


https://notes.pipal.in/2016/spjain1/

https://notes.pipal.in/2016/spjain2/
"""




#Working with files

f = open("/csshx-master/temp")
print(f.read())

#Other way of writing this is
print(open("/csshx-master/temp").read())

#using readlines()
lines = open("/csshx-master/temp").readlines()
for line in lines:
	print(line)

#In the above code it will give empty lines, we can excluce it by using
lines = open("/csshx-master/temp").readlines()
for line in lines:
	print(line.strip("\n"))

print("\n")
#Other way of doing it 
lines = open("/csshx-master/temp").readlines()
for line in lines:
	print(line,end="")

"""
Problem: Write a program cat.py that takes a filename as command-line argument and prints all the contents of that file.
$ python cat.py three.txt
one
two
three
"""
print("\n")
import sys
path = sys.argv[1]
([print(line.strip("\n")) for line in open(path).readlines()])

#Another way to doing this
print("\n")
import sys
path = sys.argv[1]
print(open(path).read())


#Word Count
"""Program to compute line count, word count and char count of a file

Usage : python3 wc.py filename
"""

import sys
def linecount(f):
    return len(open(f).readlines())

def wordcount(f):
    return len(open(f).read().split())

def charcount(f):
    return len(open(f).read())

def main():
    f = sys.argv[1]
    print(linecount(f), wordcount(f), charcount(f), f)
    
if __name__ == "__main__":
    main()


import sys

def linecount(f):
	return len(open(f).readlines())

def wordcount(f):
	return len(open(f).read().split())

def charcount(f):
	return len(open(f).read())

if __name__ == "__main__":
	f = sys.argv[1]
	print(linecount(f),wordcount(f),charcount(f),f)

# Writing to files
f = open("a.txt","w")
f.write("one\n")
f.write("second\n")
f.close()
print(open("a.txt").read())

print("\n")
#Appending to an existing file
f = open("a.txt","a")
f.write("three\n")
f.close()
print(open("a.txt").read())

#With Statement

with open("b.txt","w") as f:
	f.write("another one\n")
	f.write("another second\n")
print(open("b.txt").read())


#Dictionaries
d = {"x": 1, "y": 2, "z": 3}
print(d)

person = {"name": "Alice", "email": "alice@example.com"}
print("name" in person)

#.get() function will give the value of the key if it is available otherwise it will give the default value which is defined after
#in the example "not provided" is the default value

print(person.get("phone", "not-provided"))
print(person.get("email", "not-provided"))


print("\n")
"""Program to compute frequency of words in a file.

USAGE: python wordfreq.py filename.txt
"""
import sys

def read_words(filename):
    return open(filename).read().split()

def wordfreq(words):
    """Computes the frequency of each word in the 
    given list of words.
    """
    freq = {}
    print(freq)
    for w in words:
        # if w in freq:
        #     freq[w] = freq[w] + 1
        # else:
        #     freq[w] = 1
        freq[w] = freq.get(w, 0) + 1
        print(w, freq)            
    return freq

def print_freq(freq):
    # TODO: improve this
    print(freq)

def main():
    filename = sys.argv[2]
    words = read_words(filename)
    freq = wordfreq(words)
    print_freq(freq)
    
if __name__ == "__main__":
    main()


#Classes
"""
The __init__ is a special method that is called to initialize the newly created object. Objects are created by calling the class like a function. It creates the object and initializes it by calling the __init__ method.
The __init__ is optional.
"""
class Point:
	def __init__(self,x ,y):
		self.x = x
		self.y = y
p = Point(3,4)
print(p.x,p.y)

"""
Problem: Add a method double to the above Point class. It should return a new point with both x and y coordinates doubled.
>>> p = Point(2, 3)
>>> p2 = p.double()
>>> p2.display()
4 6
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getx(self):
        return self.x
    
    def display(self):
        print(self.x, self.y)
        
    def add(self, p):
        x = self.x + p.x
        y = self.y + p.y
        return Point(x, y)

    def double(self):
    	x = self.x + self.x
    	y = self.y + self.y
    	return Point(x, y)
    
p1 = Point(1, 2)
p2 = Point(10, 20)
p3 = p1.add(p2)
p3.display()

p = Point(2, 3)
p2 = p.double()
p2.display()

print(p.__dict__)
p.z = 4
print(p.__dict__)
#Every variable that is being used in Python is nothing but a key value pair in the dictionary
# All the variables are stored in dictorary called globals

#Classes are nothing but glorified dictionaries too


x = 1
g = globals()

print(g['x'])

g['y']=2
print(y)


"""
Problem: Write a class Timer to measure the time taken in a task. The class should have start and stop methods and it should be able to find the time taken between then.
t = Timer()
t.start()
do_something()
t.stop()
print("Time taken:", t.get_time_taken())

Hint: see time.time()
"""
import time
class timer:
	def __init__(self):
		self.time_start = 0
		self.time_stop = 0

	def start(self):
		self.time_start = time.asctime().split()[3:4]

	def stop(self):
		self.time_stop = time.asctime().split()[3:4]

	def get_time_taken(self):
		return time_stop - time_start

def main()
	t = Timer()
	t.start()
	do_something(1000)
	t.stop()
	print("Time taken:", t.get_time_taken())

def do_something(n):
		for i in range(n):
        	for j in range(n):
            	x = i*j

if __name__ = "__main__":
	main()
