## Task 0: Squared simple

### Code: [0-square_matrix_simple.py](0-square_matrix_simple.py)

```python
def square_matrix_simple(matrix=[]):
    """Square the elements of a matrix."""
    return [[num ** 2 for num in row] for row in matrix]
```

### Explanation:
- This function takes a matrix as input and returns a new matrix with each element squared.
- It uses list comprehensions to iterate through the rows and elements of the matrix.

---

## Task 1: Search and replace

### Code: [1-search_replace.py](1-search_replace.py)

```python
def search_replace(my_list, search, replace):
    """Search and replace elements in a list."""
    return [replace if elem == search else elem for elem in my_list]
```

### Explanation:
- The function takes a list (`my_list`), a search value, and a replacement value.
- It creates a new list with elements replaced if they match the search value.

---

## Task 2: Unique addition

### Code: [2-uniq_add.py](2-uniq_add.py)

```python
def uniq_add(my_list=[]):
    """Add unique elements of a list."""
    return sum(set(my_list))
```

### Explanation:
- The function takes a list (`my_list`) and returns the sum of its unique elements.
- It converts the list to a set to remove duplicates and then calculates the sum.

---

## Task 3: Present in both

### Code: [3-common_elements.py](3-common_elements.py)

```python
def common_elements(set_1, set_2):
    """Find common elements between two sets."""
    return set_1 & set_2
```

### Explanation:
- The function takes two sets (`set_1` and `set_2`) and returns their common elements using the `&` operator.

---

## Task 4: Only differents

### Code: [4-only_diff_elements.py](4-only_diff_elements.py)

```python
def only_diff_elements(set_1, set_2):
    """Find elements that are unique to each set."""
    return set_1 ^ set_2
```

### Explanation:
- The function takes two sets (`set_1` and `set_2`) and returns their symmetric difference using the `^` operator.

---

## Task 5: Number of keys

### Code: [5-number_keys.py](5-number_keys.py)

```python
def number_keys(a_dictionary):
    """Return the number of keys in a dictionary."""
    return len(a_dictionary)
```

### Explanation:
- The function takes a dictionary (`a_dictionary`) and returns the number of keys using the `len` function.

---

## Task 6: Print sorted dictionary

### Code: [6-print_sorted_dictionary.py](6-print_sorted_dictionary.py)

```python
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
```

### Explanation:
- The function prints the dictionary by keys in alphabetical order using the `sorted` function.

---

## Task 7: Update dictionary

### Code: [7-update_dictionary.py](7-update_dictionary.py)

```python
def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value in a dictionary."""
    a_dictionary[key] = value
    return a_dictionary
```

### Explanation:
- The function replaces or adds a key-value pair in the dictionary and returns the updated dictionary.

---

## Task 8: Simple delete by key

### Code: [8-simple_delete.py](8-simple_delete.py)

```python
def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary."""
    a_dictionary.pop(key, None)
    return a_dictionary
```

### Explanation:
- The function deletes a key from the dictionary using the `pop` method and returns the updated dictionary.

---

## Task 9: Multiply by 2

### Code: [9-multiply_by_2.py](9-multiply_by_2.py)

```python
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2."""
    return {key: value * 2 for key, value in a_dictionary.items()}
```

### Explanation:
- The function returns a new dictionary with all values multiplied by 2 using a dictionary comprehension.

---

## Task 10: Best score

### Code: [10-best_score.py](10-best_score.py)

```python
def best_score(a_dictionary):
    """Return a key with the biggest integer value."""
    if a_dictionary:
        return max(a_dictionary, key=lambda k: a_dictionary[k])
    return None
```

### Explanation:
- The function returns the key with the highest integer value in the dictionary using the `max` function.

---

## Task 11: Multiply by using map

### Code: [11-multiply_list_map.py](11-multiply_list_map.py)

```python
def multiply_list_map(my_list=[], number=0):
    """Return a new list with all values multiplied by a number using map."""
    return list(map(lambda x: x * number, my_list))
```

### Explanation:
- The function uses `map` to multiply each

 element of the list by a given number and returns the new list.

---

## Task 12: Roman to Integer

### Code: [12-roman_to_int.py](12-roman_to_int.py)

```python
def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(roman_string):
        value = roman_values[char]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    return total
```

### Explanation:
- The function converts a Roman numeral to an integer using a dictionary of Roman numeral values.

---

## Task 13: Weighted average

### Code: [100-weight_average.py](100-weight_average.py)

```python
def weight_average(my_list=[]):
    """Return the weighted average of integers tuple (score, weight)."""
    if not my_list:
        return 0
    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)
    return total_score / total_weight
```

### Explanation:
- The function calculates the weighted average of integers tuple (score, weight) in a list.

---

## Task 14: Squared by using map

### Code: [101-square_matrix_map.py](101-square_matrix_map.py)

```python
def square_matrix_map(matrix=[]):
    """Return a new matrix with square values using map."""
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
```

### Explanation:
- The function uses `map` to square each element of the matrix and returns the new matrix.

---

## Task 15: Delete by value

### Code: [102-complex_delete.py](102-complex_delete.py)

```python
def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
```

### Explanation:
- The function deletes keys with a specific value in the dictionary without using `pop` or `filter`.

---

## Task 16: CPython #1: PyBytesObject

### Code: [103-python.c](103-python.c)

```c
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
```

### Explanation:
- This C file defines two functions (`print_python_list` and `print_python_bytes`) for printing information about Python lists and bytes objects.

---
