#!/usr/bin/python3
def weight_average(my_list=None):
    if my_list is None:
        my_list = []
    if not my_list:
        return 0

    sum_products = 0
    sum_weights = 0

    for score, weight in my_list:
        sum_products += score * weight
        sum_weights += weight

    return sum_products / sum_weights


# Example usage
if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
