""" print the following patterns:
b)
       *
     * * *
   * * * * *
 * * * * * * * 
 """

rows=int(input("Enter the no of rows:"))


for i in range(rows):
    for j in range(i,rows):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    for j in range(i+1):
        print("*", end=" ")
    print()