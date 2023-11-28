# 0x08. Python - More Classes and Objects

## Task 0: Simple rectangle
### Code: [0-rectangle.py](#)
```python
#!/usr/bin/python3
"""Defines a simple Rectangle class."""


class Rectangle:
    """Represents a rectangle."""
    pass
```
### Explanation:
This task introduces a simple Python class named `Rectangle` with no attributes or methods.

---

## Task 1: Real definition of a rectangle
### Code: [1-rectangle.py](#)
```python
#!/usr/bin/python3
"""Defines a Rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height."""
    
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
```
### Explanation:
The `Rectangle` class now has an `__init__` method to initialize instances with optional width and height attributes.

---

## Task 2: Area and Perimeter
### Code: [2-rectangle.py](#)
```python
#!/usr/bin/python3
"""Defines a Rectangle class with area and perimeter methods."""


class Rectangle:
    """Represents a rectangle with width and height."""
    
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
```
### Explanation:
Added methods `area` and `perimeter` to calculate the area and perimeter of the rectangle.

---

## Task 3: String representation
### Code: [3-rectangle.py](#)
```python
#!/usr/bin/python3
"""Defines a Rectangle class with a string representation method."""


class Rectangle:
    """Represents a rectangle with width and height."""
    
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "\n".join(["#" * self.width] * self.height)
```
### Explanation:
Added the `__str__` method to provide a string representation of the rectangle using "#" characters.

---

## Task 4: Eval is magic
### Code: [4-rectangle.py](#)
```python
#!/usr/bin/python3
"""Defines a Rectangle class with an additional representation method."""


class Rectangle:
    """Represents a rectangle with width and height."""
    
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "\n".join(["#" * self.width] * self.height)
    
    def __repr__(self):
        """Returns a string representation of the rectangle for eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)
```
### Explanation:
Added the `__repr__` method to provide a string representation of the rectangle suitable for `eval()`.

---

## Task 5: Detect instance deletion
### Code: [5-rectangle.py](#)
```python
#!/usr/bin/python3
"""Defines a Rectangle class with a deletion message."""


class Rectangle:
    """Represents a rectangle with width and height."""
    
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "\n".join(["#" * self.width] * self.height)
    
    def __repr__(self):
        """Returns a string representation of the rectangle for eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)
    
    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
```
### Explanation:
Added the `__del__` method to print a message when an instance of `Rectangle` is deleted.

---

## Task 6: How many instances
### Code: [6-rectangle.py](#)
```python
#!/usr/bin/python3
"""Defines a Rectangle class with a counter for instances."""


class Rectangle:
    """Represents a rectangle with width and height."""
    
    number_of_instances = 0
    
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "\n".join(["#" * self.width] * self.height)
    
    def __repr__(self):
        """Returns a string representation of the rectangle for eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)
    
    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
```
### Explanation:
Added a class variable `number_of_instances` to keep track of the number of `Rectangle` instances.

---

## Task 7: Change representation
### Code: [7-rectangle.py](#)
```python
#!/usr/bin/python3
"""Defines a Rectangle class with enhanced representation options."""


class Rectangle:
    """Represents a rectangle with width and height."""
    
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self

):
        """Retrieves the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)
    
    def __repr__(self):
        """Returns a string representation of the rectangle for eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)
    
    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
```
### Explanation:
Enhanced the representation of the rectangle by allowing customization of the print symbol.

---

## Task 8: Compare rectangles
### Code: [8-rectangle.py](#)
```python
#!/usr/bin/python3
"""Defines a Rectangle class with comparison capabilities."""


class Rectangle:
    """Represents a rectangle with width and height."""
    
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)
    
    def __repr__(self):
        """Returns a string representation of the rectangle for eval()."""
        return "Rectangle({}, {})".format(self.width, self.height)
    
    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
```
### Explanation:
Added a static method `bigger_or_equal` to compare two rectangles based on their area.

---

## Task 9: A Square is a Rectangle

### Overview:
This task involves creating a Python class named `Rectangle` that represents rectangles. The class includes methods to calculate area and perimeter, set width and height, and more. Additionally, it introduces a class method `square` to create a square using the same `Rectangle` class.

### Code:
```python
class Rectangle:
    def __init__(self, width=0, height=0):
        # Initialization code...

    # Other methods...

    @classmethod
    def square(cls, size=0):
        """Creates a square using the Rectangle class."""
        return cls(size, size)
```

### Explanation:
- **Initialization:** The `Rectangle` class is initialized with optional `width` and `height`.
- **Class Method:** The `square` class method is introduced to create a square. It takes a size argument and initializes a rectangle with equal width and height, creating a square.

---

## Task 10: N Queens

### Overview:
This task involves solving the N Queens puzzle, a classic chess problem. The program takes an integer N as input and prints all possible solutions to place N non-attacking queens on an N×N chessboard.

### Code:
```python
def solve_nqueens(n):
    """Solves the N Queens puzzle."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions

# Other helper functions...

if __name__ == "__main__":
    # Input validation and solution printing...
```

### Explanation:
- **Solution Function:** `solve_nqueens` is the main function that solves the N Queens puzzle. It initializes a chessboard, finds solutions using backtracking, and returns a list of solutions.
- **Usage:** The script can be run from the command line by providing an integer argument N. It then prints all possible solutions for placing N queens on an N×N chessboard.
