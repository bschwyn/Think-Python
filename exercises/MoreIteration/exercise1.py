#More Iteration Exercise 1

#Add a print function to Newton's *sqrt* function that prints out *better* each time it is calculated.
#Call your modified function with 25 as an argument and record the results.

def sqrt(n, howmany):
	approx = 0.5*n
	print(n)
	print(approx)
	for i in range (howmany):
		better = 1/2 *(approx + n/approx)
		print(better)
	return better
print(sqrt(25,10))
	
