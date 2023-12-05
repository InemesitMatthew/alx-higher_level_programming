# Task 0x0A: Python - Inheritance

This project focuses on understanding and implementing concepts related to Python programming, specifically dealing with inheritance.

### Task 0: Lookup

**Objective:** Write a function that returns the list of available attributes and methods of an object.

```python
def lookup(obj):
    """
    Returns a list of attributes and methods of an object.
    """
    return dir(obj)
```

This function uses the `dir()` function to retrieve all attributes and methods of the given object.

### Task 1: My List

**Objective:** Write a class `MyList` that inherits from the built-in `list` class.

```python
class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
```

This class introduces a new method `print_sorted()` which prints the list in ascending order.

### Task 2: Exact Same Object

**Objective:** Write a function `is_same_class` that returns `True` if the object is exactly an instance of the specified class, otherwise `False`.

```python
def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class.
    """
    return type(obj) == a_class
```

This function checks if the type of the object matches the specified class.

### Task 3: Same Class or Inherit From

**Objective:** Write a function `is_kind_of_class` that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

```python
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or inherited from, the specified class.
    """
    return isinstance(obj, a_class)
```

This function uses the `isinstance()` function to check if the object is an instance of the specified class or its subclasses.

### Task 4: Only Subclass Of

**Objective:** Write a function `inherits_from` that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

```python
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited from the specified class.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
```

This function checks if the type of the object is a subclass of the specified class.

### Task 5: Geometry Module

**Objective:** Write an empty class `BaseGeometry`.

```python
class BaseGeometry:
    """
    An empty base geometry class.
    """
    pass
```

This task introduces a base class `BaseGeometry` with no methods or attributes.

### Task 6: Improve Geometry

**Objective:** Enhance the `BaseGeometry` class with a public instance method `area()` that raises an Exception with the message "area() is not implemented".

```python
class BaseGeometry:
    """
    A base geometry class with an empty implementation of the area method.
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
```

This improvement adds a method `area()` with a default exception message.

### Task 7: Integer Validator

**Objective:** Enhance the `BaseGeometry` class with a public instance method `integer_validator(name, value)` that validates the value.

```python
class BaseGeometry:
    """
    A base geometry class with an integer validator method.
    """
    def integer_validator(self, name, value):
        """
        Validates the value, raising TypeError or ValueError if necessary.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
```

This method checks if the value is an integer and greater than 0, raising appropriate exceptions if not.

### Task 8: Rectangle

**Objective:** Write a class `Rectangle` that inherits from `BaseGeometry` with an instantiation method `__init__(self, width, height)`.

```python
class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
```

This class introduces private attributes `__width` and `__height` and validates them using the inherited `integer_validator` method.

### Task 9: Full Rectangle

**Objective:** Enhance the `Rectangle` class with an implementation of the `area()` method and a custom string representation.

```python
class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
```

This enhancement adds an `area()` method and a custom string representation to the `Rectangle` class.

### Task 10: Square #1

**Objective:** Write a class `Square` that inherits from `Rectangle` with an instantiation method `__init__(self, size)`.

```python
class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes the Square with size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
```

This class introduces a `Square` class that inherits from `Rectangle` and uses its `integer_validator` method for size validation.

### Task 11: Square #2

**Objective:** Override the `__str__` method in the `Square` class

 for custom string representation.

```python
class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes the Square with size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
```

This task customizes the string representation of the `Square` class.

### Task 12: My Integer

**Objective:** Write a class `MyInt` that inherits from `int` with inverted `==` and `!=` operators.

```python
class MyInt(int):
    """
    A class MyInt that inherits from int with inverted equality operators.
    """
    def __eq__(self, other):
        """
        Inverted equality operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted inequality operator.
        """
        return super().__eq__(other)
```

This class introduces a custom `MyInt` class that inherits from `int` with inverted equality operators.

### Task 13: Can I?

**Objective:** Write a function `add_attribute` that adds a new attribute to an object if it's possible.

```python
def add_attribute(obj, name, value):
    """
    Adds a new attribute to the object if possible.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
```

This function checks if an object has a `__dict__` attribute and raises an exception if not, indicating that a new attribute can't be added.

