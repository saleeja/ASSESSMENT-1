""" Write a Python program to count the number of vowels in a string"""

def count_in_vowels(userInput):
    vowels=["a","e","i","o","u"]  # List of vowels to check 
    # Initialize a counter variable to keep track of the vowel count
    count=0
    
    for i in userInput:
        if i in vowels:
            count+=1
    return count
   
# Get user input
userInput=(input("Enter a string:"))
vowel_count=(count_in_vowels(userInput))

if vowel_count > 0:
    print(f"The number of vowels in the string is: {vowel_count}")
else:
    print("There are no vowels in the string.")