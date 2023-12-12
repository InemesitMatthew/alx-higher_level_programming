# #!/usr/bin/python3
# """1-main"""
# from models.rectangle import Rectangle

# if __name__ == "__main__":
#     r1 = Rectangle(10, 2)
#     print(r1.id)

#     r2 = Rectangle(2, 10)
#     print(r2.id)

#     r3 = Rectangle(10, 2, 0, 0, 12)
#     print(r3.id)


# #!/usr/bin/python3
# """2-main"""
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     try:
#         Rectangle(10, "2")
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         r = Rectangle(10, 2)
#         r.width = -10
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         r = Rectangle(10, 2)
#         r.x = {}
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         Rectangle(10, 2, 3, -1)
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))


# #!/usr/bin/python3
# """3-main"""
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     r1 = Rectangle(3, 2)
#     print(r1.area())  # Output: 6

#     r2 = Rectangle(2, 10)
#     print(r2.area())  # Output: 20

#     r3 = Rectangle(8, 7, 0, 0, 12)
#     print(r3.area())  # Output: 56


# #!/usr/bin/python3
# """4-main"""
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     r1 = Rectangle(4, 6)
#     r1.display()
#     """
#     Output:
#     ####
#     ####
#     ####
#     ####
#     ####
#     ####
#     """

#     print("---")

#     r2 = Rectangle(2, 2)
#     r2.display()
#     """
#     Output:
#     ##
#     ##
#     """



# #!/usr/bin/python3
# """5-main"""
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     r1 = Rectangle(4, 6, 2, 1, 12)
#     print(r1)  # Output: [Rectangle] (12) 2/1 - 4/6

#     r2 = Rectangle(5, 5, 1)
#     print(r2)  # Output: [Rectangle] (1) 1/0 - 5/5



# #!/usr/bin/python3
# """6-main"""
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     r1 = Rectangle(2, 3, 2, 2)
#     r1.display()
#     """
#       ##
#       ##
#       ##
#     """

#     print("---")

#     r2 = Rectangle(3, 2, 1, 0)
#     r2.display()
#     """
#      ###
#      ###
#     """




# #!/usr/bin/python3
# """Doc"""
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     r1 = Rectangle(10, 10, 10, 10)
#     print(r1)  # Output: [Rectangle] (1) 10/10 - 10/10

#     r1.update(89)
#     print(r1)  # Output: [Rectangle] (89) 10/10 - 10/10

#     r1.update(89, 2)
#     print(r1)  # Output: [Rectangle] (89) 10/10 - 2/10

#     r1.update(89, 2, 3)
#     print(r1)  # Output: [Rectangle] (89) 10/10 - 2/3

#     r1.update(89, 2, 3, 4)
#     print(r1)  # Output: [Rectangle] (89) 4/10 - 2/3

#     r1.update(89, 2, 3, 4, 5)
#     print(r1)  # Output: [Rectangle] (89) 4/5 - 2/3




# #!/usr/bin/python3
# """8-main"""
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     r1 = Rectangle(10, 10, 10, 10)
#     print(r1)  # Output: [Rectangle] (1) 10/10 - 10/10

#     r1.update(height=1)
#     print(r1)  # Output: [Rectangle] (1) 10/10 - 10/1

#     r1.update(width=1, x=2)
#     print(r1)  # Output: [Rectangle] (1) 2/10 - 1/1

#     r1.update(y=1, width=2, x=3, id=89)
#     print(r1)  # Output: [Rectangle] (89) 3/1 - 2/1

#     r1.update(x=1, height=2, y=3, width=4)
#     print(r1)  # Output: [Rectangle] (89) 1/3 - 4/2




# #!/usr/bin/python3
# """General tests for Rectangle and Square classes."""
# from models.rectangle import Rectangle
# from models.square import Square

# # Test Rectangle
# r1 = Rectangle(4, 6, 2, 1, 12)
# print(r1)
# print(r1.area())
# r1.display()

# print("---")

# r2 = Rectangle(2, 3, 2, 2, 13)
# print(r2)
# print(r2.area())
# r2.display()

# print("---")

# # Test Square
# s1 = Square(5)
# print(s1)
# print(s1.area())
# s1.display()

# print("---")

# s2 = Square(2, 2)
# print(s2)
# print(s2.area())
# s2.display()

# print("---")

# s3 = Square(3, 1, 3)
# print(s3)
# print(s3.area())
# s3.display()





# #!/usr/bin/python3
# """10-main"""
# from models.square import Square

# if __name__ == "__main__":

#     s1 = Square(5)
#     print(s1)       # Output: [Square] (1) 0/0 - 5
#     print(s1.size)  # Output: 5
#     s1.size = 10
#     print(s1)       # Output: [Square] (1) 0/0 - 10

#     try:
#         s1.size = "9"
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))




# #!/usr/bin/python3
# """ 11-main """
# from models.square import Square

# if __name__ == "__main__":

#     s1 = Square(5)
#     print(s1)

#     s1.update(10)
#     print(s1)

#     s1.update(1, 2)
#     print(s1)

#     s1.update(1, 2, 3)
#     print(s1)

#     s1.update(1, 2, 3, 4)
#     print(s1)

#     s1.update(x=12)
#     print(s1)

#     s1.update(size=7, y=1)
#     print(s1)

#     s1.update(size=7, id=89, y=1)
#     print(s1)







# #!/usr/bin/python3
# """ 12-main """
# from models.rectangle import Rectangle

# if __name__ == "__main__":

#     r1 = Rectangle(10, 2, 1, 9, id=None)
#     print(r1)
#     r1_dictionary = r1.to_dictionary()
#     print(r1_dictionary)
#     print(type(r1_dictionary))

#     r2 = Rectangle(1, 1)
#     print(r2)
#     r2.update(**r1_dictionary)
#     print(r2)
#     print(r1 == r2)




# #!/usr/bin/python3
# """ 13-main """
# from models.square import Square

# if __name__ == "__main__":

#     s1 = Square(10, 2, 1)
#     print(s1)
#     s1_dictionary = s1.to_dictionary()
#     print(s1_dictionary)
#     print(type(s1_dictionary))

#     s2 = Square(1, 1)
#     print(s2)
#     s2.update(**s1_dictionary)
#     print(s2)
#     print(s1 == s2)




from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
