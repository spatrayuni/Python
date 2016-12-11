import sys
import socket

def lookup(name):
	print name
	hostip = socket.gethostbyname_ex(name)
	print "%s - %s" %name

if __name__ == '__main__':
	with open(sys.argv[1],'r') as f:
		for line in f:
			lookup(line)

