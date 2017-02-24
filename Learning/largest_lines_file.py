import os
import wc

files = [f for f in os.listdir(".") if f.endswith(".py")]
print(max(files,key=wc.linecount))