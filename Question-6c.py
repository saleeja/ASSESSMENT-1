""" print the following patterns:

c)
0
1 1
2 2 2
3 3 3 3
4 4 4 4 4
5 5 5 5 5 5
"""

rows=int(input("Enter the number of rows:"))


for i in range(0,rows+1):
    for j in range(i+1):
        print(i,end=" ")
    print()