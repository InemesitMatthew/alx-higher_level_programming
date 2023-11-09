#!/usr/bin/python3


# # Get all the names defined in hidden_4 module
# module_names = dir(hidden_4)

# # Filter and print the names that do not start with double underscores
# for name in sorted(module_names):
#     if not name.startswith("__"):
#         print(name)

if __name__ == '__main__':
    import hidden_4
    words = dir(hidden_4)


    for word in words:
        if word[:2] != '__':
            print(word)