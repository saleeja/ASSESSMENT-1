"""Write a Python program to check if a given number is a perfect number"""

# perfect number, a positive integer that is equal to the sum of its proper divisors. 
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.

def is_perfect_number(number):
    if number <= 0:
        return False

    divisors_sum = 0
    for i in range(1, number):  
        if number % i == 0:
            divisors_sum += i

    return divisors_sum == number

# Get user input for the number
user_input = input("Enter a number: ")

# Check if the input is a positive integer
if user_input.isdigit():
    user_number = int(user_input)
    
    # Check if the number is a perfect number
    if is_perfect_number(user_number):
        print(f"{user_number} is a perfect number.")
    else:
        print(f"{user_number} is not a perfect number.")
else:
    print("Invalid input. Please enter a valid positive integer.")
