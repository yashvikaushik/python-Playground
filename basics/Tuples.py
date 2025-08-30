# Tuples in Python - Basic Understanding

# Creating a tuple
fruits = ("apple", "banana", "cherry", "apple")

print("Original Tuple:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Tuple is immutable (can't change values)
# fruits[1] = "mango"  #This will raise an error

# Tuple methods
print("Count of 'apple':", fruits.count("apple"))
print("Index of 'cherry':", fruits.index("cherry"))

# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)

# Nesting tuples
nested_tuple = (fruits, mixed_tuple)
print("Nested Tuple:", nested_tuple)

# Tuple unpacking
a, b, c, d = fruits
print("Unpacked values:", a, b, c, d)

# Using tuple in a function (return multiple values)
def min_max(numbers):
    return (min(numbers), max(numbers))

numbers = (5, 3, 8, 1, 9)
print("Numbers:", numbers)
print("Min and Max:", min_max(numbers))