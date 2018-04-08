# Empty List

myList = []
print(myList)

myList = list()
print(myList)

# List with data

myList = [1, 2, 3]
print(myList)

myList = ['a', 'b', 'c', 'd']
print(myList)

myList = [1, 'b', 2, "python"]
print(myList)

# Nested list

numberList = [1, 2, 3]
alphabetList = ['a', 'b', 'c']
nestedList = [numberList, alphabetList]
print(nestedList)

# Retrieving data from list

numberList = [1, 2, 3]
myList = ["Python", 1, 'a', numberList]
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[3][0])
print(myList[3][1])
print(myList[3][2])
