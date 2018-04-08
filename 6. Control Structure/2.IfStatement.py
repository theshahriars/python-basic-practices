# If Satetment

# Example 1

if 5 > 4:
    print('5 is greater than 4')

if 5.1 > 5.0:
    print('5.1 is greater than 5.0')

# Nested if satetment

# Example 1

a = 7
b = 6
c = 1

if a > b:
    print('%s is greater than %s' % (a, b))
    if a > c:
        print('%s is greater than %s' % (a, c))

# Example 2

a = 10

if a > 5:
    print('a is greater than 5')
    if a < 20:
        print('a is between 5 and 20')