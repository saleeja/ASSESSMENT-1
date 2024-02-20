"""Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.(gcd(48, 
60)=12)"""


def gcd(a, b):

  while b > 0:
    r= a % b
    a=b
    b=r

  return a


# Get user input for the two numbers
num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

result_gcd = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {result_gcd}")
