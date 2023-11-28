## 0x07. Python - Test-driven development

Certainly! Here's a detailed, brief, and straightforward README for tasks 0 to 8. I've provided explanations for the main code, focusing on each task. Note that this README assumes a basic understanding of Python programming concepts.

---

## Task 0: Integers addition

### Code (`0-add.py`):
```python
#!/usr/bin/python3
"""
Module to add two integers
"""


def add_integer(a, b=98):
    """
    Function to add two integers

    Args:
        a (int): The first integer.
        b (int): The second integer (default is 98).

    Returns:
        int: The sum of the two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
```

### Explanation:
- The `add_integer` function takes two arguments, `a` and `b`, and adds them.
- If either `a` or `b` is not an integer or float, a `TypeError` is raised.
- The function returns the sum of `a` and `b` as an integer.

---

## Task 1: Divide a matrix

### Code (`1-divide_matrix.py`):
```python
#!/usr/bin/python3
"""
Module to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix

    Args:
        matrix (list): The matrix as a list of lists of integers or floats.
        div (int or float): The number to divide each matrix element by.

    Returns:
        list: The new matrix with all elements divided by div.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix should contain only integers or floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
```

### Explanation:
- The `matrix_divided` function takes a matrix (`list` of `list`s) and a divisor (`div`).
- It checks if the matrix is valid and contains only integers or floats.
- Raises `TypeError` if any element in the matrix is not an integer or float.
- Raises `TypeError` if the divisor is not a number or if it's zero.
- Returns a new matrix with all elements divided by the divisor, rounded to 2 decimal places.

---

## Task 2: Say my name

### Code (`2-say_my_name.py`):
```python
#!/usr/bin/python3
"""
Module to print "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print "My name is <first name> <last name>"

    Args:
        first_name (str): The first name.
        last_name (str): The last name (default is an empty string).

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
```

### Explanation:
- The `say_my_name` function prints a formatted string indicating the first and last name.
- The first name is mandatory, and the last name is optional (default is an empty string).
- Raises `TypeError` if either `first_name` or `last_name` is not a string.

---

## Task 3: Print square

### Code (`3-print_square.py`):
```python
#!/usr/bin/python3
"""
Module to print a square with the character #
"""


def print_square(size):
    """
    Function to print a square with the character #

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Notes:
        The function prints an empty line for size = 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
```

### Explanation:
- The `print_square` function prints a square of '#' characters with the specified size.
- Raises `TypeError` if the size is not an integer and `ValueError` if it's less than 0.

---

## Task 4: Text indentation

### Code (`4-text_indentation.py`):
```python
#!/usr/bin/python3
"""
Module to print text with 2 new lines after '.', '?', and ':'
"""


def text_indentation(text):
    """
    Function to print text with 2 new lines after '.', '?', and ':'

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")

    print(text, end="")
```

### Explanation:
- The `text_indentation` function adds 2 new lines after '.', '?', and ':' in the input text.
- Raises `TypeError` if the input is not a string.

---

## Task 5: Max integer - Unittest

### Code (`5-max_integer.py`):
```python
#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def max_integer(list=[]):
    """
    Function to find and return the max integer in a list of integers

    Args:
        list (list): The list of integers.

    Returns:
        int: The max integer in the list or None if the list is empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    for num in list:
        if num > result:
            result = num
    return result
```

### Explanation:
- The `max_integer` function finds and returns the maximum integer in a list.
- Returns `None` if the list is empty.

---

## Task 6: Matrix multiplication

### Code (`100-matrix_mul.py`):
```python
#!/usr/bin/python3
"""
Module to multiply 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply 2 matrices

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Raises:
        TypeError: If matrices are not valid or can't be multiplied.

    Returns:
        list: The resulting matrix after multiplication.
    """
    if not isinstance

(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists of integers/floats")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists of integers/floats")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
    return result
```

### Explanation:
- The `matrix_mul` function multiplies two matrices and returns the result.
- Raises `TypeError` if matrices are not valid or can't be multiplied.
- Uses nested list comprehensions to perform matrix multiplication.

---

## Task 7: Lazy matrix multiplication

### Code (`101-lazy_matrix_mul.py`):
```python
#!/usr/bin/python3
"""
Module to multiply 2 matrices using NumPy
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using NumPy

    Args:
    - m_a and m_b must be validated with these requirements in this order

        m_a and m_b must be an list of lists of integers or floats:
        - if m_a or m_b is not a list: raise a TypeError exception with the message m_a must be a list or m_b must be a list
        - if m_a or m_b is not a list of lists: raise a TypeError exception with the message m_a must be a list of lists or m_b must be a list of lists
        - if m_a or m_b is empty (it means: = [] or = [[]]): raise a ValueError exception with the message m_a can't be empty or m_b can't be empty
        - if one element of those list of lists is not an integer or a float: raise a TypeError exception with the message m_a should contain only integers or floats or m_b should contain only integers or floats
        - if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size): raise a TypeError exception with the message each row of m_a must be of the same size or each row of m_b must be of the same size
        - If m_a and m_b can’t be multiplied: raise a ValueError exception with the message m_a and m_b can't be multiplied

    You are not allowed to import any module

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
```

### Explanation:
- The `lazy_matrix_mul` function multiplies two matrices using NumPy.
- Validates input matrices according to specified requirements.
- Uses NumPy for efficient matrix multiplication.
- Returns the resulting matrix after multiplication.

---

## Task 8: CPython #3: Python Strings

## Objective
The goal of this task is to create a C function that prints information about Python strings using the CPython API. The provided code includes a C function (`print_python_string`) and a Python script to test this function.

## Files

### 1. `102-python.c`

This C file contains the implementation of the `print_python_string` function. Here's a breakdown:

- `print_python_string(PyObject *p)`: This function takes a Python object as an argument and prints information about it.

  - It checks if the object is a valid Unicode string using `PyUnicode_Check`.
  
  - If it's a Unicode string, it checks whether it's a compact ASCII or compact Unicode object using `PyUnicode_IS_COMPACT_ASCII` and `PyUnicode_IS_COMPACT`.

  - It then prints information about the string, including its type, length, and value.

  - If the object is not a valid Unicode string, an error message is printed.

### 2. `102-tests.py`

This Python script (`102-tests.py`) demonstrates the usage of the `print_python_string` function by creating different types of strings and calling the function on them. The script includes examples of ASCII strings, Unicode strings, and a bytes object.

## How to Compile and Run

1. **Compile the C code:**
   ```bash
   gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
   ```

2. **Run the Python test script:**
   ```bash
   python3 102-tests.py
   ```

## Explanation

- The C code uses the CPython API to interact with Python objects.

- The `print_python_string` function provides information about the type, length, and value of a Python string.

- The Python test script demonstrates the usage of the C function with different types of strings.

## Notes

- This task focuses on working with Python objects using the CPython API and is intended for C developers interested in Python/C integration.

- Ensure that you have Python development headers installed (`-I/usr/include/python3.4`) to compile the C code.

- The provided test script (`102-tests.py`) showcases how to use the C function in a Python environment.
