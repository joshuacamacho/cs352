print("Problem 1")
print("Max []: Error") # max([])
print("Max [3]:", max([3]) )
print("Max [5,2,8]:", max([5,2,8]) )
print("Max [2,4,8,1,6]:", max([2,4,8,1,6]) )

print("Problem 2")
print("Method 1")
a = list(range(1,200,3))
print(a)

print("Method 2")
b = []
for i in range(1,200,3):
	b.append(i)
print(b)

print("Method 3")
c = [i for i in range(1,200,3)]
print(c)