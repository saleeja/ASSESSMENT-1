"""11) Write a Python program to find the intersection of two lists."""

def find_intersection(list1, list2):
    # Use list comprehension to find common elements
    intersection = [element for element in list1 if element in list2]
    return intersection

# Get user input for the lists
input_list1 = input("Enter elements of list 1 (comma-separated): ").split(',')
input_list2 = input("Enter elements of list 2 (comma-separated): ").split(',')

# Convert input strings to integer lists
list1 = [int(element) for element in input_list1]
list2 = [int(element) for element in input_list2]

intersection_result = find_intersection(list1, list2)

print("Intersection of the two lists:", intersection_result)
