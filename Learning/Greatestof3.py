#Greatest Of 3 With Python

if __name__ == "__main__":
	print "Enter 3 Numbers for which you need to know the Greatest : "
	Great = 0
	y = []
	for i in range(0,3):
		print i
		x = raw_input("Enter value : ")
		y.append(x)
		if Great < y[i]:
			Great = y[i]

print "Greatest among %s %s %s numbers is %s " %(y[0],y[1],y[2],Great)