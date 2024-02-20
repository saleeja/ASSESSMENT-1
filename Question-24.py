"""Write a Python program to remove all occurrences of a given element from a list"""


def remove_element(lst, element_to_remove):
    return list(filter(lambda x: x != element_to_remove, lst))

# Get user input for the list
input_list = input("Enter elements of the list (space-separated): ").split()

# Get user input for the element to remove
element_to_remove = input("Enter the element to remove: ")

# Convert input strings to the integer list
number_list = [int(element) for element in input_list]

# Remove all occurrences of the given element
result_list = remove_element(number_list, int(element_to_remove))


print("List after removing all occurrences of", element_to_remove, ":", result_list)
