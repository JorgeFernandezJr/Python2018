#sets_1.py jfj
alpha = {"a", "bb", "ccc", "dddd", "eeeee", "ffffff"}
for x in alpha:
	#print(alpha[x]) #uncomment this line an try 
	print (x)
print(sorted(alpha))

"""
Look at what is going on here.
A set can not be indexed.
for x in alpha looks at all the elements in
the set and assigns one at a time to the x
variable.
The folowing is an excellent resource.
https://www.programiz.com/python-progamming
"""
