"""Write a Python program to find the second largest number in a list"""


input_str = input("Enter elements of the list (comma-separated): ")

# Check if the input contains commas
if ',' not in input_str:
    print("Error: Please enter numbers separated by commas.")
else:
    # Convert input strings to integer list
    number_list = [int(element) for element in input_str.split(',')]

    if len(number_list) < 2:
        print("Error: Please enter at least two numbers.")
    else:
        # Find the maximum number (first largest)
        first_largest = max(number_list)

        # Remove the first largest number from the list
        number_list.remove(first_largest)

        # Find the second largest number (new maximum)
        second_largest = max(number_list)

        # Display the result
        print("Second-largest number in the list:", second_largest)

