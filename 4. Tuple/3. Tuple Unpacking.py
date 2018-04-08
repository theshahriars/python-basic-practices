# Unpacking tuples

# Example 1
a, b = ('a', 'b')
print(a)
print(b)

# Example 2

myTuple = (1, 3, 6, 2, 8)
a, b, c, d, e = myTuple
print(a)
print(b)
print(c)
print(d)
print(e)

# Example 3

myTuple = (1, 2, 3, 4, 5, 6, 7)
a, *b, c = myTuple
print(a)
print(b)
print(c)
