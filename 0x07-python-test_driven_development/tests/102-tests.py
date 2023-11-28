import ctypes

lib = ctypes.CDLL("./libPython.so")
lib.print_python_string.argtypes = [ctypes.py_object]

s1 = "The spoon does not exist"
s2 = "ложка не существует"
s3 = "La cuillère n'existe pas"
s4 = "勺子不存在"
s5 = "숟가락은 존재하지 않는다."
s6 = "スプーンは存在しない"
s7 = b"The spoon does not exist"

lib.print_python_string(s1)
lib.print_python_string(s2)
lib.print_python_string(s3)
lib.print_python_string(s4)
lib.print_python_string(s5)
lib.print_python_string(s6)
lib.print_python_string(s7)
