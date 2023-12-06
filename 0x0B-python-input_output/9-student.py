#!/usr/bin/python3
"""
Defines a student with public instance attributes
and a method to retrieve a dictionary representation of the student
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the student"""
        return self.__dict__


# Uncomment the following lines for testing
# student = Student("John", "Doe", 23)
# j_student = student.to_json()
# print(type(j_student))
# print(j_student['first_name'])
# print(type(j_student['first_name']))
# print(j_student['age'])
# print(type(j_student['age']))
