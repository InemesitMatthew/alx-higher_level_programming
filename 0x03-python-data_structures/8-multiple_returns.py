#!/usr/bin/python3


def multiple_returns(sentence):
    first_char = None if len(sentence) == 0 else sentence[0]
    length = len(sentence)

    return (length, first_char)


# Example usage
if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
