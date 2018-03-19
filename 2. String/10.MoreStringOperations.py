# Replacing string

# Example one
string = "Hello World"
replacedString = string.replace("Hello", "My")
print(replacedString)

# Example two
string = "*****Hello*****"
replacedString = string.replace('*', '-')
print(replacedString)

# Joining array elements
array = ["one", "two", "three"]
string = ",".join(array)
print(string)

# Splitting string into array elements
string = "one,two,three"
array = string.split(",")
print(array)
