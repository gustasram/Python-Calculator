from number_input import input_number
from math_symbol_input import input_math_symbol
from math_solving import solve_math
from result_print import print_result

number_list = []

while True:
    # Entering a number and quitting if the input is letter 'q' or 'Q'
    number = input_number()
    number_list.append(number)
    if number == 'q':
        break

    # If the number list has 2 numbers in it, the equation is solved
    if len(number_list) == 2:
        number = solve_math(number_list[0], number_list[1], math_sign)
        number_list = print_result(number, number_list, math_sign)

    # Entering a math symbol and quitting if the input is letter 'q' or 'Q'
    math_sign = input_math_symbol()
    if math_sign == 'q':
        break
