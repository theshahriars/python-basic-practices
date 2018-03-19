# String formatting or String substitution

# First example
language = "Python"
print("%s is my favourite programming language." % language)

# Second example
food = "Biryani"
string = "I love %s."
print(string % food)

# Third example
food = "Biryani"
language = "Python"
string = "I love %s & %s." % (food, language)
print(string)

# Fourth example
floatString = "Float string: %f" % (2.83)
print(floatString)

# Fifth example
floatString = "Float string: %0.2f" % (2.83)
print(floatString)

# Another formatting method

# Some examples
print("%(lang)s is fun!" % {"lang":"Python"})
print("%(message)s! this is a %(message)s alert." % {"message":"success"})
print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2, "z":3})

# Another example
string = "My name is {0} {1}" . format("Shahriar", "Shabbir")
print(string)

# This is the last example
xy = {"x": 10, "y": 20}
string = "Value of x-coordinate is: {x} and y-coordinate is: {y}" . format(**xy)
print(string)