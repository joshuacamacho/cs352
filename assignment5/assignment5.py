from functools import reduce
#problem 1

def listAdd(a, b):
	if len(a) > 0 and len(b) > 0:
		return [ a[0]+b[0] ] + listAdd(a[1:],b[1:])
	elif len(a) > 0:
		return a
	elif len(b) > 0:
		return b
	else:
		return []

print(listAdd([3,1,4],[8,2,5]))
print(listAdd([3,1,4],[2,2]))
print(listAdd([3,1,4],[]))

#problem 2
def intersection(a, b):
	if len(a) > 0:
		return [a[0]] + intersection(a[1:],b) if a[0] in b else intersection(a[1:],b)
	else:
		return []

print('\n')
print(intersection([4,1,2],[2,5,3,1,7]))
print(intersection([4,1,2],[]))

#problem 3
def none(a):
	if len(a) > 0:
		if a[0] % 2 == 0:
			return listAdd([0,1], none(a[1:]))
		else:
			return listAdd([1,0], none(a[1:]))
	else:
		return [0,0]
print('\n')
print(none([]))
print(none([3]))
print(none([2]))
print(none([3,1,4,1,5,6]))

#problem 5
def opSome(cond, op, a):
	return list(map((lambda x: op(x) if cond(x) else x), a))

print('\n')
print(opSome((lambda x: x % 2 == 1), (lambda x: x * x), []))
print(opSome((lambda x: x % 2 == 1), (lambda x: x * x), [2]))
print(opSome((lambda x: x % 2 == 1), (lambda x: x * x), [3]))
print(opSome((lambda x: x % 2 == 1), (lambda x: x * x), [3,6,4,5,2]))

#output
# [11, 3, 9]
# [5, 3, 4]
# [3, 1, 4]


# [1, 2]
# []


# [0, 0]
# [1, 0]
# [0, 1]
# [4, 2]


# []
# [2]
# [9]
# [9, 6, 4, 25, 2]