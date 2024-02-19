"""Write a Python program to reverse a list."""

# Get a list from user input
user_input = input("Enter a list of numbers separated by spaces: ")

# Check if there are spaces in the input
if ' ' not in user_input:
    print("Please enter a list of numbers separated by spaces.")
else:
    # Convert the input into integers
    user_list = [int(num) for num in user_input.split()]

    # Reverse the list using the reversed() function
    reversed_result = list(reversed(user_list))

    print("Original List:", user_list)
    print("Reversed List:", reversed_result)



