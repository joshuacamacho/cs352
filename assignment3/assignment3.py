import random

ints = []
for x in range(20):
	ints.append(random.randint(10,100))
print(ints)

floats = []

for x in range(20):
	floats.append(random.uniform(10.0,80.0))
print(floats)

def formatPoly(pair):
	sign = "" if pair[0]< 0  else "+"
	mult = str(pair[0])
	mid = "x" if pair[0] != 0 else ""
	end = "^" + str(pair[0]) if pair[0] != 1 else ""
	return sign + mult + mid + end + " "

def writePoly(listSet):
	full = ""
	for item in listSet:
		full += formatPoly(item)
	print( full if len(full) > 0 and full[0]=='-' else full[1:])

writePoly([])
writePoly([[2, 1], [1, 0]])
writePoly([[3, 2], [-1, 0]])
writePoly([[5, 2], [-4, 1], [1, 0]])
writePoly([[7, 14], [11, 13], [-3, 2], [7, 1], [-5, 0]])
writePoly([[1, 0], [2, 1], [-5, 3], [-3, 1], [7, 0]])               
