def copy_file(source_file,dest_file):
	with open(dest_file,"w") as f:
		f.write(open(source_file).read())

if "__name__" == "__main__":
	copy_file(sys.argv[1],sys.argv[2])