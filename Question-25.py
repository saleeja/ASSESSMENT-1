"""Write a Python program to perform matrix multiplication using lists of lists."""


def matrix_multiply(matrix1, matrix2):
    # Check if matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        print("Matrices cannot be multiplied. Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        return None

    # Perform matrix multiplication using list comprehension
    result_matrix = [
        [sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))]
        for i in range(len(matrix1))
    ]

    return result_matrix


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = matrix_multiply(matrix1, matrix2)


if result is not None:
    print("Result of matrix multiplication:")
    for row in result:
        print(row)



