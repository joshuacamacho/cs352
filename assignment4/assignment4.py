def count(theList):
	if len(theList) == 0:
			return 0
	if not isinstance(theList[0],(list,)):
		if len(theList) == 1:
			if str(theList[0]).isdigit():
				return 1
			else:
				return 0
		if str(theList[0]).isdigit():
			return 1 + count(theList[1:])
		else:
			return count(theList[1:])
	else:
		if len(theList) == 0:
			return 0
		else:
			return count(theList[0]) + count(theList[1:])

print(count([]))
print(count([3]))
print(count(['a']))
print(count([5, 1, 'a', 4]))
print(count([[1, 1], ['a'], 7, ['b', [3]]]))


def pal(theList):
	if not isinstance(theList,(list,)):
		return False
	listLength = len(theList) 
	if listLength == 0:
		return False
	elif listLength == 1:
		return True
	elif listLength == 2:
		return theList[0] == theList[1]
	return theList[0] == theList[listLength-1] and pal(theList[1:listLength-1])
print('\n\n\n')
print(pal([]))
print(pal('a'))
print(pal(['a']))
print(pal(['a', 'b', 'c', 'b', 'a']))
print(pal(['a', 'b', 'c', 'c', 'b', 'a']))
print(pal(['a', 'b', 'c', 'a']))
print(pal(['a', 'b', 'd', 'e', 'f', 'f', 'c', 'b', 'd', 'a']))
print(pal([['a', 'b'], ['b', 'a']]))

def pali(theList):
	if not isinstance(theList,(list,)):
		return False
	listLength = len(theList)
	if listLength == 0:
		return False
	mid = listLength // 2
	for top in theList[0:mid]:
		for bottom in theList[mid+1: listLength-1]:
			if(top != bottom):
				return False
	return True
print("\n\n\n")
print(pali([]))
print(pali('a'))
print(pali(['a']))
print(pali(['a', 'b', 'c', 'b', 'a']))
print(pali(['a', 'b', 'c', 'c', 'b', 'a']))
print(pali(['a', 'b', 'c', 'a']))
print(pali(['a', 'b', 'd', 'e', 'f', 'f', 'c', 'b', 'd', 'a']))
print(pali([['a', 'b'], ['b', 'a']]))