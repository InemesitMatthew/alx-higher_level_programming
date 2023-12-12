# tests/test_models/test_rectangle.py
import io  # Add this import for the io module
import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch  # Use the mock library for older Python versions
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_create_rectangle(self):
        rectangle_instance = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rectangle_instance), "[Rectangle] (12) 2/1 - 4/6")

    def test_area_calculation(self):
        rectangle_instance = Rectangle(3, 4)
        self.assertEqual(rectangle_instance.area(), 12)

    def test_display_method(self):
        rectangle_instance = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            rectangle_instance.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
