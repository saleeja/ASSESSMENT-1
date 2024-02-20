""" Write a Python program to check if a string is an anagram of another string.("listen", "silent")"""


def is_anagram(str1, str2):
    # Check if the frequency of characters in both strings is the same
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if is_anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
