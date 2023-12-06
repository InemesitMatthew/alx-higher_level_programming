#!/usr/bin/python3
"""
Defines a student with public instance attributes
and a method to retrieve a dictionary representation of the student
with optional filtering of attributes
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the student
        with optional attribute filtering"""
        if attrs is None:
            return self.__dict__
        return {
            attr: getattr(self, attr, None) for attr in attrs if hasattr(self, attr)
        }


# Uncomment the following lines for testing
# student = Student("John", "Doe", 23)
# j_student_1 = student.to_json()
# print(j_student_1)
# j_student_2 = student.to_json(['first_name', 'age'])
# print(j_student_2)
# j_student_3 = student.to_json(['middle_name', 'age'])
# print(j_student_3)
