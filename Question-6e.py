"""print the following patterns:\
 e)
* * * * * *
* * * * *
* * * *
* * * 
* *
* 
"""


row=int(input("Enter the no of rows:"))

for i in range(row): #row 
    for j in range(i,row): # column
        print("*" , end=" ")
    print()