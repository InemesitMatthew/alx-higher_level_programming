#!/usr/bin/python3


def square_matrix_simple(matrix=None):
    if matrix is None:
        matrix = []
    # Create an empty list for the new matrix
    new_matrix = []

    # Iterate through the rows of the input matrix
    for row in matrix:
        new_row = [element**2 for element in row]
        # Append the new row to the new matrix
        new_matrix.append(new_row)

    # Return the new matrix
    return new_matrix
