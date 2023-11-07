#!/usr/bin/python3


def delete_at(my_list=None, idx=0):
    if my_list is None:
        my_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[:] = [my_list[i] for i in range(len(my_list)) if i != idx]  # Update the original list
    return my_list  # Return the modified list

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)
