""" print the following patterns:
a)                       
0                           
0 0
0 0 0
0 0 0 0
"""


row=int(input("Enter the no of rows:"))

for i in range(row+1):
    for j in range(i):
        print("0", end=" ")
    print()