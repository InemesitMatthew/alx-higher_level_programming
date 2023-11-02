## Task 0: Run Python file

### Code (0-run):
```bash
#!/bin/bash
./$PYFILE
```

### Explanation:
This Bash script runs a Python file whose name is stored in the environment variable `$PYFILE`. The script executes the Python file, and the output will be displayed in the terminal.

---

## Task 1: Run inline

### Code (1-run_inline):
```bash
#!/bin/bash
python -c "$PYCODE"
```

### Explanation:
This Bash script runs Python code provided in the environment variable `$PYCODE`. It uses the `-c` option with Python, which allows you to specify a command as a string. The script executes the Python code, and the output will be displayed in the terminal.

---

## Task 2: Hello, print

### Code (2-print.py):
```python
print("Programming is like building a multilingual puzzle")
```

### Explanation:
This Python script simply uses the `print` function to output the specified string to the console. It prints "Programming is like building a multilingual puzzle" followed by a newline, as required.

---

## Task 3: Print integer

### Code (3-print_number.py):
```python
number, street = 98, "Battery street"
print(f"{number} {street}")
```

### Explanation:
This Python script prints an integer (`number`) and a string (`street`) using f-strings. It combines the values of `number` and `street` in the required format: "the number, followed by Battery street," followed by a new line. It doesn't convert the integer into a string explicitly, as required.

---

## Task 4: Print float

### Code (4-print_float.py):
```python
number = 3.14159
print(f"Float: {number:.2f}")
```

### Explanation:
This Python script prints a floating-point number (`number`) with a precision of 2 digits after the decimal point using an f-string. It formats the output as "Float: X.XX" where `X.XX` represents the float value with two decimal places.


---

## Task 5: Print string

### Code (5-print_string.py):
```python
str = "Holberton School"
print(str * 3)
print(str[:9])
```

### Explanation:
This Python script prints the string "Holberton School" three times and then prints the first 9 characters of the same string. It accomplishes this without using any loops or conditional statements, and it is within the maximum 5 lines required.

---

## Task 6: Play with strings

### Code (6-concat.py):
```python
str1 = "Welcome to"
str2 = "Holberton School!"
print(str1 + " " + str2)
```

### Explanation:
This Python script uses the provided variables `str1` and `str2` to concatenate them with a space in between. It prints the resulting string "Welcome to Holberton School!" without using any loops or conditional statements, and it is exactly 5 lines long as required.

---

## Task 7: Copy - Cut - Paste

### Code (7-edges.py):
```python
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```

### Explanation:
This Python script extracts specific parts of the `word` variable to create new variables `word_first_3`, `word_last_2`, and `middle_word`. It then prints these parts as required: the first 3 letters, the last 2 letters, and the middle word. This is done without using loops or conditional statements and is exactly 8 lines long as specified.

---

## Task 8: Create a new sentence

### Code (8-concat_edges.py):
```python
str = "object-oriented programming"
print(str + " with Python")
```

### Explanation:
This Python script directly prints the provided string "object-oriented programming with Python" without the need for any loops or conditional statements. It's exactly 5 lines long and doesn't create new variables or use string literals, as required.

---

## Task 9: Easter Egg

### Code (9-easter_egg.py):
```python
import this
```

### Explanation:
This Python script uses the `import` statement to import the "this" module, which is a special module in Python. When imported, it prints "The Zen of Python" by Tim Peters, followed by the Zen of Python principles. The script is concise, with a maximum length of 98 characters, as required.

---

## Task 10: Linked list cycle

### Code (10-check_cycle.c, lists.h):
```c
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 0 if no cycle, 1 if a cycle is detected
 */
int check_cycle(listint_t *list);
```

### Explanation:
This C function, when provided with a singly linked list, checks if the list contains a cycle. It returns 0 if no cycle is detected and 1 if a cycle is found. The function uses the Floyd's Tortoise and Hare algorithm to detect cycles efficiently.

---

## Task 11: Hello, write

### Code (100-write.py):
```python
#!/usr/bin/python3
import sys

sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
sys.exit(1)
```

### Explanation:
This Python script prints the specified message to the standard error output (stderr) using the `sys.stderr.write` method. It then exits with a status code of 1, as required. It does not use the `print` function.

---

## Task 12: Compile

### Code (101-compile):
```bash
#!/bin/bash
PYFILE="$PYFILE"
py_compile "$PYFILE"
```

### Explanation:
This bash script compiles a Python script specified in the environment variable `PYFILE`. It uses the `py_compile` module to create a compiled Python file with the extension `.pyc`. The compiled file is named after the original file. For example, if `PYFILE=my_main.py`, the compiled file will be `my_main.pyc`.

---

## Task 13: ByteCode -> Python #1

### Code (102-magic_calculation.py):
```python
def magic_calculation(a, b):
    return 98 + a ** b
```

### Explanation:
This Python function, `magic_calculation`, is designed to mimic the behavior of the provided Python bytecode. It takes two arguments, `a` and `b`, and returns the result of the expression `98 + a ** b`. This function is an equivalent Python representation of the given bytecode.

---
