"""  Write a Python program to check if a string contains only digits.("12345" -->True"""

#function to check if a string contains only digits
def contains_only_digits(user_input):
    return user_input.isdigit()

# Get user input
user_input = input("Enter a string: ")

# Check if the input contains only digits using the function
if contains_only_digits(user_input):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

