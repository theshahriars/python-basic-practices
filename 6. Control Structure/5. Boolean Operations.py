# Boolean operations

# Boolean logic - Simple Example

print(1 == 1 and 2 == 2) # true

print(1 != 2 and 2 == 2) # true

print(1 == 2 and 2 == 2) # false

print(1 == 2 or 2 == 2) # true

print(not 1 == 2) # true

print(not 1 == 1) # false

print(not 1 != 1) # true

print(not 1 > 7) # true

# Example 1

a = 4
b = 5

if a > 5 or b < 10:
    print('The statement is true')
else:
    print('The statement is false')

# Example 2

a = 4
b = 5

if a > 5 and b < 10:
    print('The statement is true')
else:
    print('The statement is false')

# Example 3

a = 10
b = 10

if a == 10 and b == 20:
    print('The statement is true')
else:
    print('The statement is false')

# Example 4

a = 10
b = 10

if a == 10 or b == 20:
    print('The statement is true')
else:
    print('The statement is false')

# Example 5

a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 5

if a not in a_list:
    print('%s is not in the list' % a)
else:
    print('%s is in the list' % a)

# Example 6

a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 15

if a not in a_list:
    print('%s is not in the list' % a)
else:
    print('%s is in the list' % a)
