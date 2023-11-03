#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1

if num_args == 0:
    print("0 arguments.")
else:
    if num_args == 1:
        arg_word = "argument:"
    else:
        arg_word = "arguments:"
        print(f"{num_args} {arg_word}")

        for i, arg in enumerate(argv[1:], 1):
            print(f"{i}: {arg}")
