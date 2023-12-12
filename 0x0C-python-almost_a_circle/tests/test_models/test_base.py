# tests/test_models/test_base.py
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_create_instance_with_id(self):
        base_instance = Base(42)
        self.assertEqual(base_instance.id, 42)

    def test_create_instance_without_id(self):
        base_instance = Base()
        self.assertIsNotNone(base_instance.id)

    def test_create_multiple_instances(self):
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertNotEqual(base_instance1.id, base_instance2.id)

if __name__ == '__main__':
    unittest.main()
