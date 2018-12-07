#sets_4.py jfj
alpha = {"a","b","c","d","e","f"}
bravo = {"z","y","x","w","v"}
charlie = alpha.union(bravo)
charlie.update("g","h","i","j","k")
for x in charlie:
	print(x," ",end="c")
print()
#popl all the records
for i in range(len(charlie)):
	print("pop ",i," ",end="")
	thepop = charlie.pop()
	print (thepop)
	
