"""Function allows to print the result of the equation and to clear and append the list with the result"""

def print_result(number, number_list, math_sign):
    print(f"{number_list[0]} {math_sign} {number_list[1]} = {number}")
    number_list = []
    number_list.append(number)
    return number_list