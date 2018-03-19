# Extending Lists

emptyList = []
anotherList = [1, 2, 3]
emptyList.extend(anotherList)
print(emptyList)

# Appending Lists

myList = [1, 2, 3]
myList.append(4)
print(myList)
myList.append(5)
print(myList)

# Index of list elements

myList = ['a', 'b', 'c', 'd', 'e']
print(myList.index('b'))
print(myList.index('e'))

# Inserting in list
myList = ['b', 'c', 'd', 'e']
index = 0
myList.insert(index, 'a')
print(myList)

# Max value in list
myList = [1, 2, 7, 9, 5, 6]
print(max(myList))

# Counting list elements
myList = [1, 2, 7, 9, 5, 6, 1, 2, 1, 5, 1]
print(myList.count(1))
print(myList.count(2))
print(myList.count(9))

# Length of list
myList = [1, 2, 7, 9, 5, 6, 1, 2, 1, 5, 1]
print(len(myList))

# Sorting list
myList = [5, 6, 1, 3, 7]
myList.sort()
print(myList)

