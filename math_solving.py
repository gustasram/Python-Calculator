"""Function solves math problems with symbols that are chosen by a user"""

def solve_math(number_1, number_2, operator):
    if operator == "+":
        sum = number_1 + number_2
    elif operator == "-":
        sum = number_1 - number_2
    elif operator == "*":
        sum = number_1 * number_2
    elif operator == "/":
        sum = number_1 / number_2
    elif operator == "^":
        sum = number_1 ** number_2
    return sum