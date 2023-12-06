#!/usr/bin/python3
"""
Defines a student with public instance attributes
and methods for serialization and deserialization
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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with
        the provided dictionary"""
        for key, value in json.items():
            setattr(self, key, value)


# Uncomment the following lines for testing
# student = Student("John", "Doe", 23)
# j_student = student.to_json()
# print("Initial student:")
# print(student)
# print(type(student))
# print(type(j_student))
# print("{} {} {}".format(student.first_name, student.last_name, student.age))

# save_to_json_file(j_student, "student.json")
# read_file("student.json")
# print("\nSaved to disk")

# new_student = Student("Fake", "Fake", 89)
# print("Fake student:")
# print(new_student)
# print(type(new_student))
# print("{} {} {}".format(new_student.first_name, new_student.last_name, new_student.age))

# print("Load dictionary from file:")
# new_j_student = load_from_json_file("student.json")

# new_student.reload_from_json(new_j_student)
# print(new_student)
# print(type(new_student))
# print("{} {} {}".format(new_student.first_name, new_student.last_name, new_student.age))
