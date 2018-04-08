# If-else Satetment

# Example 1

a = 5
b = 6

if a > b:
    print('%s is greater than %s' % (a, b))
else:
    print('%s is less than %s' % (a, b))

# Example 3

print('Please input first number: ')
a = input()
a = int(a)

print('Please input second number: ')
b = input()
b = int(b)

if a > b:
    print('%s is greater than %s' % (a, b))
else:
    print('%s is greater than %s' % (a, b))

# Nested if-else

# Example 1

print('Please input first number: ')
a = input()
a = int(a)

print('Please input second number: ')
b = input()
b = int(b)

if a > b:
    print('%s is greater than %s' % (a, b))
    # Nested if-else block
    if a > 5:
        print('%s is greater than 5' % a)
    else:
        print('%s is less than 5' % a)
else:
    print('%s is greater than %s' % (a, b))
    # Nested if-else block
    if b > 5:
        print('%s is greater than 5' % b)
    else:
        print('%s is less than 5' % b)
