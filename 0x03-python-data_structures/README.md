# Project: Data Structures in C

This project consists of various C programs focusing on data structures, linked lists, and basic algorithms.

## Task 0: Print a List of Integers

**File:** `0-print_list_integer.c`

**Description:** This program defines a function `print_list_integer` that prints all integers of a given list, one integer per line.

```c
void print_list_integer(int *my_list, int size);
```

## Task 1: Secure Access to an Element in a List

**File:** `1-element_at.c`

**Description:** The program implements a function `element_at` to retrieve an element from a list. It returns the element at a given index if the index is valid; otherwise, it returns `NULL`.

```c
int *element_at(int *my_list, int idx);
```

## Task 2: Replace Element in a List

**File:** `2-replace_in_list.c`

**Description:** The program defines a function `replace_in_list` that replaces an element at a specific position in a list. If the index is out of range, it returns the original list; otherwise, it modifies the list and returns the updated one.

```c
int *replace_in_list(int *my_list, int idx, int new_element);
```

## Task 3: Print a List of Integers in Reverse

**File:** `3-print_reversed_list_integer.c`

**Description:** This program prints all integers of a list in reverse order. It defines a function `print_reversed_list_integer` that achieves this.

```c
void print_reversed_list_integer(int *my_list, int size);
```

## Task 4: Replace in a Copy

**File:** `4-new_in_list.c`

**Description:** The program provides a function `new_in_list` that replaces an element in a list at a specific position without modifying the original list. If the index is out of range, it returns a copy of the original list.

```c
int *new_in_list(int *my_list, int idx, int new_element);
```

## Task 5: Remove Characters 'c' and 'C' from a String

**File:** `5-no_c.c`

**Description:** This program defines a function `no_c` that removes all occurrences of characters 'c' and 'C' from a given string.

```c
char *no_c(char *my_string);
```

## Task 6: Lists of Lists = Matrix

**File:** `6-print_matrix_integer.c`

**Description:** The program prints a matrix of integers. It defines a function `print_matrix_integer` that takes a matrix (list of lists) as input and prints it.

```c
void print_matrix_integer(int **matrix, int rows, int columns);
```

## Task 7: Tuples Addition

**File:** `7-add_tuple.c`

**Description:** This program defines a function `add_tuple` that adds two tuples. The result is a tuple containing the element-wise addition of the input tuples.

```c
int *add_tuple(int *tuple_a, int *tuple_b);
```

## Task 8: Multiple Returns

**File:** `8-multiple_returns.c`

**Description:** The program defines a function `multiple_returns` that returns a tuple with the length of a string and its first character. If the string is empty, the first character is set to `NULL`.

```c
int *multiple_returns(char *sentence);
```

## Task 9: Find the Max Integer in a List

**File:** `9-max_integer.c`

**Description:** This program defines a function `max_integer` that finds the biggest integer in a list. If the list is empty, it returns `NULL`.

```c
int *max_integer(int *my_list, int size);
```

## Task 10: Find Multiples of 2 in a List

**File:** `10-divisible_by_2.c`

**Description:** The program defines a function `divisible_by_2` that finds all multiples of 2 in a list. It returns a new list of boolean values indicating whether each element is divisible by 2.

```c
int *divisible_by_2(int *my_list, int size);
```

## Task 11: Delete Element at a Specific Position

**File:** `11-delete_at.c`

**Description:** This program defines a function `delete_at` that deletes an item at a specific position in a list. If the index is negative or out of range, it returns the same list.

```c
int *delete_at(int *my_list, int idx);
```

## Task 12: Switch Values of Two Variables

**File:** `12-switch.c`

**Description:** The program switches the values of two variables `a` and `b`. It demonstrates a simple swap operation.

```c
void switch_values(int *a, int *b);
```



## Task 13: Linked List Palindrome

**Files:** `13-is_palindrome.c`, `lists.h`

**Description:** This program checks if a singly linked list is a palindrome. It defines a function `is_palindrome` that returns 1 if the linked list is a palindrome, and 0 otherwise.

```c
int is_palindrome(listint_t **head);
```

---
