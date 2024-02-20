""" Write a Python program to check if a given year is a leap year."""

def is_leap_year(year):
    # Leap years are either divisible by 4 and not divisible by 100
    # or divisible by 400.
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


user_input = int(input("Enter a year: "))

if is_leap_year(user_input):
    print(f"{user_input} is a leap year.")
else:
    print(f"{user_input} is not a leap year.")
