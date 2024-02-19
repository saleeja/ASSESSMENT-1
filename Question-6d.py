""" print the following patterns:

d)
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 """

rows=int(input("Enter the number of rows:"))


for i in range(rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()