#!/usr/bin/python3
"""
Module to print text with 2 new lines after '.', '?', and ':'
"""


def text_indentation(text):
    """
    Function to print text with 2 new lines after '.', '?', and ':'

    Args:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.

    Returns:
    - None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")

    lines = text.splitlines()
    for line in lines:
        print(line.strip())


if __name__ == "__main__":
    text_indentation(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres"""
    )
