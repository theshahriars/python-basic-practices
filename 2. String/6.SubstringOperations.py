# Finding substring on starting of a string

# Example one
string = "Hello World"
substring = string.startswith("Hello")
print(substring)

# Example two
string = "Hello World"
substring = string.startswith("Bello")
print(substring)

# Finding substring on ending of a string

# Example one
string = "Hello World"
substring = string.endswith("World")
print(substring)

# Example two
string = "Hello World"
substring = string.endswith("Mars")
print(substring)

# Finding substring on a string

# Example one
string = "Hello World"
substring = "Hello" in string
print(substring)

# Example two
string = "Hello World"
substring = "Bello" in string
print(substring)