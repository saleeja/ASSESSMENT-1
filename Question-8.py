"""Write a Python program to count the number of occurrences of each element in a tuple."""


from collections import Counter
# Get user input as a string
tuple_input = input("Enter a list of numbers separated by spaces: ")

# Convert the string to a tuple
input_tuple = tuple(map(int, tuple_input.split()))

# Create a Counter object for the tuple
counter = Counter(input_tuple)

# Print the count of each element
for element, count in counter.items():
    print(f"Number of occurrences of {element} = {count}")


