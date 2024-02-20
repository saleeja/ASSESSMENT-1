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

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    print(f"Enter the elements for the {rows}x{cols} matrix:")
    for i in range(rows):
        row = [int(input(f"Enter element at position ({i+1}, {j+1}): ")) for j in range(cols)]
        matrix.append(row)

    return matrix

# Get user input for matrix1
print("Enter details for the first matrix:")
matrix1 = input_matrix()

# Get user input for matrix2
print("\nEnter details for the second matrix:")
matrix2 = input_matrix()

# Perform matrix multiplication
result = matrix_multiply(matrix1, matrix2)

# Print the result
if result is not None:
    print("\nResult of matrix multiplication:")
    for row in result:
        print(row)
