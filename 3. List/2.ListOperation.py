# List element replace

myList = [1, 2, 3, 4]
print(myList)
myList[2] = 10
print(myList)

# Adding lists

myList1 = [1, 2, 3, 4]
myList2 = ['a', 'b']
myList3 = ["Python", "C#"]
extendedList = myList1 + myList2 + myList3
print(extendedList)

# List multiplication / List repeat

myList = [1, 2, 3]
multipliedList = myList * 5
print(multipliedList)

# List element check
myList = ['a', 'b', 'c', 'd', 'e']
print('a' in myList)
print('z' in myList)
print('y' not in myList)

# Deleting list element
myList = ['a', 'b', 'c', 'd', 'e']
del myList[2]
print(myList)