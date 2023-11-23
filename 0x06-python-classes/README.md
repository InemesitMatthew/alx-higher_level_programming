## 0x06. Python - Classes and Objects

### Task 0: My First Square

#### Description

Write an empty class `Square` that defines a square. You are not allowed to import any module.

#### Code Example

```python
#!/usr/bin/python3
"""
0-square.py - Defines an empty Square class
"""

class Square:
    """
    The Square class represents a square.
    """
    pass
```

#### Explanation

In this task, we define a basic `Square` class with no attributes or methods. This serves as the foundation for subsequent tasks.

#### Test Code

```python
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
```

### Task 1: Square with Size

#### Description

Write a class `Square` that defines a square with a private instance attribute `size`.

#### Code Example

```python
#!/usr/bin/python3
"""
1-square.py - Defines a Square class with a private size attribute
"""

class Square:
    """
    The Square class represents a square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square.
        """
        self.__size = size
```

#### Explanation

In this task, we enhance the `Square` class to include a private attribute `__size`. The `__init__` method initializes a new square with the specified size.

#### Test Code

```python
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
```

### Task 2: Size Validation

#### Description

Write a class `Square` that defines a square with a private instance attribute `size` and includes size validation.

#### Code Example

```python
#!/usr/bin/python3
"""
2-square.py - Defines a Square class with size validation
"""

class Square:
    """
    The Square class represents a square.

    Attributes:
    - size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Parameters:
        - value (int): The size value.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
```

#### Explanation

In this task, we add a size validation to the `Square` class using a property and a setter method. The size must be an integer and greater than or equal to 0.

#### Test Code

```python
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
```

### Task 3: Area of a Square

#### Description

Write a class `Square` that defines a square and includes a method `area` to calculate the current square area.

#### Code Example

```python
#!/usr/bin/python3
"""
3-square.py - Defines a Square class with an area method
"""

class Square:
    """
    The Square class represents a square.

    Attributes:
    - size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        -

 ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Parameters:
        - value (int): The size value.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2
```

#### Explanation

In this task, we add an `area` method to the `Square` class, which calculates and returns the area of the square.

#### Test Code

```python
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
```

### Task 4: Access and Update Private Attribute

#### Description

Write a class `Square` that defines a square with a private instance attribute `size` and includes methods to get, set, and calculate the square area.

#### Code Example

```python
#!/usr/bin/python3
"""
4-square.py - Defines a Square class with getter, setter, and area methods
"""

class Square:
    """
    The Square class represents a square.

    Attributes:
    - size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Parameters:
        - value (int): The size value.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2
```

#### Explanation

In this task, we enhance the `Square` class with getter (`size` method), setter (`size` method), and area methods to retrieve, set, and calculate the square area.

#### Test Code

```python
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
```

### Task 5: Printing a Square

#### Description

Write a class `Square` that defines a square with methods to get, set, calculate the square area, and print the square using the `#` character.

#### Code Example

```python
#!/usr/bin/python3
"""
5-square.py - Defines a Square class with printing capabilities
"""

class Square:
    """
    The Square class represents a square.

    Attributes:
    - size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Parameters:
        - value (int): The size value.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
```

#### Explanation

In this task, we enhance the `Square` class with a `my_print` method, which prints the square using the '#' character. If the size is 0, it prints an empty line.

#### Test Code

```python
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
```

### Task 6: Coordinates of a Square

#### Description

Extend the `Square` class to include a private instance attribute `position`. This represents the square's position. The `my_print` method now considers the position while printing the square with the `#` character.

#### Code Example

```python
class Square:
    """
    Represent a square with size and position.

    Attributes:
    - size (int): The size of the square.
    - position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square instance.

        Parameters:
        - size (int): The size of the square (default is 0).
        - position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
        tuple: The position as a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Parameters:
        - value (tuple): The position as a tuple of 2 positive integers.

        Raises:
        TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print the square with the '#' character, considering the position.
        """
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
```

#### Explanation

In this task, we introduced the `position` attribute to the `Square` class, allowing the square to be positioned. The `my_print` method was updated to consider the position while printing.

#### Testing

```python
my_square_1 = Square(3)
my_square_1.my_print()

# Output:
# ###
# ###
# ###

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

# Output:
#  ###
#  ###
#  ###

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

# Output:
# ###
# ###
# ###
```

### Task 7: Singly Linked List

#### Description

Create a `Node` class representing a node in a singly linked list and a `SinglyLinkedList` class to represent the list. Implement a `sorted_insert` method to insert a new node into the list in sorted order.

#### Code Example

```python
class Node:
    """
    Represent a node in a singly linked list.

    Attributes:
    - data: Data stored in the node.
    - next_node: Reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize the Node instance.

        Parameters:
        - data: Data to be stored in the node.
        - next_node: Reference to the next node in the list.
        """
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """
    Represent a singly linked list.

    Attributes:
    - head: Reference to the head of the list.
    """

    def __init__(self):
        """
        Initialize the SinglyLinkedList instance.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Parameters:
        - value: Value to be stored in the new node.
        """
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the list.

        Returns:
        str: String representation of the list.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
```

#### Explanation

In this task, we implemented a singly linked list with a `Node` class representing nodes and a `SinglyLinkedList` class representing the list. The `sorted_insert` method inserts a new node into the list in sorted order

.

#### Testing

```python
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

# Output:
# -4
# -3
# 1
# 2
# 3
# 3
# 4
# 5
# 5
# 10
# 12
```

### Task 8: Print Square instance

#### Description

Enhance the `Square` class to include a `__str__` method, allowing instances to be printed in the same format as `my_print`.

#### Code Example

```python
class Square:
    """
    Represent a square with size and position.

    Attributes:
    - size (int): The size of the square.
    - position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square instance.

        Parameters:
        - size (int): The size of the square (default is 0).
        - position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
        tuple: The position as a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Parameters:
        - value (tuple): The position as a tuple of 2 positive integers.

        Raises:
        TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print the square with the '#' character, considering the position.
        """
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: String representation of the square.
        """
        result = []
        for _ in range(self.position[1]):
            result.append('')
        for _ in range(self.size):
            result.append(" " * self.position[0] + "#" * self.size)
        return '\n'.join(result)
```

#### Explanation

In this task, the `Square` class was enhanced to include a `__str__` method, allowing instances to be printed in the same format as `my_print`.

#### Testing

```python
my_square = Square(5, (0, 0))
print(my_square)

# Output:
# #####
# #####
# #####
# #####
# #####

print("--")

my_square = Square(5, (4, 1))
print(my_square)

# Output:
#     #####
#     #####
#     #####
#     #####
#     #####
```

### Task 9: Compare 2 Squares

#### Code Example

```python
class Square:
    """A class to represent a square and perform comparisons based on area."""
    
    def __init__(self, size=0):
        """
        Initialize the Square instance.

        Parameters:
        size (int or float): The size of the square.

        Raises:
        TypeError: If size is not a number.
        ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
        value (int or float): The size to set.

        Raises:
        TypeError: If value is not a number.
        ValueError: If value is less than 0.
        """
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare two squares for equality based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two squares for inequality based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare two squares for less than based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if area is less than, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare two squares for less than or equal based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare two squares for greater than based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if area is greater than, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare two squares for greater than or equal based on area.

        Parameters:
        other (Square): The square to compare.

        Returns:
        bool: True if area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()
```

#### Explanation

The `Square` class represents a square and includes methods for comparing two squares based on their areas. The comparison methods (`__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`) provide functionality to determine the relationship between two squares.

#### Testing

You can test the functionality using the provided code:

```python
s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")
```

This code demonstrates the use of comparison operators to compare two `Square` instances.

---

### Task 10: ByteCode -> Python #5

#### Code Example

```python
import math

class MagicClass:
    """A class to perform operations equivalent to given Python bytecode."""

    def __init__(self, radius=0):
        """
        Initialize the MagicClass instance.

        Parameters:
        radius (int or float): The radius of the circle.

        Raises:
        TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
        float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
        float: The circumference of the circle.
        """
        return

 2 * math.pi * self.__radius
```

#### Explanation

The `MagicClass` class is designed to replicate the operations described in the given Python bytecode. It includes methods for calculating the area and circumference of a circle based on the provided radius.

#### Testing

You can test the functionality using the provided code:

```python
magic_circle = MagicClass(5)
print("Area:", magic_circle.area())
print("Circumference:", magic_circle.circumference())
```

This code creates a `MagicClass` instance with a radius of 5 and prints the calculated area and circumference.

---
