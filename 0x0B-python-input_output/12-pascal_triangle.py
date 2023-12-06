#!/usr/bin/python3
"""
Generates Pascal's Triangle up to a given number of rows
"""


def pascal_triangle(n):
    """Generates Pascal's Triangle up to the nth row"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        row.extend(triangle[i - 1][j - 1] + triangle[i - 1][j] for j in range(1, i))
        row.append(1)
        triangle.append(row)

    return triangle


# Uncomment the following lines for testing
# if __name__ == "__main__":
#     triangle = pascal_triangle(5)
#     for row in triangle:
#         print(row)
