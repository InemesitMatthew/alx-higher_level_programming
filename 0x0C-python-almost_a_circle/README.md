0x0C-python-almost_a_circle


# Almost a Circle

This project is a part of the ALX Higher-Level Programming curriculum and focuses on the implementation of a Base class and its derived classes - Rectangle and Square. The project involves the creation of instances, serialization/deserialization to JSON and CSV formats, and drawing shapes using the Turtle graphics module.

## Contents

1. **Base Class**: The `Base` class serves as the foundation for the Rectangle and Square classes. It manages the assignment of unique IDs to instances and provides methods for JSON and CSV serialization/deserialization.

    - **Complete Code:**
        ```python
        # See complete code in models/base.py
        ```

2. **Rectangle Class**: The `Rectangle` class inherits from the `Base` class and represents a rectangle. It includes methods for area calculation, display, and update.

    - **Complete Code:**
        ```python
        # See complete code in models/rectangle.py
        ```

3. **Square Class**: The `Square` class is a derived class of `Rectangle` and represents a square. It inherits attributes and methods from both `Rectangle` and `Base`.

    - **Complete Code:**
        ```python
        # See complete code in models/square.py
        ```

4. **Serialization/Deserialization to JSON**:
   - `to_json_string(list_dictionaries)`: Converts a list of dictionaries to a JSON string.
   - `from_json_string(json_string)`: Converts a JSON string to a list of dictionaries.
   - `save_to_file(list_objs)`: Saves a list of objects to a JSON file.
   - `load_from_file()`: Loads objects from a JSON file.

    - **Complete Code:**
        ```python
        # See complete code in models/base.py
        ```

5. **Serialization/Deserialization to CSV**:
   - `save_to_file_csv(list_objs)`: Saves a list of objects to a CSV file.
   - `load_from_file_csv()`: Loads objects from a CSV file.

    - **Complete Code:**
        ```python
        # See complete code in models/base.py
        ```

6. **Drawing Shapes with Turtle Graphics**:
   - `draw(list_rectangles, list_squares)`: Opens a window and draws rectangles and squares using Turtle graphics.

    - **Complete Code:**
        ```python
        # See complete code in models/base.py
        ```

## Usage

1. **Installation**:
   - Ensure Python is installed.
   - Install the Turtle graphics module: `sudo apt-get install python3-tk`

2. **Run the Tests**:
   - Execute the test script: `python test.py`

3. **Advanced Task - Drawing Shapes**:
   - Uncomment the line in Vagrantfile: `config.ssh.forward_x11 = true`
   - Restart the VM: `vagrant halt` and then `vagrant up --provision`
   - Run the drawing script: `python 101-main.py`
