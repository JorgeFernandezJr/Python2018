# multiplication.py jfj

def multi_table(a):
	for i in range(1, 11):
		print('{0} x {1}'.format(a, i, a*i))

if __name__ == '_main_':
	a = input('Enter a number: ')
	multi_table(float(a))
