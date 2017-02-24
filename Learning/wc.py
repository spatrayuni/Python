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