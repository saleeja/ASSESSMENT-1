"""Write a Python program to merge two sorted lists into a single sorted list"""


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

# Merge the two lists
merged_list = sorted(list1 + list2)

print ("The original list 1 is : " + str(list1))
print ("The original list 2 is : " + str(list2))

print("The merged list is:",merged_list)

