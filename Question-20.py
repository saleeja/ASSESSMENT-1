""" Write a Python program to flatten a nested list.([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6])"""


 

nested_list = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
 
# iterate through the sublist using List comprehension
flatList = [element for innerList in nested_list for element in innerList]
 
print("Orginal List:",nested_list)
print('Flat List:', flatList)