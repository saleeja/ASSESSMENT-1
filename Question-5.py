"""Write a Python program to remove duplicates from a list."""

# Get user input for a list
user_input = input("Enter elements of the list separated by spaces: ")

# Check if there are spaces in the input
if ' ' not in user_input:
    print("Please enter a list of numbers separated by spaces.")
else:

    # Convert the input into a list of integers
    user_list = [int(item) for item in user_input.split()]

    # Remove duplicates using set and then convert back to list
    result = list(set(user_list))

    print(f"Original List: {user_list}")
    print(f"Duplicates Removed: {result}")
