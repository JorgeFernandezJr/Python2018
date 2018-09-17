# find-factors.py jfj
def factors(b):
	
	for i in range(1, b+1):
		if b % i == 0:
			print(i)

if __name__ == '_main_':
	b = input(25)
	b = float(b)
	
	if b > 0 and b.is_integer():
		factors(int(b))
else:
	print("15*5")
	
