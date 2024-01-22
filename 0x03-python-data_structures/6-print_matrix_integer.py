#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate over the rows of the matrix
    for row in matrix:
        # Iterate over the elements of the row
        for element in row:
            # Print the element followed by a space
            print("{:d}".format(element), end=" ")
        # Print a new line
        print()
