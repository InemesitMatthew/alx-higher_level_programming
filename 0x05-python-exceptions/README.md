0x05. Python - Exceptions

---

## Task 0: Safe List Printing

### Objective:
Write a Python function to print elements of a list safely, handling exceptions.

### Code:
```python
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end=" ")
    except (IndexError, TypeError):
        pass
    finally:
        print()
```

### Explanation:
This function prints the first `x` elements of a list safely. It uses `try`, `except`, and `finally` blocks to handle exceptions like `IndexError` and `TypeError`. The goal is to ensure the program doesn't crash if there are issues with the list.

---

## Task 1: Safe Printing of Integers

### Objective:
Write a function to safely print an integer.

### Code:
```python
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
```

### Explanation:
The function prints an integer using the `"{:d}"` format. It uses a `try` block and catches a `ValueError` if the value is not an integer. Returns `True` if printed successfully, `False` otherwise.

---

## Task 2: Print and Count Integers

### Objective:
Write a function to print the first `x` integers of a list safely.

### Code:
```python
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end=" ")
                count += 1
        except IndexError:
            pass
    print()
    return count
```

### Explanation:
The function prints the first `x` integers of a list safely. It uses a `try` block to handle exceptions and checks if the element is an integer before printing.

---

## Task 3: Integers Division with Debug

### Objective:
Write a function to divide two integers and print the result with debug information.

### Code:
```python
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
        return result
    except ZeroDivisionError:
        print("Inside result: None")
        return None
```

### Explanation:
The function divides two integers, prints the result inside the `try` block, and handles `ZeroDivisionError`. It returns the result or `None` if the division is not possible.

---

## Task 4: Divide a List

### Objective:
Write a function to divide elements of two lists and handle various exceptions.

### Code:
```python
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except (ZeroDivisionError, TypeError):
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
```

### Explanation:
The function divides corresponding elements of two lists. It handles `ZeroDivisionError`, `TypeError`, and `IndexError`, providing appropriate values in case of exceptions.

---

## Task 5: Raise Exception

### Objective:
Write a function that raises a type exception.

### Code:
```python
def raise_exception():
    raise TypeError("Exception raised")
```

### Explanation:
The function raises a `TypeError` exception when called. It demonstrates how to intentionally raise exceptions.

---

## Task 6: Raise a Message

### Objective:
Write a function that raises a name exception with a message.

### Code:
```python
def raise_exception_msg(message=""):
    raise NameError(message)
```

### Explanation:
The function raises a `NameError` exception with an optional message. It shows how to raise exceptions with custom messages.

---

## Task 7: Safe Integer Print with Error Message (Advanced)

### Objective:
Write a function to safely print an integer with error handling and error message to stderr.

### Code:
```python
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as ve:
        import sys
        print("Exception: {}".format(ve), file=sys.stderr)
        return False
```

### Explanation:
The function prints an integer and handles `ValueError`. If an error occurs, it prints the exception message to `stderr` and returns `False`.

---

## Task 8: Safe Function (Advanced)

### Objective:
Write a function that executes a function safely, handling exceptions.

### Code:
```python
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
```

### Explanation:
The function executes a given function with arguments safely. It catches any exceptions, prints the exception message to `stderr`, and returns `None`.

---

## Task 9: ByteCode -> Python #4 (Advanced)



### Objective:
Write a Python function that mimics a given Python bytecode.

### Code:
```python
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if a > i:
                raise Exception("Too far")
            result += (a ** b) / i
        except:
            result = b + a
            break
    return result
```

### Explanation:
The function replicates the given Python bytecode using a `for` loop, `try`, and `except` blocks. It calculates a result based on conditions and handles exceptions.

---

## Task 10: CPython #2: PyFloatObject (Advanced)

### Objective:
Create C functions to print info about Python lists, bytes, and float objects.

### Code:
See [103-python.c](103-python.c)

### Explanation:
The C code defines functions to print information about Python lists, bytes, and float objects. It uses Python's C API to access and print object details.

---

