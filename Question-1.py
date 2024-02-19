"""1) write a single program to handle the following arithmetic operations for addition, subtraction, 
multiplication , division, floor division,modulus and Exponentiation."""


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def floor_divide(x, y):
    if y != 0:
        return x // y
    else:
        return "Cannot divide by zero"

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Cannot divide by zero"

def exponentiation(x, y):
    return x ** y


def calculator():
    print("""Choose the operation need to perform:
          1.Addition
          2.Subtraction
          3.Multiplication
          4.Division
          5.Floor division
          6.Modulus
          7.Exponentiation
          """)

    choice=int(input("which operation do you need to perform (1/2/3/4/5/6/7):"))
    if choice not in [1, 2, 3, 4, 5, 6, 7]:
        print('Enter a valid operation')
        return
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))


    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 4:
        print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == 5:
        print(num1, "//", num2, "=", floor_divide(num1, num2))

    elif choice == 6:
        print(num1, "%", num2, "=", modulus(num1, num2))

    elif choice == 7:
        print(num1, "**", num2, "=", exponentiation(num1, num2))

    else:
        print("Invalid Input")

        
while True:
    calculator()
    # Ask the user if they want to continue
    user_choice = input("Do you want to continue (yes/no)? ")
    if user_choice != 'yes':
        print("Thank you for using. Exiting.")
        break



