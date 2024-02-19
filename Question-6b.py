""" print the following patterns:
b)
 *
 * * *
 * * * * *
 * * * * * * * """

row=int(input("Enter the no of rows:"))

for i in range(1,row+1,2):
    for j in range(i):
        print("*", end=" ")
    print()