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
		return self.time_stop - self.time_start

def main():
	t = Timer()
	t.start()
	do_something(1000)
	t.stop()
	print("Time taken:", t.get_time_taken())

def do_something(n):
	for i in range(n):
		for j in range(n):
			x = i*j

if "__name__" == "__main__":
	main()