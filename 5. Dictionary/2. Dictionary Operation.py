# Get values from dictionary

myDict = {"a": 1, "b": 2, "c": 3}
print(myDict['a'])
print(myDict['b'])

myDict = {"a": {"book": "Automate the boring stuff with python", "language" : "Python"}, "b": 2, "c": [1, 2, 3]}
print(myDict)
print(myDict['a'])
print(myDict['a']['book'])
print(myDict['a']['language'])
print(myDict['b'])
print(myDict['c'])
print(myDict['c'][0])
print(myDict['c'][1])
print(myDict['c'][2])

# Deleting dictionary element

myDict = {"a": {"book": "Automate the boring stuff with python", "language" : "Python"}, "b": 2, "c": [1, 2, 3]}
del myDict['a']
print(myDict)