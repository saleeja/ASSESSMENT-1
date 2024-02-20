"""Write a Python program to perform matrix multiplication using lists of lists."""


matrix_A_rows = int(input('ENter number of rows for matrix-A: '))

matrix_A_cols  = int(input('ENter number of columns for matrix-A: '))

print() 

matrix_B_rows = int(input('ENter number of rows for matrix-B: '))
matrix_B_cols  = int(input('ENter number of columns for matrix-B: '))

print() 

if matrix_A_cols == matrix_B_rows:
    print('Enter values for matrix A')
    matrix_A = [[int(input(f"column {j+1} -> ENter {i+1} element:")) for j in range(matrix_A_cols)] for i in range(matrix_A_rows) ]

    print() 

    print('Enter values for matrix B ')
    matrix_B = [[int(input(f"column {j+1} -> ENter {i+1} element:")) for j in range(matrix_B_cols)] for i in range(matrix_B_rows) ]

    print()

    print('Matrix-A :')
    for i in matrix_A:
        print(i)

    print()

    print('Matrix-B :')
    for i in matrix_B:
        print(i)

    # mutiplication operation

    # resultant matrix (matrix that store answer and intially it is Zero)
    result = [[0 for j in range(matrix_B_cols)] for i in range(matrix_A_rows)]

    # main logic for matrix multiplication (multiplication operation)
    for i in range(len(matrix_A)):
        for j in range(len(matrix_B[0])):
            for k in range(len(matrix_B)):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]
        
    print() 

    print('Multiplication of Matrix-A and Matrix-B is :')
    for i in result:  
        print(i)
        
else:
    print('Multiplication of matrices is not possible (columns of matrix-A = row of matrix-B)')











