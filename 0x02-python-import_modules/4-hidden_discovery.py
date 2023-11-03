#!/usr/bin/python3
import hidden_4

# Get all the names defined in hidden_4 module
module_names = dir(hidden_4)

# Filter and print the names that do not start with double underscores
for name in sorted(module_names):
    if not name.startswith("__"):
        print(name)
