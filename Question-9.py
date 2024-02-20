"""  Write a Python program to check if a string contains only digits.("12345" -->True"""

def contains_only_digits(user_input):
    return user_input.isdigit()


user_input = input("Enter a string: ")

if contains_only_digits(user_input):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

