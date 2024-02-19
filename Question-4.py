"""Write a Python program to find the sum of all even numbers in a list"""

def sum_even_odd_numbers(input_list):
    # Initialize sums for even and odd numbers
    sum_even = 0
    sum_odd = 0

    for number in input_list:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number

    return sum_even, sum_odd

# Get user input for a list
user_input = input("Enter elements of the list separated by spaces: ")
if ' ' not in user_input:
    print("Please enter a list of numbers separated by spaces.")
else:
    # Convert the input into a list of integers
    user_list = [int(item) for item in user_input.split()]

    # Call the function to find the sum of even and odd numbers
    sum_even, sum_odd = sum_even_odd_numbers(user_list)

    if sum_odd == 0:
        print("There are no odd numbers in this list")
    else:
        print(f"Sum of Odd Numbers: {sum_odd}")
        
    if sum_even==0:
        print("There are no even numbers in this list")
    else:
        print(f"Sum of Even Numbers: {sum_even}")

