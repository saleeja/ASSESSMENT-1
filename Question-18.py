"""Write a Python program to implement a binary search on a sorted list."""


def binary_search_recursive(sorted_list, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        mid_element = sorted_list[mid]

        if mid_element == target:
            return mid  # Found the target, return its index
        elif mid_element < target:
            return binary_search_recursive(sorted_list, target, mid + 1, high)  # Search the right half
        else:
            return binary_search_recursive(sorted_list, target, low, mid - 1)  # Search the left half
    else:
        return -1  # Target not found in the list


sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
target = int(input("Enter the target element to search: "))

result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
