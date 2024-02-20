""" Write a Python program to count the occurrences of an element in a list."""


def count_occurrences(lsts, element):
    return lsts.count(element)


print("Welcome to the Occurrence Counter!")

# Get user input for the list
user_input = input("Enter elements of the list: ")
user_list = list(user_input)

# Get user input for the element to count
element_to_count = input("Enter the element to count: ")


occurrences = count_occurrences(user_list, element_to_count)

print(f"The element '{element_to_count}' occurs {occurrences} times in the list.")

