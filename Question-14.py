""" Write a Python program to remove all whitespace characters from a string"""


def remove(string):
	return string.replace(" ", "")


string = input("Enter a string:")
print(remove(string))
