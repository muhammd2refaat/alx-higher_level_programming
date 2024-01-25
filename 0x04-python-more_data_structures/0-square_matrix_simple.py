def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [[0 for _ in range(len(row))] for row in matrix]
    # Iterate through each element of the matrix and compute the square
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix


# Two blank lines after the function definition
# Example usage:
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_matrix_simple(input_matrix)
print(result)
