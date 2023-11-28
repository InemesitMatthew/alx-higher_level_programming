#!/usr/bin/python3
"""
Module to multiply 2 matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using NumPy

    Args:
    - m_a (list): The first matrix.
    - m_b (list): The second matrix.

    Raises:
    - ValueError: If matrices can't be multiplied.

    Returns:
    - numpy.ndarray: The resulting matrix after multiplication.
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    np_a = np.array(m_a)
    np_b = np.array(m_b)

    result = np.matmul(np_a, np_b)
    return result.tolist()


if __name__ == "__main__":
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
