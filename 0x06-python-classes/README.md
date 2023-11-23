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

