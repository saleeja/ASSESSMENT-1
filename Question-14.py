""" Write a Python program to remove all whitespace characters from a string"""


def remove(string):
	return string.replace(" ", "")  #(oldvalue, newvalue)


string = input("Enter a string:")
print(remove(string))
