# Stripping string

# Example one
string = "    Hello    "
strippedString = string.strip()
print(strippedString)

# Example two
string = "    Hello    "
strippedString = string.rstrip()
print(strippedString)

# Example three
string = "    Hello    "
strippedString = string.lstrip()
print(strippedString)

# Example four
string = "*****Hello*****"
strippedString = string.lstrip('*')
print(strippedString)

# Example five
string = "*****Hello*****"
strippedString = string.rstrip('*')
print(strippedString)

# Example six
string = "*****Hello*****"
strippedString = string.strip('*')
print(strippedString)
