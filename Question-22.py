""" Write a Python program to calculate the sum of all elements in a list recursively."""

def findSum(list1): 
     if len(list1)== 1: 
        return list1[0] 
     else: 
        return list1[0]+findSum(list1[1:]) 
 
list1 = [1, 2, 3, 4, 5] 
print(findSum(list1))